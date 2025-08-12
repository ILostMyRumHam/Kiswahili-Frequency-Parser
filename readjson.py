import json 
from random import randint
select_current_page = input("Select a page between 1 and 183: ")

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
        current_page = int(select_current_page)
        print("---"*15)
        print(f"Entries for page {current_page}")
        print("---"*15)
        for i in data[current_page-1].get(f"Page {current_page}"):
            print(i)
    except (IndexError, ValueError):
        current_page = randint(1, 183)
        print("---"*15)
        print("This page number is not valid. Showing a random page instead.")
        print(f"Entries for page {current_page}")
        print("---"*15)
        for i in data[current_page-1].get(f"Page {current_page}"):
            print(i)
    finally:
        print("---"*15)
        print(f"Entries for page {current_page}")
        print("---"*15)

access_json()
