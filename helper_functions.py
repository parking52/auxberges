
text_id_1="Angry against nn"

def add_elevens(a_dict):
    for i in range(len(a_dict)):
        if i % 11 == 0:
            a_dict[i].text = a_dict[i].text + '\n' + text_id_1

text_id_2="Angry against %10"

def add_tens(a_dict):
    for i in range(len(a_dict)):
        if i % 10 == 0:
            a_dict[i].text = a_dict[i].text+ '\n' + text_id_2


text_id_3="Poisons the dragon"

def add_poisoner(a_dict):
    for i in range(len(a_dict)):
		if type((i**0.5)) is int:
            a_dict[i].text = a_dict[i].text+ '\n' + text_id_3


#Glossary of text ids
#text_id_1="Angry against nn"
#text_id_2="Angry against %10"
#text_id_3="Poisons the dragon"