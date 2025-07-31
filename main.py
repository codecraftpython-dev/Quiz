from tkinter import *
from tkinter import messagebox
import random

questions = [
{"question": "In which year did the French Revolution begin?", "options": ["1789", "1804", "1815", "1792"],
 "correct_answer": "1789"},
{"question": "Which country is known as the Land of the Rising Sun?", "options": ["China", "Japan", "South Korea", "Vietnam"],
 "correct_answer": "Japan"},
{"question": "In which year did the Titanic sink?", "options": ["1912", "1920", "1931", "1945"],
 "correct_answer": "1912"},
{"question": "Who was the first emperor of the Maurya Dynasty?", "options": ["Ashoka", "Chandragupta Maurya", "Bindusara", "Bimbisara"],
 "correct_answer": "Chandragupta Maurya"},
{"question": "The Indian National Congress was founded in which year?", "options": ["1885", "1905", "1890", "1915"],
 "correct_answer": "1885"},
{"question": "Who wrote the famous Hindi poem 'Madhushala'?", "options": ["Harivansh Rai Bachchan", "Ramdhari Singh 'Dinkar'", "Sumitranandan Pant", "Maithili Sharan Gupt"],
 "correct_answer": "Harivansh Rai Bachchan"},
{"question": "What is the currency of Brazil?", "options": ["Peso", "Euro", "Real", "Yen"],
 "correct_answer": "Real"},
{"question": "Who painted the Mona Lisa?", "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
 "correct_answer": "Leonardo da Vinci"},
{"question": "Who wrote the book 'Godan'?", "options": ["Mahadevi Verma", "Suryakant Tripathi 'Nirala'", "Munshi Premchand", "Harivansh Rai Bachchan"],
 "correct_answer": "Munshi Premchand"},
{"question": "Who was the first woman to become the President of India?", "options": ["Pratibha Patil", "Indira Gandhi", "Vijayalakshmi Pandit", "Sarojini Naidu"],
 "correct_answer": "Pratibha Patil"},

]

random.shuffle(questions) #To shuffle questions in a list

current_question = 0
score = 0

def load_question():
    global current_question
    question_data = questions[current_question]
    label_question.config(text = question_data["question"])  #To print question on screen from dictionary

    for i in range(4):
        radio_buttons[i].config(text = question_data["options"][i]) #To print options from dictionary

def next_question():
    global current_question
    global score

    if radio_var.get() is not None:
        selected_option = radio_buttons[int(radio_var.get())]["text"]
        correct_answer = questions[current_question]["correct_answer"]

        if selected_option == correct_answer:
            score += 1

        current_question += 1
        radio_var.set(None)

        if current_question < len(questions):
            load_question()
        else:
            show_score()
    else:
        messagebox.showinfo("Incomplete", "Please select an option.")

def show_score():
    global current_question
    global score

    messagebox.showinfo("Quiz Completed", f"Your score: {score}/{len(questions)}")
    current_question = 0
    score = 0
    random.shuffle(questions)
    load_question()


def Exit():
    root.destroy()


root = Tk()
root.title("Quiz App")
root.geometry("550x700")
root.wm_iconbitmap("quizicon.ico")

head = Label(root, text = "Quiz Challenge", font = "arial 30 bold underline", fg = "yellow", bg = "red")
head.pack(pady = 10, fill = X)

details = Label(root, text = "Check your knowledge through this quiz...", font = "arial 15 bold", fg = "blue")
details.pack(pady = 10)

label_question = Label(root, text="", font = "arial 15 bold")
label_question.pack(pady=10)


radio_var = StringVar()

radio_var.set(None)  #For initially none of them is selected


radio_buttons = []

for i in range(4):
    radio_btn = Radiobutton(root, text = "", font = "arial 13 bold", variable = radio_var, value = i)
    radio_btn.pack()
    radio_buttons.append(radio_btn)


next_button = Button(root, text = "Next", font = "arial 15 bold", bg = "#29F914", command = next_question)
next_button.pack(pady = 10)

restart_button = Button(root, text = "Restart", font = "arial 15 bold", bg = "#04FCDE", command = show_score)
restart_button.pack(pady = 10)

clear = Button(root, text = "Exit", bg = "purple", font = "arial 18 bold", padx = 20, command = Exit)
clear.pack(anchor = "ne", pady = 10, padx = 20)

load_question()

root.mainloop()
