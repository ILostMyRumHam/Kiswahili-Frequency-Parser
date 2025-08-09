from modules import swahili_frequency_parser
import swahili_json_init
def main():
    current_page = 0
    pdf_page_by_page = swahili_json_init.parse_pdf
    print(pdf_page_by_page[current_page])

if __name__ == "__main__":
    print("This is a parser for Swahili words")