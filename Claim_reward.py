from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Creation of the window
window = Tk()
window.title("Bank Details")
window.geometry("800x600")
window.config(bg="yellow")


def convert():
    window.destroy()
    import currency_converter


def confirm():
    with open("user.txt", "r", encoding="utf-8-sig", errors="ignore")as file:
        for line in file:
            if "email :" in line:
                print(line.split(":")[1])
                email = line.split(",")[1][8:len(line.split(",")[1])]

    sender_email = "ghiyaathwilliams2@gmail.com"
    receiver_email = email
    password = input("Type your password and press enter:")

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = ", ".join(receiver_email)

    a_message = """\
    hello
    i
    y
    """

    part1 = MIMEText(a_message, "plain")

    message.attach(part1)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


# heading at the top of the window
value_label = Label(window, text="Claim Your Reward Here", font=("Arial", 25))
value_label.config(bg="yellow")
value_label.pack()
# labels and entries for the application
lbl_heading = Label(window, text="Insert Account Holder Name :", font=("Garuda bold", 17), bg="yellow")
lbl_heading.place(x=50, y=150)
entry1 = Entry(window)
entry1.place(x=450, y=155)

lbl_heading2 = Label(window, text="Insert Bank Account Number :", font=("Garuda bold", 17), bg="yellow")
lbl_heading2.place(x=50, y=250)
entry2 = Entry(window)
entry2.place(x=450, y=255)

lbl_heading3 = Label(window, text="Select Your Bank :", font=("Garuda bold", 17), bg="yellow")
lbl_heading3.place(x=50, y=350)
# Combobox that contains all the banks you can select from
banks = Combobox(window)
banks.pack()
banks["values"] = "Capitec", "ABSA", "FNB", "Nedbank", "Standard Bank", "Investec Bank",
value_label = Label(window, text="Congratulations !", font=("Arial", 25))
value_label.config(bg="yellow")
value_label.pack()
banks.place(x=300, y=355)


# closes your window
def close():
    msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit ?", icon='warning')
    if msg_box == "yes":
        window.destroy()
    else:
        messagebox.showinfo("Return", "You will now return to the login", icon="warning")


# Exit button that exits the window
exit_btn = Button(text="Quit", bg="blue", fg="white", borderwidth=5, font="Arial 15 bold", command=close)
exit_btn.place(x=600, y=450, height=70, width=80)
# Converts the money from one currency to another
Currency_converter_btn = Button(window, text="Currency Converter", bg="blue", fg="white", borderwidth=5, font="Arial 10 bold", command=convert)
Currency_converter_btn.place(x=320, y=450, height=70, width=152)
submit_btn = Button(text="Submit", bg="blue", fg="white", borderwidth=5, font="Arial 15 bold", command=confirm)
submit_btn.place(x=100, y=450)

window.mainloop()
