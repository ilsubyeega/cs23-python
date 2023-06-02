# Copied from Week 13/assignment_8_3_2_plus_8_5_1/utility/lecture.py
import struct

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

    def get_lectures(self):
        return list(self.__lectures.keys())
    
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

my_lecture = LectureScore()
my_lecture.add_lecture('korean')
my_lecture.add_lecture('english')
my_lecture.add_lecture_score('korean', 90)
my_lecture.add_lecture_score('korean', 95)
my_lecture.add_lecture_score('korean', 88)
my_lecture.add_lecture_score('english', 88)
my_lecture.add_lecture_score('english', 91)
my_lecture.add_lecture_score('english', 93)

# NOTE: This problem does not solve the problem of three lecture? I'm not sure what the textbook going to say.
# > 각 교과목 성적이 세 과목이 아니라 서로 다를 때이다. 이런 문제를 해겨랗는 프로그램을 작성하라.
with open('Week 14/lecture_dump.tmp', 'wb') as io_write:
    for lecture in my_lecture.get_lectures():
        # FIX: Make lecture name into variable length.
        encoded_lecture_name = lecture.encode()
        len_lcecture = len(encoded_lecture_name)

        # Write the length first.
        io_write.write(struct.pack('>i', len_lcecture))
        packed = struct.pack(f'>{len_lcecture}s3i', encoded_lecture_name, *my_lecture.get_lecture_scores(lecture))
        io_write.write(packed)

with open('Week 14/lecture_dump.tmp', 'rb') as io_read:
    while True:
        raw = io_read.read(4)
        if not raw:
            break # no more data.

        len_lecture = struct.unpack('>i', raw)[0]
        raw = io_read.read(struct.calcsize(f'>{len_lecture}s3i'))
        lecture_name, *scores = struct.unpack(f'>{len_lecture}s3i', raw)
        print(f'{lecture_name.decode().strip()} {scores}')