from question_model import Question
from data import question_data
from quiz_brain import QuizeBrain

question_bank =[]

for question in question_data:
    
    que_text =question["text"]
    que_ans =question["answer"]
    obj =Question(que_text,que_ans)
    question_bank.append(obj)
    

quize =QuizeBrain(question_bank)



while quize.still_has_question():
    quize.next_question()
    
    
print("The Quize is ended !")

print(f"the final score is {quize.score}/{quize.question_number}")