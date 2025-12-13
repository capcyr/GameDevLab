class student:
    #Constructor
    def __init__(self, name, year, age, colorshirt):
        self.name = name
        self.year = year
        self.age = age
        self.colorshirt = colorshirt
    def details(self):
        self.name = input("What is your name ")
        self.year = input("What year are you in ")
        self.age = input("How old are you ")
        self.colorshirt = input("What color is your shirt ")
    def detailed(self):
        print(self.name)
        print(self.year)
        print(self.age)
        print(self.colorshirt)


#object creation to create an object you need a variable for the first student
f_student = student("Billy",8,14,"red")
f_student.detailed()
f_student.details()
f_student.detailed()



