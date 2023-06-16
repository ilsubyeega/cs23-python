class Score:
    def __init__(self, point):
        self.point = point

    def setPoint(self, point):
        if 0 <= point <= 100:
            self.point = point
        else:
            raise ValueError()
    
    def getPoint(self):
        return self.point

class GradeScore(Score):
    def __init__(self, point):
        self.setPoint(point)

    def setPoint(self, point):
        super().setPoint(point)

        if point >= 90:
            self.grade = 'A'
        elif point >= 80:
            self.grade = 'B'
        elif point >= 70:
            self.grade = 'C'
        else:
            self.grade = 'F'

    def getGrade(self):
        return self.grade
    

score = Score(95)
print(score.getPoint())
gscore = GradeScore(90)
print(gscore.getPoint())
print(gscore.getGrade())
gscore.setPoint(88)
print(gscore.getPoint())
print(gscore.getGrade())