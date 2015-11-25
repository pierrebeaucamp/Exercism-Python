class Allergies:
    items = ["cats", "pollen", "chocolate", "tomatoes", "strawberries",
             "shellfish", "peanuts", "eggs"]
    lst = []

    def __init__(self, score=0):
        score = bin(score)[2:]
        score = '00000000'[len(score):] + score

        self.lst = [] # Reset the list to delete previous items
        for i in range(len(score)):
            if score[i] == '1': self.lst.extend([self.items[i]])

    def is_allergic_to(self, item):
        return item in self.lst
