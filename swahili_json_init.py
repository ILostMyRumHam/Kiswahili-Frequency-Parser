from pypdf import PdfReader
from modules import swahili_frequency_parser
import json

first_page = swahili_frequency_parser.frequency_of_swahili_words_first_page
reader = PdfReader('swahili-freq-10000.pdf')
pdf_length = len(reader.pages)

def pdf_parser(pdf_input: str) -> list:
    '''Parse the pdf starting from the second page of entries'''
    entire_pdf_page_by_page = []
    entire_pdf_page_by_page.append(first_page)
    for page in range(2, pdf_length):
        current_page = pdf_input.pages[page].extract_text()
        parse_current_page = swahili_frequency_parser.parse_frequency(current_page)
        entire_pdf_page_by_page.append(parse_current_page)
    return entire_pdf_page_by_page

parse_pdf = pdf_parser(reader)
""" def json_conversion(parsed_data):
# Convert into JSON
    json_string = ""
    for page in parsed_data:
        json_string += json.dumps([ob.__dict__ for ob in page])
    return json_string

json_string = json_conversion(parse_pdf)
def json_file_init(json_string):
    with open("frequency.json", "w") as out_file:
        json.dump(json_string, out_file, sort_keys = True, indent = 4, ensure_ascii = False)

json_file_init(json_string) """
