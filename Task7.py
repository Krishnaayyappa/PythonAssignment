#1
import math

C=50
H=30
inputNumbers = input("Please provide the values of D seperated by Comma")
numbersList = inputNumbers.split(',')
resultValues= []
for D in numbersList:
    Q = math.sqrt((2 * C * int(D)) / H)
    resultValues.append(Q)

print(resultValues)
    


#2
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,len):
        Shape.__init__(self)
        self.len = len

    def area(self):
        return self.len*self.len


square1 = Square(10)
print(square1.area())


#3


class Sumtozero:
    def __init__(self, list1):
        self.list1 = list1

    def output(self):
        n = len(self.list1)
        x=1
        y=2
        output = []
        for i in range(0, n-2):
            for j in range(x, n-1):
                for k in range(y, n):
                    if self.list1[i] + self.list1[j] + self.list1[k] == 0:
                        output.append([self.list1[i], self.list1[j], self.list1[k]])
                y = y+1
            x=x+1
            y=x+1

        print(output)


object1 = Sumtozero([12, 13, 14, -5, -7, -4, -9])
object1.output()

#4
class Time:
    def __init__(self, hours, minuites):
        self.h = hours
        self.m = minuites

    def addTime(t1,t2):
        t3 = Time(0,0)
        t3.h = t1.h + t2.h
        t3.m = t1.m + t2.m
        if (t3.m >60):
            t3.h = t3.h + t3.m//60
            t3.m = t3.m % 60
        return t3

    def displayTime(self):
        print("{} hours {} minuites.".format(self.h, self.m))

    def displayMinuite(self):
        print("{} minuites".format(self.h*60 + self.m))



t1 = Time(2, 50)
t2 = Time(3,15)
totTime = Time.addTime(t1,t2)
totTime.displayTime()
totTime.displayMinuite()


#5
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
        






