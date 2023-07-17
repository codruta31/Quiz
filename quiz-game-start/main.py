from quiz_structure import Question
from data import raw_questions
from quiz_structure import Quiz

questions = []
# populate the new list with objects from class Question, by iterating into the raw_question list
for element in raw_questions:
	question_text = element['text']
	question_answer = element['answer']
	new_question = Question(question_text, question_answer)
	questions.append(new_question)
# creating the quiz object form the Quiz class
quiz = Quiz(questions)
