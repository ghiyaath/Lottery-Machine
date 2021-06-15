from tkinter import *
from tkinter import messagebox
from playsound import playsound
import rsaidnumber
from datetime import date
from dateutil.relativedelta import relativedelta

window = Tk()
window.title("Lottery Machine")
window.geometry("700x550")
window.config(bg="yellow")

value_label = Label(window, text="Log-In Details", font=("Arial", 25))
value_label.config(bg="yellow")
value_label.pack()

# img = PhotoImage(file="mic.png")
# lbl = Label(window, image=img).place(x=250, y=100, width=200, height=150)


entry1 = Label(window, text="FULLNAME :", bg="yellow", font=("Arial", 15))
entry1.place(x=50, y=50)
entry_1 = Entry(window)
entry_1.place(x=200, y=50)

entry2 = Label(window, text="E-Mail :", bg="yellow", font=("Arial", 15))
entry2.place(x=50, y=100)
entry_2 = Entry(window)
entry_2.place(x=200, y=100)

entry3 = Label(window, text="ID Number :", bg="yellow", font=("Arial", 15))
entry3.place(x=50, y=150)
entry_3 = Entry(window)
entry_3.place(x=200, y=150)


def entry_1():
    if eval(entry_1.get()) != str(entry_1.get()):
        messagebox.showerror("Error", "Please enter your Fullname")

    elif entry1 == " ":
        messagebox.showerror("Error", "Enter correct details")

    else:
        messagebox.showinfo("Correct info given")


def verify():
    try:
        #   Calculates the age.
        id_number = rsaidnumber.parse(entry_3.get())
        birth_date = id_number.date_of_birth
        real_age = relativedelta(date.today(), birth_date.date())
        real_age = real_age.years
        #  Checks if the id_number is valid.
        if len(entry_3.get()) != 13:
            messagebox.showerror("Error", "Please enter correct ID number")

        elif id_number == " ":
            messagebox.showerror("Error", "Enter correct details")

        elif real_age >= 18:
            real_age = str(real_age)
            messagebox.showinfo("You are " + real_age + " years old", "You can play")
            window.destroy()
            playsound("DaBaby Oh lord, Jetson made another one sound effect.mp3")
            import lotto_numbers

        else:
            messagebox.showinfo("You're not old enough", "")
        # Shows error sign
    except ValueError:

        messagebox.showerror("", "")


def quit_program():
    msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application ?", icon='warning')
    if msg_box == "yes":
        window.destroy()
    else:
        messagebox.showinfo("Return", "You will now return to the App", icon="warning")


exit_btn = Button(window, text="Exit", bg="blue", fg="white", borderwidth=5, font="Arial 15 bold", command=quit_program)
exit_btn.place(x=400, y=350)


verify_btn = Button(window, text="Verify", bg="blue", fg="white", borderwidth=5, font="Arial 15 bold", command=verify)
verify_btn.place(x=100, y=350)


window.mainloop()
