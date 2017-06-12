import numpy as np
from character import Character
from helper_functions import add_elevens, add_tens, add_poisoner, add_NRV_family, add_50_bonus, add_snow_white_77, \
    add_brothers_sisters_2772_3663


def add_family_rules(a_dict):
    add_elevens(a_dict)
    add_tens(a_dict)
    add_poisoner(a_dict)
    add_NRV_family(a_dict)


def add_unique_rules(a_dict):
    add_50_bonus(a_dict)
    add_snow_white_77(a_dict)
    add_brothers_sisters_2772_3663(a_dict)


def add_bonus_cards(a_dict):
    pass


def create_the_dict(n_cards):

    the_dict = np.array([Character(id=i, name="numero  " + str(i), value=i, text="", text_id="") for i in range(n_cards)])
    add_family_rules(the_dict)
    add_unique_rules(the_dict)
    add_bonus_cards(the_dict)

    return the_dict


if __name__ == '__main__':

    n_cards = 80
    the_dict = create_the_dict(80)
    for i in range(n_cards):
        print(the_dict[i].get_card())

