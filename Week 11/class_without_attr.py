class Score:
    def set(self, point):
        self.point = point
    def get(self):
        return self.point

a = Score()
a.set(100)

print(a.get())