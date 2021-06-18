import requests
from tkinter import *
from tkinter import messagebox


# Coverts the currencies according to all the different exchange rates
def convert():
    information = 'https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/' + entry_1.get()
    exchange_data = requests.get(information).json()
    rates = float(entry_2.get()) * exchange_data['conversion_rates'][entry_3.get()]
    messagebox.showinfo("Your Amount", rates)


# creation of the window
window = Tk()
window.title("Currency Converter")
window.geometry("600x500")
window.config(bg="yellow")

# Labels and entries in the window
entry1 = Label(window, text="From Currency :", bg="yellow", font=("Arial", 15))
entry1.place(x=50, y=50)
entry_1 = Entry(window)
entry_1.place(x=400, y=50)

entry2 = Label(window, text="Enter Amount :", bg="yellow", font=("Arial", 15))
entry2.place(x=50, y=120)
entry_2 = Entry(window)
entry_2.place(x=400, y=120)

entry3 = Label(window, text="To Currency (Foreign) :", bg="yellow", font=("Arial", 15))
entry3.place(x=50, y=190)
entry_3 = Entry(window)
entry_3.place(x=400, y=190)
# changes the currency to another
change_btn = Button(window, text="Exit", bg="blue", fg="white", borderwidth=5, font="Arial 15 bold")
change_btn.place(x=400, y=550)
# clears all input that has been inserted
convert_btn = Button(window, text="Convert", bg="blue", fg="white", borderwidth=5, font="Arial 15 bold", command=convert)
convert_btn.place(x=200, y=350)


def back():
    msg_box = messagebox.askquestion("Return Application", "Are you sure you want to return?", icon='warning')
    if msg_box == "yes":
        window.destroy()
        import currency_converter
    else:
        messagebox.showinfo("Return", "You will now return to the ", icon="warning")


# returns you
return_btn = Button(window, text="Return", bg="blue", fg="white", borderwidth=5, font="Arial 15 bold", command=back)
return_btn.place(x=450, y=350)


window.mainloop()

