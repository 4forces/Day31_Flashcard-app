from tkinter import *
from tkinter import messagebox
import random
import pandas
import csv

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("French words Flashcards")
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)

canvas = Canvas(height=600, width=1000, bg = BACKGROUND_COLOR, highlightthickness = 0)
cardfront_img = PhotoImage(file="./images/card_front.png")

canvas.grid(row=0, column=0, columnspan = 2)
canvas_image = canvas.create_image(500, 300, image= cardfront_img)
cardback_img = PhotoImage(file="./images/card_back.png")
top_text = canvas.create_text(500,200,text = "Language", fill="black", font=("Arial", 40, "italic"))
bottom_text = canvas.create_text(500,400,text = "Word", fill="black", font=("Arial", 60, "bold"))

dataframe = pandas.read_csv("./data/french_words.csv")
print(dataframe)
words_dict = dataframe.to_dict()
french_list = list(words_dict['French'])
print(french_list)

num = random.choice(french_list)
print(type(num))


#TODO - Unknown button
def i_know():
    global num

    # print(words_dict)
    french_word = words_dict['French'][num]
    canvas.create_image(500, 300, image= cardfront_img)
    top_text = canvas.create_text(500, 200, text="French", fill="black", font=("Arial", 40, "italic"))
    bottom_text = canvas.create_text(500, 400, text=french_word, fill="black", font=("Arial", 60, "bold"))
    # canvas.itemconfig(top_text, text = "French")
    # canvas.itemconfig(bottom_text, text=
    french_list.remove(num)
    tolearn_dict = words_dict.pop(num)

    dataframe2 = pandas.DataFrame(list(tolearn_dict.items()), columns=['French', 'English'])
    dataframe2.to_csv('to_learn.csv', index=False)

    window.after(3000, flip_card)

def dun_know():
        global num

        print(words_dict)
        french_word = words_dict['French'][num]
        canvas.create_image(500, 300, image=cardfront_img)
        top_text = canvas.create_text(500, 200, text="French", fill="black", font=("Arial", 40, "italic"))
        bottom_text = canvas.create_text(500, 400, text=french_word, fill="black", font=("Arial", 60, "bold"))
        # canvas.itemconfig(top_text, text = "French")
        # canvas.itemconfig(bottom_text, text=french_word)
        window.after(3000, flip_card)

def flip_card():
    global num
    canvas.create_image(500, 300, image=cardback_img)
    # english_text = canvas.create_text(500,200,text ="English", fill = "white", font = ("Arial", 40, "italic"))
    english = canvas.create_text(500,200, text= "English", fill="white", font=("Arial", 40, "italic"))
    words_dict = dataframe.to_dict()
    english_word = words_dict['English'][num]
    english_display = canvas.create_text(500,400, text= english_word, fill="white", font=("Arial", 60, "bold"))
    # canvas.itemconfig(top_text, text="English", fill = "white")
    # canvas.itemconfig(bottom_text, text=english_word, fill = "white")
    num = random.randint(0, 102)
    window.after_cancel(flip_card)

cross_image = PhotoImage(file="./images/wrong.png")
cross_button = Button(image= cross_image, highlightthickness = 0, command = dun_know)
cross_button.grid(row=1, column=0)

tick_image = PhotoImage(file="./images/right.png")
tick_button = Button(image= tick_image, highlightthickness = 0, command = i_know)
tick_button.grid(row=1, column=1)



window.mainloop()