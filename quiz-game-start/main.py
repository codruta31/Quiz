from quiz_structure import Question
from data import raw_questions
from quiz_structure import Quiz

questions = []

for element in raw_questions:
	question_text = element['text']
	question_answer = element['answer']
	new_question = Question(question_text, question_answer)
	questions.append(new_question)

quiz = Quiz(questions)
