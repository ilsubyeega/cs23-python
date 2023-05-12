# 앞서 정의한 `LectureScore` 클래스 정의에 `__str__()` 메소드를 추가하여, 이 메소드가 호출될 때 전체 과목명이 공백으로 구분된 문자열이 반환되도록 하라.
# 풀이: `assignment_6_5_3.py`에서 `__str__()` 내부 메소드 구현.

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
        return sum(self.get_lecture_sum(item) for item in self.lectures.keys())

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

# ASSIGNMENT START - Implement `__str__()` method
lecture = LectureScore()
lecture.add_lecture('korean')
lecture.add_lecture('english')
lecture.add_lecture('japanese')
lecture.add_lecture('cpp')
lecture.add_lecture('rust')
print(lecture.lectures)
print(lecture)
# ASSIGNMENT END