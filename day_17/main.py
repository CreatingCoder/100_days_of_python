from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    q = Question(i['text'], i['answer'])
    question_bank.append(q)

qb = QuizBrain(question_bank)

while qb.still_has_questions():
    qb.next_question()

print(f'Done with the quiz!  Your final score is {qb.score}/{len(question_bank)}')



