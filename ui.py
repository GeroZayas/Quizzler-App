from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 18, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        # --------------------------- images ---------------------------
        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")

        # --------------------------- main window ---------------------------
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        # --------------------------- label ---------------------------
        self.score_label = Label(
            text=f"Score:0",
            bg=THEME_COLOR,
            fg="white",
            font=("Arial", 11, "bold"),
            pady=20,
            padx=20
        )
        self.score_label.grid(column=2, row=1)

        # --------------------------- Canvas ---------------------------
        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.canvas.grid(column=1, row=2, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="HEY HEY HEY",
            font=FONT,
            fill=THEME_COLOR
        )

        # --------------------------- Buttons ---------------------------
        self.true_button = Button(
            image=true_image,
            bd=1,
            highlightthickness=0,
            command=self.true_pressed
        )
        self.true_button.grid(row=3, column=1, padx=20, pady=20)

        self.false_button = Button(
            image=false_image,
            bd=1,
            highlightthickness=0,
            command=self.false_pressed
        )
        self.false_button.grid(row=3, column=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text="That's the end of the quiz",
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(600, self.get_next_question)



