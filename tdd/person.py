class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        # self.name = self.first_name + " " + self.last_name

    @property
    def name(self):
        return self.first_name + " " + self.last_name

    def birthday(self):
        self.age += 1
