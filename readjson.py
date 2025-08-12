import json 
from random import randint
select_current_page = 1
select_random_page = True
current_page = randint(1, 182) if select_random_page == True else select_current_page

def load_json():
    try:
        with open('frequency.json', 'r') as parsed_data:
        # Parsing the JSON file into a Python dictionary
            frequency_data = json.load(parsed_data)
            return frequency_data
    except:
        print("Json file not found.")

data = load_json()

def access_json():
    try:
        print("---"*15)
        for i in data[current_page-1].get(f"Page {current_page}"):
            print(i)
    except IndexError:
        print("Invalid page number. Choose a number between 1 and 182")
    finally:
        print("---"*15)
        print(f"Showing entries for page {current_page}")

access_json()