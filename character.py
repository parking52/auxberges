

class Character():

    def __init__(self, id, name, value, text_id, text):
        self.id = id
        self.name = name
        self.value = value
        self.text_id = text_id
        self.text = text

    # def __repr__(self):
    #     return str(self.value) + self.color
    #
    # def __str__(self):
    #     return str(self.value) + self.color

    def get_card(self):
        return str("id: " + str(self.id) + '\n'
                   + "name: " + str(self.name) + '\n'
                   + "value: " + str(self.value) + '\n'
                   + "text: " + self.text + '\n')

