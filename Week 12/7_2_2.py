# Copied from Week 11/assignment_6_6_2.py

class LectureScore:
    RANGE_OF_SCORE = (0, 100)
    RANGE_MIN = RANGE_OF_SCORE[0]
    RANGE_MAX = RANGE_OF_SCORE[1]

    def __init__(self):
        self.lectures = {} # {lecture_name: [scores]}

    # ASSIGNMENT START - Implement `__str__()` method
    def __str__(self):
        return ' '.join(self.lectures.keys())
    # ASSIGNMENT END

    def add_lecture(self, lec_name: str):
        if lec_name not in self.lectures.keys():
            self.lectures[lec_name] = []
    
    def get_lecture_scores(self, lec_name: str):
        return self.lectures[lec_name]
    
    def get_lecture_sum(self, lec_name: str):
        return sum(self.get_lecture_scores(lec_name))
    
    def add_lecture_score(self, lec_name: str, score: int):
        if LectureScore.RANGE_MIN <= score <= LectureScore.RANGE_MAX:
            self.lectures[lec_name].append(score)
        else:
            raise ValueError(f'Score is out of range. Should be in {LectureScore.RANGE_OF_SCORE}.')
    
    def modify_lecture_score(self, lec_name: str, idx: int, score: int):
        if LectureScore.RANGE_MIN <= score <= LectureScore.RANGE_MAX:
            self.lectures[lec_name][idx] = score
        else:
            raise ValueError(f'Score is out of range. Should be in {LectureScore.RANGE_OF_SCORE}.')

    def get_total_score(self):
        return sum(self.get_lecture_sum(key) for key in self.lectures.keys())

    def get_lecture_average(self, lec_name: str):
        return self.get_lecture_sum(lec_name) / len(self.get_lecture_scores(lec_name))

    def get_average(self):
        total_avg_score = sum(self.get_lecture_average(key) for key in self.lectures.keys())
        return total_avg_score / len(self.lectures)

class IdentifiedLectureScore(LectureScore):
    def __init__(self, *, id):
        self.id = id
        super().__init__() # <-- Required
    
    def get_id(self):
        return self.id

ourScore = IdentifiedLectureScore(id='1537')
print(ourScore.get_id())
ourScore.add_lecture('korean')