from utility.account import Account
from utility.lecture import LectureScore

my_account = Account(1000)
my_lecture = LectureScore()
my_account.deposit(1000)
print(my_account.get_balance())
my_lecture.add_lecture('math')
my_lecture.add_lecture_score('math', 95)
print(my_lecture.get_lecture_scores('math'))