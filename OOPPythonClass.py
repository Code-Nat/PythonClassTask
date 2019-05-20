class student:
    scoreSum = 0
    ageSum = 0
    Students = 0

    def __init__(self, age, score):
        self.age = age
        self. score = score

        student.scoreSum += score
        student.ageSum += age
        student.Students += 1

    @classmethod
    def scoreAvrage(cls):
        return cls.scoreSum/cls.Students
    @classmethod
    def ageAvrage(cls):
        return cls.ageSum/cls.Students

studentsList = { student (19,57), student (59,23), student (23,100), student (27,78) }
for i in studentsList:
    print (i.age,i.score)

print ("Score avrage is:",student.scoreAvrage(),"Age avrage", student.ageAvrage())



    
    