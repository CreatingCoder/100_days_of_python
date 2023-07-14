from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    q = Question(i['text'], i['answer'])
    question_bank.append(q)

   
qb = QuizBrain(question_bank)
qb.next_question()





    





   








