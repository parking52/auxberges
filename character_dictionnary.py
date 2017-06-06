import numpy as np
from character import Character
from helper_functions import add_elevens


n_cards = 80
n_bonus_cards = 20

the_dict = np.array([Character(id=i, name="numero  " + str(i), value=i, text="", text_id="") for i in range(n_cards)])


add_elevens(the_dict)



for i in range(n_cards):
    print(the_dict[i].get_card())