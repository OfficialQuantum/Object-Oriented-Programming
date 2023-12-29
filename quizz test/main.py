from question_model import Question
from a_data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)


game_on = True
while game_on:
    while quiz.still_has_question():
        quiz.next_question()
    if quiz.still_has_question():
        continue
    else:
        print("You've completed the quiz")
        print(f"Your final score is: {quiz.score}/{len(question_bank)}")
        game_on = False


