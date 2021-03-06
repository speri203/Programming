# Day 12 consisted of inheritance. You had a Person class and a Student class that inherits from Person
# Instructed to build default constructor and finish out calculate filter
# link: https://www.hackerrank.com/challenges/30-inheritance/problem


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, score):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.score = score

    def calculate(self):
        average_score = sum(self.score) / len(self.score)
        if average_score < 50:
            return "T"
        elif 40 < average_score < 55:
            return "D"
        elif 55 < average_score < 70:
            return "P"
        elif 70 < average_score < 80:
            return "A"
        elif 80 < average_score < 90:
            return "E"
        else:
            return "O"


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
