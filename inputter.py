def format_text(page):
    page_text = page.replace('\n', '')
    page_text = page_text.replace('\n', '')
    page_text = page_text.split('\u2022')
    #page_text = page_text.strip()
    return page_text


import fitz #this is just pymupdf
import json #for storing the raw data
pdf = fitz.open("HelpLine-Resource-Directory.pdf")
hyperlinks_text = []
pages_hypers = []
sections_hypers = []
compiled_sections = []
# Iterate through each page
for page in range(len(pdf)):
    page = pdf.load_page(page)
    links = page.get_links()
    page_text = page.get_text("text")
    page_text = format_text(page_text)
    for link in links:
        if 'uri' in link:
            #from is the bounding box the link is in
            rect = fitz.Rect(link['from'])
            text = page.get_text("text", clip=rect)
            hyperlinks_text.append((text.strip(), link['uri']))
            pages_hypers.append((text.strip(), link['uri']))
    
    for section in page_text:
        for text, hyperlink in pages_hypers:
            if text in section:
                sections_hypers.append(hyperlink + ", ")
        #might need to tuple this later, probably not though
        compiled_sections.append(f'Text: {section}. Hyperlinks Attatched: {" ".join(sections_hypers)}')
        sections_hypers.clear()
    pages_hypers.clear()

#print(compiled_sections[1])
with open ('rawdata.txt', 'w') as file:
    json.dump(compiled_sections, file)

#for loading the list
#with open (rawdata.txt, 'r') as file:
    #data = json.load(file)