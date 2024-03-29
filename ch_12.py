class Person:
    def __init__(self, firstName, lastName, idNumber):
	    self.firstName = firstName
	    self.lastName = lastName
	    self.idNumber = idNumber

    def printPerson(self):
	    print("Name:", self.lastName + ",", self.firstName)
	    print("ID:", self.idNumber)
        

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNum, scores):
        self.scores = scores
        super().__init__(firstName, lastName, idNum)


    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        media = sum(self.scores)/ len(self.scores)
        if media < 40:
            return 'T'
        elif media < 55:
            return 'D'
        elif media < 70:
            return 'P'
        elif media < 80:
            return 'A'
        elif media < 90:
            return 'E'
        elif media <= 100:
            return 'O'
        else:
            return ''

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
#numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
