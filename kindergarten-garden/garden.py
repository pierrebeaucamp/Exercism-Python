PLANTS = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}

class Garden():
    def __init__(self, cups, students=[]):
        self.cups = cups.split("\n")
        self.students = sorted(students) if students else [
            "Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny",
            "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"
        ]

    def plants(self, student):
        i = self.students.index(student) * 2
        return [PLANTS[c] for c in (self.cups[0][i:i+2] + self.cups[1][i:i+2])]
