#asks the questions
#check if correct
#check if end of quiz

#which question

class QuizBrain():


    def __init__(self,  q_list):
        self.question_number = 0 
        self.question_list = q_list



#retrieve the item at the current question_number from the question_list
#user the input() function to show the user the Question text and ask for the user's answer
    def next_question(self):
        curr_question = self.question_list[self.question_number]
        input(f'Question {self.question_number}: {curr_question.text} True or False?')
        self.question_number = self.question_number + 1
