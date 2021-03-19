# Day 4 focuses on classes and instances. You are instructed to complete Person class
# which takes a age and then based on that age prints out an output. Age can also
# be incremented by a value of 1 each time yearPasses is called. 
# Link: https://www.hackerrank.com/challenges/30-class-vs-instance/problem

class Person:
    def __init__(self, initialAge):
        self.age = initialAge

    def amIOld(self):
        if self.age < 0:
            self.age = 0
            print("Age is not valid, setting age to 0.")
        elif self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        self.age += 1


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
