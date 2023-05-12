# 구현되어 있지 않은 `LectureScore` 클래스의 나머지 메소드를 구현하고, 정상적으로 동작하는 가를 시험하는 프로그램을 작성하라.

class LectureScore:
    RANGE_OF_SCORE = (0, 100)
    RANGE_MIN = RANGE_OF_SCORE[0]
    RANGE_MAX = RANGE_OF_SCORE[1]

    def __init__(self):
        self.lectures = {} # {lecture_name: [scores]}

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
    

lecture = LectureScore()
lecture.add_lecture('korean')
lecture.add_lecture_score('korean', 95)
lecture.add_lecture_score('korean', 85)

print(lecture.get_lecture_scores('korean')) # [95, 85]
print(lecture.get_lecture_average('korean')) # 90.0
print(lecture.get_average()) # 90.0
print(lecture.get_total_score()) # 180