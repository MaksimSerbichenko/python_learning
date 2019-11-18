class Person:
    def print_info(self):
        print(self.name, "is", self.age)


john = Person()
john.name = "John"
john.age = 22

lucy: Person = Person()
lucy.name = "Lucy"
lucy.age = 20

john.print_info()
lucy.print_info()

