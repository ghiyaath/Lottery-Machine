from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.title("Lottery Machine")
window.geometry("800x600")
window.config(bg="yellow")


value_label = Label(window, text="Claim Your Reward Here", font=("Arial", 25))
value_label.config(bg="yellow")
value_label.pack()

lbl_heading = Label(window, text="Insert Account Holder Name :", font=("Garuda bold", 17), bg="yellow")
lbl_heading.place(x=50, y=150)
entry1 = Entry(window)
entry1.place(x=450, y=155)

lbl_heading2 = Label(window, text="Insert Bank Account Number :", font=("Garuda bold", 17), bg="yellow")
lbl_heading2.place(x=50, y=250)
entry1 = Entry(window)
entry1.place(x=450, y=255)

lbl_heading3 = Label(window, text="Select Your Bank :", font=("Garuda bold", 17), bg="yellow")
lbl_heading3.place(x=50, y=350)

banks = Combobox(window)
banks.pack()
banks["values"] = "Capitec", "ABSA", "FNB", "Nedbank", "Standard Bank", "Investec Bank",
value_label = Label(window, text="Congratulations !", font=("Arial", 25))
value_label.config(bg="yellow")
value_label.pack()
banks.place(x=300, y=355)


def close():
    window.destroy()


exit_btn = Button(text="Quit", bg="blue", fg="white", borderwidth=5, font="Arial 15 bold", command=exit)
exit_btn.place(x=600, y=450, height=70, width=80)

Currency_converter_btn = Button(window, text="Currency Converter", bg="blue", fg="white", borderwidth=5, font="Arial 10 bold", command=exit)
Currency_converter_btn.place(x=320, y=450, height=70, width=152)

verify_btn = Button(window, text="Verify", bg="blue", fg="white", borderwidth=5, font="Arial 15 bold", command=exit)
verify_btn.place(x=50, y=450, height=70, width=152)

window.mainloop()
