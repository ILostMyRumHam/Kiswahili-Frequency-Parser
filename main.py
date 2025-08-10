import swahili_json_init
from random import randint 
select_random_page = True
pick_a_page = 0

def main():
    '''To pick a specific page select in a range between 0 and 182'''
    current_page = randint(0, 182) if select_random_page == True else pick_a_page
    pdf_page_by_page = swahili_json_init.parse_pdf
    try:
        print(f"List of entries for page: {current_page}")
        print("---"*15)
        print(pdf_page_by_page[current_page])
    except:
        print(f"Page not found. Showing the list of entries for the first page instead")
        print("---"*15)
        print(pdf_page_by_page[0])

main()
if __name__ == "__main__":
    print("---"*15)
    print("This is a parser for Swahili words")
    
