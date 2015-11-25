class Allergies:
    items = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes',
             'chocolate', 'pollen', 'cats']

    def __init__(self, score=0):
        check = lambda x: score & 2**self.items.index(x)
        self.lst = [i for i in self.items if check(i)]

    def is_allergic_to(self, item):
        return item in self.lst
