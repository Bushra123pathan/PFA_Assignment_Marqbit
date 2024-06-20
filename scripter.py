import scribus
import xml.etree.ElementTree as ET

def import_articles_from_xml(xml_file):
    try:
        # Parse the XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Set initial positions for text frames
        x_position = 10
        y_position = 10
        title_font_size = 18
        description_font_size = 12
        vertical_spacing = 20
        
        for article in root.findall('article'):
            # Extract title and description
            title = article.find('title').text
            description = article.find('description').text
            
            # Create text frame for title
            title_frame = scribus.createText(x_position, y_position, 400, 50)
            scribus.setText(title, title_frame)
            scribus.setFont("Arial Bold", title_frame)
            scribus.setFontSize(title_font_size, title_frame)
            
            # Adjust y_position for description
            y_position += title_font_size + vertical_spacing
            
            # Create text frame for description
            description_frame = scribus.createText(x_position, y_position, 400, 50)
            scribus.setText(description, description_frame)
            scribus.setFont("Arial", description_frame)
            scribus.setFontSize(description_font_size, description_frame)
            
            # Adjust y_position for next article
            y_position += description_font_size + 2 * vertical_spacing
            
    except FileNotFoundError:
        scribus.messageBox("Error", f"The file {xml_file} was not found.", icon=scribus.ICON_WARNING, button1=scribus.BUTTON_OK)
    except ET.ParseError:
        scribus.messageBox("Error", f"The file {xml_file} is not a valid XML file.", icon=scribus.ICON_WARNING, button1=scribus.BUTTON_OK)

# Specify the XML file to import
xml_file = "example.xml"
import_articles_from_xml(xml_file)
