
import javax.xml.XMLConstants;
import javax.xml.transform.Source;
import javax.xml.transform.stream.StreamSource;
import javax.xml.validation.*;
//import java.net.URL; //Somente para uso de arquivos via URL
import org.xml.sax.SAXException;
import java.io.File; // Somente para uso de arquivos
import java.io.IOException;

class ValidadorXML {
    public static void main(String[] args) {
        
        // webapp example xsd: 
        // URL schemaFile = new URL("http://java.sun.com/xml/ns/j2ee/web-app_2_4.xsd");
        // local file example:
        // File schemaFile = new File("/location/to/localfile.xsd");
        
        File schemaFile = new File(args[0]); //.xsd file
        Source xmlFile = new StreamSource(new File(args[1])); //.xml file
        SchemaFactory schemaFactory = SchemaFactory
                .newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
        try {
            Schema schema = schemaFactory.newSchema(schemaFile);
            Validator validator = schema.newValidator();
            validator.validate(xmlFile);
            System.out.println(xmlFile.getSystemId() + " Documento Válido!");
        } catch (SAXException e) {
            System.out.println(xmlFile.getSystemId() + " Documento Inválido" + e);
        } catch (IOException e) {
            System.out.println(e);
        }
    }

}
