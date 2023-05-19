class Score:
    def __init__(self, point=0):
        self.set(point)
        print("Score.__init__()")
    def get(self):
        print("Score.get()")
        return self.point
    def set(self, point):
        self.point = point
        print("Score.set()")

class IDScore(Score):
    def __init__(self, id, point=0):
        super().__init__(point)
        self.id = id
        print("IDScore.__init__()")
    def getId(self):
        print("IDScore.get()")
        return self.id
    
myscore = IDScore('ID1000', 100)
print(myscore.getId())
print(myscore.get())
myscore.set(200)
print(myscore.get())