from typing import List, Dict


class LectureScore:
    lecture_list: List[str] = []
    lecture_scores_dict: Dict[str, List[int]] = {}

    def add_lecutre(self, lec_name):
        self.lecture_list.append(lec_name)
        self.lecture_scores_dict[lec_name] = []

    #def get_lecture_scores(self, lec_name):
    def get_lecture_score(self, lec_name):
        return self.lecture_scores_dict[lec_name]
    
    def get_lecture_sum(self, lec_name):
        return sum(self.get_lecture_score(lec_name))
    
    def add_lecture_score(self, lec_name, score):
        self.get_lecture_score(lec_name).append(score)

    def modify_lecture_score(self, lec_name, idx, score):
        self.get_lecture_score(lec_name)[idx] = score

    def get_total_score(self):
        sum_val = 0
        for item in self.lecture_scores_dict.keys():
            sum_val += self.get_lecture_sum(item)
        return sum_val

lec_score_lee = LectureScore()
lec_score_lee.add_lecture('korean')
lec_score_lee.add_lecture_score('korean', 95)