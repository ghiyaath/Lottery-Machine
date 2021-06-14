from tkinter import *

window = Tk()
window.title("Lottery Machine")
window.geometry("700x800")
window.config(bg="yellow")

value_label = Label(window, text="Lottery", font=("Italic", 25))
value_label.config(bg="yellow")
value_label.pack()

value_label2 = Label(window, text="Play Here", font=("Italic", 25))
value_label2.config(bg="yellow")
value_label2.pack()

lbl_heading = Label(window, text="Place Your Numbers", font=("Garuda bold", 20), bg="yellow")
lbl_heading.place(x=150, y=150)

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

lbl2_heading = Label(window, text="Today's Lotto Numbers", font=("Garuda bold", 20), bg="yellow")
lbl2_heading.place(x=150, y=300)

en_1 = Entry(window)
en_1.place(x=50, y=350, width=40, height=25)

en_2 = Entry(window)
en_2.place(x=150, y=350, width=40, height=25)

en_3 = Entry(window)
en_3.place(x=250, y=350, width=40, height=25)

en_4 = Entry(window)
en_4.place(x=350, y=350, width=40, height=25)

en_5 = Entry(window)
en_5.place(x=450, y=350, width=40, height=25)

en_6 = Entry(window)
en_6.place(x=550, y=350, width=40, height=25)

play_lotto_No_btn = Button(text="Play Lotto Numbers", bg="black", fg="white", borderwidth=5, font=("Ariel 12 bold"))
play_lotto_No_btn.place(x=250, y=400, height=70, width=200)

play_again_btn = Button(text="Play Again ?", bg="blue", fg="white", borderwidth=5, font=("Ariel 12 bold"))
play_again_btn.place(x=50, y=550, height=70, width=170)

claim_reward_btn = Button(text="Claim Reward !", bg="red", fg="white", borderwidth=5, font=("Ariel 13 bold"))
claim_reward_btn.place(x=480, y=550, height=70, width=170)

exit_btn = Button(text="Exit", bg="grey", fg="white", borderwidth=5, font=("Ariel 15 bold"))
exit_btn.place(x=250, y=700, height=70, width=170)


window.mainloop()
