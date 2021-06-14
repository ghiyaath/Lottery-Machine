from tkinter import *

window = Tk()
window.title("Lottery Machine")
window.geometry("800x600")
window.config(bg="yellow")

value_label = Label(window, text="Log-In Details", font=("Arial", 25))
value_label.config(bg="yellow")
value_label.pack()

entry1 = Label(window, text="FULLNAME :", bg="yellow", font=("Arial", 15))
entry1.place(x=50, y=50)
entry1 = Entry(window)
entry1.place(x=200, y=50)

entry1 = Label(window, text="Street Name :", bg="yellow", font=("Arial", 15))
entry1.place(x=400, y=50)
entry1 = Entry(window)
entry1.place(x=540, y=50)

entry1 = Label(window, text="Street No. ", bg="yellow", font=("Arial", 15))
entry1.place(x=400, y=100)
entry1 = Entry(window)
entry1.place(x=540, y=100)

entry1 = Label(window, text="Area :", bg="yellow", font=("Arial", 15))
entry1.place(x=400, y=150)
entry1 = Entry(window)
entry1.place(x=540, y=150)

entry2 = Label(window, text="E-Mail :", bg="yellow", font=("Arial", 15))
entry2.place(x=50, y=100)
entry2 = Entry(window)
entry2.place(x=200, y=100)

entry3 = Label(window, text="ID Number :", bg="yellow", font=("Arial", 15))
entry3.place(x=50, y=150)
entry3 = Entry(window)
entry3.place(x=200, y=150)


def ex():
    window.destroy()
    import lotto_numbers


exit_btn = Button(text="Quit", bg="blue", fg="white", borderwidth=5, font=("Arial 15 bold"), command=ex)
exit_btn.place(x=500, y=350, height=70, width=80)

verify_btn = Button(window, text="Submit Details", bg="blue", fg="white", borderwidth=5, font=("Arial 15 bold"), command=exit)
verify_btn.place(x=100, y=350, height=70, width=152)

window.mainloop()
