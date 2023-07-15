#asks the questions
#check if correct
#check if end of quiz

#which question

class QuizBrain():


    def __init__(self,  q_list):
        self.question_number = 0 
        self.question_list = q_list
        self.score = 0



#retrieve the item at the current question_number from the question_list
#user the input() function to show the user the Question text and ask for the user's answer
    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number = self.question_number + 1
        user_input = input(f'Question {self.question_number}: {curr_question.text} True or False?')
        self.check_answer(user_input, curr_question.answer)
        

    def still_has_questions(self):
        if(self.question_number < len(self.question_list)):
            return True
        else:
            return False
        
    
    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            print('Correct')
            self.score += 1
        else:
            print(f'Wrong, the correct answer was: {correct_answer}.')
        print(f'Your current score is {self.score}/{self.question_number} \n')

        
