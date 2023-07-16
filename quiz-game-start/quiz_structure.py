from tkinter import *


class Question:
	def __init__(self, question_text, answer):
		self.text = question_text
		self.answer = answer


class Quiz:
	def __init__(self, questions):
		self.question_number = 0
		self.score = 0
		self.questions = questions
		# create tkinter screen (GUI)
		self.window = Tk()
		self.window.geometry('600x500')
		self.window.title("Codruta's Quiz")
		# display quiz name on GUI
		self.my_quiz_name = Label(text="Codruta's Quiz", font=30, width=60, height=3)

		#  display the question text for the user in GUI
		self.quiz_display_questions = Label(text=0, width=80)

		# create text box for user to enter the answer
		self.user_response = Entry(width=15)

		# create button to submit answer
		self.submit_answer_button = Button(text='Trimite răspuns!', command=self.check_answer)

		# create a Label object to display if the user's answer is correct or not
		self.status = Label(text=0)

		# create a button to display the next question when clicked
		self.next_question_button = Button(text='Următoarea întrebare', command=self.next_question)

		# create a Label to display the score in real time
		self.current_score_box = Label(text='')

		# display the first question at start
		self.display_current_question()
		# initialize the widgets and set there place on GUI
		self.my_quiz_name.grid(column=0, row=0)
		self.quiz_display_questions.grid(column=0, row=2, sticky=W, padx=2)
		self.user_response.grid(column=0, row=3)
		self.submit_answer_button.grid(column=0, row=4)
		self.status.grid(column=0, row=5)
		self.next_question_button.grid(column=0, row=6)
		self.current_score_box.grid(column=0, row=7)
		# initialize the GUI screen in tkinter
		self.window.mainloop()

	def still_has_questions(self):
		return self.question_number < len(self.questions)

	def display_current_question(self):
		# get the text of the current question from the specified index in the questions list
		current_question = self.questions[self.question_number]
		# create variable for the question number and its adjacent question
		question_text = f'Q.{self.question_number + 1}: {current_question.text} \n '
		# add the text to display for this Label
		self.quiz_display_questions.config(text=str(question_text))

	def check_answer(self):
		user_answer = self.user_response.get()  # get hold of the user input
		current_question = self.questions[self.question_number]
		correct_answer = current_question.answer
		self.submit_answer_button.config(state=DISABLED)
		if user_answer.lower() == correct_answer.lower():
			self.score += 1
			self.status.config(text='Răspuns corect!', fg='green')  # modify the text to display, for the Label 'status'
		else:
			self.status.config(text=f'Răspuns greșit! Răspunsul corect este: {correct_answer}!', fg='red')
		self.current_score_box.config(text=f'Scorul tău actual este: {self.score}/{self.question_number + 1}')

	def next_question(self):
		self.submit_answer_button.config(state=NORMAL)
		self.status.config(text='')
		self.question_number += 1
		if self.still_has_questions():
			self.display_current_question()
			self.user_response.delete(0, END)
		else:

			self.submit_answer_button.destroy()
			self.next_question_button.destroy()
			self.status.destroy()
			self.current_score_box.config(text=f'Ai ajuns la finalul quiz-ului!\nScorul tău final este: {self.score} din {self.question_number} de întrebări.\n {self.end_message()}')

	def end_message(self):
		if self.score < 5:
			final_message_text = 'Scorul tău poate fi îmbunătățit !'
			return final_message_text
		elif 5 >= self.score <= 9:
			final_message_text = 'Te-ai descurcat bine! Felicitări'
			return final_message_text
		else:
			final_message_text = 'Ai făcut o treabă excelentă! Felicitări!'
			return final_message_text
