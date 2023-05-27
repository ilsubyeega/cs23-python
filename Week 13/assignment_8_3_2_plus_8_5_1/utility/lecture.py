class LectureScore:
    RANGE_OF_SCORE = (0, 100)
    RANGE_MIN = RANGE_OF_SCORE[0]
    RANGE_MAX = RANGE_OF_SCORE[1]

    def __init__(self):
        self.__lectures = {} # {lecture_name: [scores]}

    def __str__(self):
        return ' '.join(self.__lectures.keys())

    def add_lecture(self, lec_name: str):
        if lec_name not in self.__lectures.keys():
            self.__lectures[lec_name] = []
    
    def get_lecture_scores(self, lec_name: str):
        return self.__lectures[lec_name]
    
    def get_lecture_sum(self, lec_name: str):
        return sum(self.get_lecture_scores(lec_name))
    
    def add_lecture_score(self, lec_name: str, score: int):
        if LectureScore.RANGE_MIN <= score <= LectureScore.RANGE_MAX:
            self.__lectures[lec_name].append(score)
        else:
            raise ValueError(f'Score is out of range. Should be in {LectureScore.RANGE_OF_SCORE}.')
    
    def modify_lecture_score(self, lec_name: str, idx: int, score: int):
        if LectureScore.RANGE_MIN <= score <= LectureScore.RANGE_MAX:
            self.__lectures[lec_name][idx] = score
        else:
            raise ValueError(f'Score is out of range. Should be in {LectureScore.RANGE_OF_SCORE}.')

    def get_total_score(self):
        return sum(self.get_lecture_sum(key) for key in self.__lectures.keys())

    def get_lecture_average(self, lec_name: str):
        return self.get_lecture_sum(lec_name) / len(self.get_lecture_scores(lec_name))

    def get_average(self):
        total_avg_score = sum(self.get_lecture_average(key) for key in self.__lectures.keys())
        return total_avg_score / len(self.__lectures)
    

class IdentifiedLectureScore(LectureScore): 
    def __init__(self, *, id):
        self.__id = id
        super().__init__() # <-- Required
    
    def get_id(self):
        return self.__id