from tkinter import *
from tkinter import messagebox

# creation of the window
window = Tk()
window.title("Lottery Machine")
window.geometry("700x800")
window.config(bg="yellow")


def play_again():
    msg_box = messagebox.askquestion("would you like to try again ?", icon='warning')
    if msg_box == "yes":
        window.destroy()
        import lotto_numbers


# generation of numbers
# lotto game
def play_lotto():
    import random
    lotto_list = []
    while len(lotto_list) < 6:
        num = random.randint(1, 49)
        lotto_list.append(num)

    ent_1.insert(0, lotto_list[0])
    ent_2.insert(0, lotto_list[1])
    ent_3.insert(0, lotto_list[2])
    ent_4.insert(0, lotto_list[3])
    ent_5.insert(0, lotto_list[4])
    ent_6.insert(0, lotto_list[5])
# the numbers you play would be compared to the winning numbers and if you get 2 numbers you'd win some money and from 2 until 6
# tells you exactly how much you win
    lotto_list = set(lotto_list)
    entered_numbers = {int(en_1.get()), int(en_2.get()), int(en_3.get()), int(en_4.get()), int(en_5.get()), int(en_6.get())}
    count = lotto_list.intersection(entered_numbers)
    win_not = len(count)
    print(win_not)
    if win_not == 2:
        messagebox.showinfo("Congratulations ", "You win R20.00")
    elif win_not == 3:
        messagebox.showinfo("Congratulations", "You win R100.50")
    elif win_not == 4:
        messagebox.showinfo("Congratulations", "You win R2,384.00")
    elif win_not == 5:
        messagebox.showinfo("Congratulations", "you win R8,584.00")
    elif win_not == 6:
        messagebox.showinfo("Congratulations", "You win R10 000 000.00")
        # if you do not win a messagebox will pop up
    else:
        messagebox.showinfo("You Lose", "Please Try Again")


# Labels
value_label = Label(window, text="Lottery", font=("Italic", 25))
value_label.config(bg="yellow")
value_label.pack()

value_label2 = Label(window, text="Play Here", font=("Italic", 25))
value_label2.config(bg="yellow")
value_label2.pack()

lbl_heading = Label(window, text="Place Your Numbers", font=("Garuda bold", 20), bg="yellow")
lbl_heading.place(x=150, y=150)
# spinbox where you play your numbers
en_1 = Spinbox(window, from_=1, to=49, width=2, font=("Ariel", 25))
en_1.place(x=50, y=200, width=80)

en_2 = Spinbox(window, from_=1, to=49, width=2, font=("Ariel", 25))
en_2.place(x=150, y=200, width=80)

en_3 = Spinbox(window, from_=1, to=49, width=2, font=("Ariel", 25))
en_3.place(x=250, y=200, width=70)

en_4 = Spinbox(window, from_=1, to=49, width=2, font=("Ariel", 25))
en_4.place(x=350, y=200, width=70)

en_5 = Spinbox(window, from_=1, to=49, width=2, font=("Ariel", 25))
en_5.place(x=450, y=200, width=80)

en_6 = Spinbox(window, from_=1, to=49, width=2, font=("Ariel", 25))
en_6.place(x=550, y=200, width=70)
# label that states the today's winning numbers
lbl2_heading = Label(window, text="Today's Lotto Numbers", font=("Garuda bold", 20), bg="yellow")
lbl2_heading.place(x=150, y=300)
# Where the winning numbers would be displayed
ent_1 = Entry(window)
ent_1.place(x=50, y=350, width=40, height=25)

ent_2 = Entry(window)
ent_2.place(x=150, y=350, width=40, height=25)

ent_3 = Entry(window)
ent_3.place(x=250, y=350, width=40, height=25)

ent_4 = Entry(window)
ent_4.place(x=350, y=350, width=40, height=25)

ent_5 = Entry(window)
ent_5.place(x=450, y=350, width=40, height=25)

ent_6 = Entry(window)
ent_6.place(x=550, y=350, width=40, height=25)

# BUTTONS
play_lotto_No_btn = Button(text="Play Lotto Numbers", bg="black", fg="white", borderwidth=5, font="Ariel 12 bold", command=play_lotto)
play_lotto_No_btn.place(x=250, y=400, height=70, width=200)

play_again_btn = Button(text="Play Again ?", bg="blue", fg="white", borderwidth=5, font="Ariel 12 bold", command=play_again)
play_again_btn.place(x=50, y=550, height=70, width=170)


# messagebox which asks you if you want to exit the application if so it would close the window
def close():
    msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application",
                                     icon='warning')
    if msg_box == "yes":
        window.destroy()
# if not it will return you to the current window
    else:
        messagebox.showinfo("Return", "You will now return to the App", icon="warning")


def claim():
    msg_box = messagebox.askquestion("Congratulations", "Would You Like To Claim?")
    if msg_box == "yes":
        window.destroy()
        import Claim_reward
    else:
        window.destroy()


# Takes you to claim whatever you win
claim_reward_btn = Button(text="Claim Reward !", bg="red", fg="white", borderwidth=5, font="Ariel 13 bold", command=claim)
claim_reward_btn.place(x=480, y=550, height=70, width=170)

# EXIT BUTTON
exit_btn = Button(text="Exit", bg="grey", fg="white", borderwidth=5, font="Ariel 15 bold", command=exit)
exit_btn.place(x=250, y=700, height=70, width=170)


# clears the numbers and winning numbers so you can play again
def clear():
    en_1.delete(0, END)
    en_2.delete(0, END)
    en_3.delete(0, END)
    en_4.delete(0, END)
    en_5.delete(0, END)
    en_6.delete(0, END)

    ent_1.delete(0, END)
    ent_2.delete(0, END)
    ent_3.delete(0, END)
    ent_4.delete(0, END)
    ent_5.delete(0, END)
    ent_6.delete(0, END)


# clear button
clear_btn = Button(text="Clear", bg="grey", fg="white", borderwidth=5, font="Ariel 15 bold", command=clear)
clear_btn.place(x=270, y=550, height=70, width=170)

window.mainloop()
