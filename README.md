Scribus Plugin for Importing Articles from XML:-

Overview
This project provides a Scribus plugin script that imports news article titles and descriptions from an XML file into a Scribus document. The script uses the Scribus Scripter API and the xml.etree.ElementTree library for XML parsing.

Features:-
Imports article titles and descriptions from an XML file.
Creates separate text frames for titles and descriptions.
Titles are bold and larger in font size.
Descriptions are in a smaller font size.
Proper spacing between titles and descriptions.
Basic error handling for missing files and invalid XML formats.

Dependencies:-
Scribus 1.5.8 or later
Python 3.6 or later
xml.etree.ElementTree library (comes pre-installed with Python)

Installation:-
1) Install Scribus: Make sure Scribus is installed on your system. You can download it from the official Scribus website.
2) Ensure Python is Installed: Scribus comes with an embedded Python interpreter, but ensure you have Python 3.6 or later on your system if you plan to run or modify the script outside Scribus.

Usage:-
1) Open Scribus: Launch Scribus on your computer.
2) Create or Open a Document: Open an existing Scribus document or create a new one where you want to import the articles.

3) Run the Script:-
Save the provided script to a .py file, for example, import_articles.py.
In Scribus, go to Script -> Execute Script... and select the import_articles.py file.
4) Select XML File: When prompted, select the XML file containing the articles (e.g., articles.xml).
5) View Imported Articles: The script will create text frames for each article title and description in the document. Titles will be bold and larger, while descriptions will be in a smaller font.

Example XML Format:-
Ensure your XML file follows this structure:-
<articles>
  <article>
    <title>This is the first article title</title>
    <description>This is a short description of the first article.</description>
  </article>
  <article>
    <title>This is the second article title</title>
    <description>This is a short description of the second article.</description>
  </article>
</articles>

Assumptions:-
The XML file follows a simple structure with articles, article, title, and description tags.
The document has enough space to accommodate the imported text frames.
The fonts Arial and Arial Bold are available in Scribus. You can modify the script to use different fonts if necessary.
The user running the script has basic knowledge of navigating Scribus and executing scripts.

Troubleshooting:-
No Document Open: Ensure you have a Scribus document open before running the script.
File Not Found: Ensure the XML file path is correct and the file exists.
Invalid XML Format: Check the structure of your XML file to ensure it matches the expected format.

Contact:-
For further assistance, you can reach out to the project maintainer at [pathanbn1996@gmail.com].


