text_id_1 = "Angry against nn"

def add_elevens(a_dict):
    for i in range(len(a_dict)):
        if i % 11 == 0:
            a_dict[i].text = a_dict[i].text + '\n' + text_id_1

text_id_2 = "Angry against %10"

def add_tens(a_dict):
    for i in range(len(a_dict)):
        if i % 10 == 0:
            a_dict[i].text = a_dict[i].text+ '\n' + text_id_2


text_id_3 = "Poisons the dragon"


def add_poisoner(a_dict):
    for i in range(len(a_dict)):
        if type((i**0.5)) is int:
            a_dict[i].text = a_dict[i].text + '\n' + ''


#Glossary of text ids
#text_id_1="Angry against nn"
#text_id_2="Angry against %10"
#text_id_3="Poisons the dragon"

text_id_4 = "-20 for each member of the NRV family [64:69]"
def add_NRV_family(a_dict):
    for i in range(64, 70):
        a_dict[i].text = a_dict[i].text + '\n' + text_id_4

text_id_5 = 'boss is indestructible next turn'
def add_50_bonus(a_dict):
    a_dict[50].text = a_dict[50].text + '\n' + text_id_5

text_id_6 = 'for each 7 in other cards, group gets -10'
def add_snow_white_77(a_dict):
    a_dict[77].text = a_dict[77].text + '\n' + text_id_6

text_id_7 = 'gets a +1 bonus when fighting with his mirror (XY => YX)'
def add_brothers_sisters_2772_3663(a_dict):
    list = [27, 36, 63, 72]
    for i in list:
        a_dict[i].text = a_dict[i].text + '\n' + text_id_7


