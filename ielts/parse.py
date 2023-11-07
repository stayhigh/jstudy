from lxml import html
import sys

htmlfile = sys.argv[1]
# Load the HTML content from the file
#with open("arm.html", "r") as file:
with open(htmlfile, "r") as file:
    html_content = file.read()

# Parse the HTML content
parsed_html = html.fromstring(html_content)

# Define the XPath expression to select all span elements with class="COLLO"
#xpath_expression = "//span[@class='COLLO']"
#xpath_expression = "//span[@class='Collocate']"
xpath_expression = "//span[@class='ldoceEntry Entry']"

# Use the XPath expression to select the desired elements
result = parsed_html.xpath(xpath_expression)

# Loop through the selected elements and print their text content
for element in result:
    for sub_element in element.iterdescendants():
        if 'class' in sub_element.attrib:
            class_name = sub_element.attrib['class']
            #if class_name != 'neutral span' and class_name.startswith("COLLO") and class_name.startswith("EXAMPLE"):
            if class_name == "EXAMPLE":
                #print(f"Tag: {sub_element.tag}|Class: {class_name}|Content: {sub_element.text_content()}")
                print(f"Class: {class_name}|Content: {sub_element.text_content().lstrip()}")
    print("-"*10)
