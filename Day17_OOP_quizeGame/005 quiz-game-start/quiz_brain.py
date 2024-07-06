class QuizeBrain :
    
    def __init__(self,question_list):
        
        self.question_number =0
        self.que_list =question_list
        self.score =0
    
    def still_has_question(self):
        return self.question_number < len(self.que_list)
    
    def next_question(self):
            currunt_que = self.que_list[self.question_number].text
            correct_ans =self.que_list[self.question_number].answer
            self.question_number +=1
            ans =input(f"Q {self.question_number}: {currunt_que} True / False ?")
            self.check_ans(ans,correct_ans)
            
    def check_ans (self,user_ans,correct_ans):
         
        if user_ans.lower() ==correct_ans.lower():
            
            self.score+=1
            print("Yes ! You are right.")
            print(f"yor score is {self.score}/{self.question_number}")
        else :
            print("oops ! this is wrong ")
            print(f"yor score is {self.score}/{self.question_number}")
        print(f"the right ans is {correct_ans}")