from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            fill=THEME_COLOR,
            font=("Arial", 15, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_btn_img = PhotoImage(file="images/true.png")
        false_btn_img = PhotoImage(file="images/false.png")

        self.true_button = Button(
            image=true_btn_img,
            highlightthickness=0,
            borderwidth=0,
            activebackground=THEME_COLOR,
            command=self.guess_true,
        )
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(
            image=false_btn_img,
            highlightthickness=0,
            borderwidth=0,
            activebackground=THEME_COLOR,
            command=self.guess_false,
        )
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def guess_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def guess_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
