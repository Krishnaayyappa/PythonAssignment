class Person:
    def __init__(self, initialAge):
        if(initialAge < 0):
            print("Age is not valid! setting age to zero")
            self.age = 0
        else:
            self.age = initialAge

    def yearPasses(self, age):
        self.age+=age

    
    def amIOld(self):
        if self.age>=0 and self.age <13:
            print("You are young")
        elif self.age>=13 and self.age<=19:
            print("You are a teenager")
        else:
            print("You are old")


p1 = Person(35)
p1.yearPasses(5)
p1.amIOld()
        

