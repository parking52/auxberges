
def add_elevens(a_dict):
    for i in range(len(a_dict)):
        if i % 11 == 0:
            a_dict[i].text = a_dict[i].text + "angry against nn"