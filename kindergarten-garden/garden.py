class Garden():
    def __init__(self, cups, students=[]):
        if not students: students = [
            "Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny",
            "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"
        ]
        self.cups = cups.split("\n")
        self.students = sorted(students)

    def plants(self, student):
        i = self.students.index(student) * 2
        out = [self.cups[n][i+j:i+j+1] for n in range(2) for j in range(2)]
        plants = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}
        return [plants[c] for c in out]
