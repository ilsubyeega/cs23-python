# 앞서 정의한 `LectureScore` 클래스와 그 파생 클래스 `IdentifiedLectureScore`의 인스턴스 변수 `lectures`, `id`는 객체 외부에서의 접근을 제한할 필요가 있는 것이다. 이 두 인스턴스 변수을 비공개 변수가 되도록 각 클래스를 수정하여라.
# Copied from ./7_2_2.py
# Copied from Week 11/assignment_6_6_2.py

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

ourScore = IdentifiedLectureScore(id='1537')
print(ourScore.get_id())
ourScore.add_lecture('korean') # works through.