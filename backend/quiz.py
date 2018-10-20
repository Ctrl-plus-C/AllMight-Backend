from requests import get
import pprint
import random
# import event 


class Question:
    def __init__(self):
        self.ans = 0
        self.ans_list = []
        self.ques = ""

    def gen_questions(self):
        url = ('https://opentdb.com/api.php?amount=1')
        response = get(url).json()['results'][0]
        answers = response['incorrect_answers']
        corr = response['correct_answer'] 
        pos = random.randint(0,len(answers))
        self.ans = pos
        self.ans_list = answers
        self.ques = response['question']
        answers.insert(pos,corr)

    def print_ques(self):
        question = "Q. "+str(self.ques)+"\n"
        for i in range(len(self.ans_list)):
            loc = chr(ord('A') + i)
            question+=str(loc)+". "+str(self.ans_list[i])+"    "
        print(question)

    def check_ans(self,ip):
        ans_char = chr(ord('A') + self.ans)
        if ip == ans_char:
            print("Correct Answer!!")
        else:
            print("Incorrect :/ The correct answer is "+str(self.ans_list[self.ans]))

# def caller():
#     QB = Question()
#     QB.gen_questions()
#     QB.print_ques()
#     x = input()
#     QB.check_ans(x.upper())
        

# caller()