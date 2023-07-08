from quiz_body import Question
from data import raw_questions
from quiz_body import QuizBody

questions = []

for element in raw_questions:
	question_text = element['text']
	question_answer = element['answer']
	new_question = Question(question_text, question_answer)
	questions.append(new_question)


quiz = QuizBody(questions)

while quiz.still_has_questions():
	quiz.next_question()

print("You've reached the end of the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
