import random
from tkinter import *
from tkinter import messagebox
from playsound import playsound
import rsaidnumber
import smtplib
from email.mime.multipart import MIMEMultipart
from datetime import date
from dateutil.relativedelta import relativedelta
import uuid


uuid.uuid4()
user_id = uuid.uuid4()
# Creation of the window
window = Tk()
window.title("Login Details")
window.geometry("650x500")
window.config(bg="yellow")

value_label = Label(window, text="Log-In Details", font=("Arial", 25))
value_label.config(bg="yellow")
value_label.pack()


# Verifies your email
def email_verify():
    if entry_2.get() == "":
        messagebox.showerror("ERROR", "Enter a Valid Email")
    elif entry_2.get() != "":
        try:
            sender_email_id = "ghiyaathwilliams2@gmail.com"
            receiver_email_id = entry_2.get()
            password = ""
            subject = "Lotto"
            msg = MIMEMultipart()
            msg["From"] = sender_email_id
            msg["To"] = receiver_email_id
            msg["Subject"] = subject
            body = "You are a verified account"
            # msg.attach(MIMEText(body, "plain"))
            text = msg.as_string()
            s = smtplib.SMTP("smtp.gmail.com", 587)
            s.starttls()
            s.login(sender_email_id, password)
            s.sendmail(sender_email_id, receiver_email_id, text)
            s.quit()
            # populate.dict()
        except:
            playsound("wrong sound.mp3")
            messagebox.showerror("ERROR", "Invalid email,please make sure to put in a valid email")
# img = PhotoImage(file="mic.png")
# lbl = Label(window, image=img).place(x=250, y=100, width=200, height=150)


# labels and entries for the window as well as placement
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


# Validates if info given is correct to continue
def entry__1():
    # if eval(entry_1.get()) != str(entry_1.get()):
    #     messagebox.showerror("Error", "Please enter your Fullname")

    if entry_1.get() == "":
        playsound("wrong sound.mp3")
        messagebox.showerror("Error", "You have to enter all fields to continue")

    else:
        messagebox.showinfo("Correct info given", "You have entered the right details")
        playsound("DaBaby Oh lord, Jetson made another one sound effect.mp3")
        window.destroy()
        import lotto_numbers


# Defines if you put in the correct ID number and if you're old enough to play
def verify():
    try:
        #   Calculates the age.
        id_number = rsaidnumber.parse(entry_3.get())
        birth_date = id_number.date_of_birth
        real_age = relativedelta(date.today(), birth_date.date())
        real_age = real_age.years
        player_id = random.sample((1, 10), 1)
        Validate_person()
        #  Checks if the id_number is valid.
        if len(entry_3.get()) != 13:
            playsound("wrong sound.mp3")
            messagebox.showerror("Error", "Please enter correct ID number")

        elif id_number == "":
            playsound("wrong sound.mp3")
            messagebox.showerror("Error", "Enter correct details")

        elif real_age >= 18:
            real_age = str(real_age)
            messagebox.showinfo("You are " + real_age + " years old", "You can play" + "\n" + "\n" + "Player " + str(player_id[0]))
            entry__1()

        else:
            playsound("wrong sound.mp3")
            messagebox.showinfo("Error", "You're not old enough")
        # Shows error sign if you're not old enough
    except ValueError:
        playsound("wrong sound.mp3")
        messagebox.showerror("Error", "Enter A Valid  ID number and try again .")


# gets your information to make you a player id  out of the information that you put in
def Validate_person():
    player = entry_1.get()
    email = entry_2.get()
    Id = entry_3.get()

    playerfile = open("user.txt", "a+")

    playerfile.write("\n")

    playerfile.write("player :" + player)

    playerfile.write("\n")

    playerfile.write("email :" + email)

    playerfile.write("\n")

    playerfile.write("Id :" + Id)


# if you want to exit the window a messagebox would pop up to ask if you want to leave the program
# if not you will return to the current program
def quit_program():
    msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit ?", icon='warning')
    if msg_box == "yes":
        window.destroy()
    else:
        messagebox.showinfo("Return", "You will now return to the login", icon="warning")


# Exit button to exit the window
exit_btn = Button(window, text="Exit", bg="blue", fg="white", borderwidth=5, font="Arial 15 bold", command=quit_program)
exit_btn.place(x=400, y=350)

# verify button to validate if information is correct
# if so then you'll be taken to the following page
verify_btn = Button(window, text="Verify", bg="blue", fg="white", borderwidth=5, font="Arial 15 bold", command=verify)
verify_btn.place(x=100, y=350)


window.mainloop()
