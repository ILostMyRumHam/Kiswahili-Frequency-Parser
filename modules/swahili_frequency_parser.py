from dataclasses import dataclass
# Copy a page of the pdf into the input_data variable. It is important that it is wrapped in single quotation marks
input_data = '319511 "na" CC { and }  209978 "ya" GEN-CON 9/10 { of }  141843 "wa" GEN-CON 1/2 { of }  103733 "katika" PREP { in }   99483 "kwa" PREP { with }   99283 "wa" GEN-CON 11 { of }   91707 "sema" V { say }   91328 "wa" V { be }   89472 "za" GEN-CON 9/10 { of }   86246 "wa" GEN-CON 3/4 { of }   81556 "ya" GEN-CON 5/6 { of }   79135 "na" ADV { also }   78388 "wa" V MOD-CAN { be }   77239 "la" GEN-CON 5/6 { of }   52081 "hiyo" PRON DEM ASS-OBJ 9/10 { this }   51577 "mtu" N 1/2 { man }   49593 "cha" GEN-CON 7/8 { of }   40626 "ni" V NOSUBJ { is }   38463 "mwaka" N 3/4 { year }   37368 "ya" GEN-CON 3/4 { of }   36622 "kwamba" CONJ { that }   36555 "katika" PREP { on }   34947 "na" PREP { with }   32861 "*bw." TITLE { *mr. } AN   32756 "fanya" V { do }   30604 "wakati" N 11/10 { time } AR   30585 "serikali" N 9/10 { government } PERS   29518 "ake" PRON 0 { his/her/its }   28052 "lakini" CONJ { but } AR   27048 "hilo" PRON DEM ASS-OBJ 5/6 { this }   26994 "kama" ADV { as } AR   26850 "baada_ya" PREP { after }   26497 "ake" PRON { his/her/its }   26147 "nchi" N 9/10 { earth }   26028 "ni" V NOSUBJ { are }   24755 "au" CONJ CC { or } AR   24694 "vya" GEN-CON 7/8 { of }   24424 "pia" ADV { also }   23370 "nchi" N 9/10 { in }   23062 "taka" V { want }'
# Source for the frequency of words: https://www.researchgate.net/publication/373953169_Frequency_list_of_Swahili_10_000_most_common_words_1

@dataclass
class SwahiliWord:
    '''Class for keeping track of information associated with each word entry'''
    frequency: str
    word: str
    english_possible_definition: str 
    word_class: str
    def __init__(self, frequency: int, word: str, english_possible_definition: str, word_class: str):
        self.frequency = frequency
        self.word = word 
        self.english_possible_definition = english_possible_definition
        self.word_class = word_class
    def __repr__(self):
        return f"Swahili word: '{self.word}', Frequency: '{self.frequency}', Word Class: '{self.word_class}', Possible English Equivalent: '{self.english_possible_definition}'. \n"

def parse_frequency(input_string: str) -> list:
    '''
    Parses the frequency of each word in a decreasing order.
    Because there are certain words like "na" that are listed multiple times,
    and have multiple definitions, their frequencies are also listed
    separately - "na" has different frequencies when used as a coordinating constructor (319511), as an adverb (79135), and as
    a preposition (34947).
    Swahili words that have many English equivalents depending on context are only
    listed with one such possible equivalent per entry.

    Returns a list of instances of the SwahiliWord class for each page of the pdf. 
    '''
    word_classes_reference = {"AD-ADJ": "complement to adjective",
                                "ADJ": "adjective",
                                "ADJ-INFL": "inflecting adjective",
                                "ADJ-PRE": "adjective located before the head",
                                "ADV": "adverb",
                                "CC": "coordinating connector",
                                "CONJ": "conjunction",
                                "DEM": "demonstrative pronoun",
                                "GEN-CON": "genitive connector",
                                "N": "noun",
                                "NUM": "number",
                                "NUM-INFL": "inflecting number",
                                "NUM-UNINF": "uninflecting number",
                                "PERS": "personal pronoun",
                                "PREP": "preposition",
                                "PRON": "pronoun",
                                "V": "verb"
                                }
    splitter = input_string.split("  ")
    parsed_data = []
    for i in splitter:
        if i:
            split_up = i.split()
            try:
                frequency = str(int(split_up[0]))
            except ValueError:
                frequency = "Frequency not found"
            try:
                trim_quotation_marks = split_up[1]
                trim_quotation_marks = trim_quotation_marks.replace('"',"")
                swahili_word = trim_quotation_marks.replace("'","")
            except IndexError:
                swahili_word = "Word not found"
            try:
                english_possible_definition = split_up[split_up.index("{")+1]
            except ValueError:
                english_possible_definition = "English Equivalent not found"
            try:
                word_class = word_classes_reference.get(split_up[2]) if word_classes_reference.get(split_up[2]) != None else "Word Class not found"
            except IndexError:
                word_class = "Word Class not found"
            current_entry = SwahiliWord(frequency=frequency, word=swahili_word, english_possible_definition=english_possible_definition, word_class=word_class)
            parsed_data.append(current_entry)

    return parsed_data

def pretty_print(input_list: list):
    '''
    Prints the input dictionary with some formatting
    '''
    print("\n List of entries: \n")
    for object in input_list:
        print(object)

frequency_of_swahili_words_first_page = parse_frequency(input_data)


