from pypdf import PdfReader
from modules import swahili_frequency_parser
import json
from tqdm import tqdm

first_page = swahili_frequency_parser.frequency_of_swahili_words_first_page
reader = PdfReader('swahili-freq-10000.pdf')
pdf_length = len(reader.pages)

def pdf_parser(pdf_input: str) -> list:
    '''Parse the pdf starting from the second page of entries'''
    entire_pdf_page_by_page = []
    entire_pdf_page_by_page.append(first_page)
    for page in tqdm(range(2, pdf_length)):
        current_page = pdf_input.pages[page].extract_text()
        parse_current_page = swahili_frequency_parser.parse_frequency(current_page)
        entire_pdf_page_by_page.append(parse_current_page)
    return entire_pdf_page_by_page

parse_pdf = pdf_parser(reader)
def json_conversion(parsed_data): # Encoding currently correctly assigns the page
# Convert into JSON
    json_list = []
    page_counter = 1
    with open("frequency.json", "w") as out_file:
        for page in parsed_data:
            json_list.append({f"Page {page_counter}": [ob.__dict__ for ob in page]})
            page_counter +=1
        return json_list

json_list = json_conversion(parse_pdf)

def json_file_init(json_list):
    with open("frequency.json", "w") as out_file:
        json.dump(json_list, out_file, indent = 4, ensure_ascii = False)

json_file_init(json_list)