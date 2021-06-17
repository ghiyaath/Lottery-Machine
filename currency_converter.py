import requests
from tkinter import *
from tkinter import messagebox


def convert():
   information = 'https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/' + entry_1.get()
   exchange_data = requests.get(information).json()
   rates = float(entry_2.get()) * exchange_data['conversion_rates'][entry_3.get()]
   messagebox.showinfo("Your Amount", rates)


window = Tk()
window.title("Lottery Machine")
window.geometry("700x550")
window.config(bg="yellow")

entry1 = Label(window, text="From Currency :", bg="yellow", font=("Arial", 15))
entry1.place(x=50, y=50)
entry_1 = Entry(window)
entry_1.place(x=400, y=50)

entry2 = Label(window, text="Enter Amount :", bg="yellow", font=("Arial", 15))
entry2.place(x=50, y=120)
entry_2 = Entry(window)
entry_2.place(x=400, y=120)

entry3 = Label(window, text="To Currency (SA) :", bg="yellow", font=("Arial", 15))
entry3.place(x=50, y=190)
entry_3 = Entry(window)
entry_3.place(x=400, y=190)

change_btn = Button(window, text="Exit", bg="blue", fg="white", borderwidth=5, font="Arial 15 bold")
change_btn.place(x=400, y=550)

clear_btn = Button(window, text="Clear", bg="blue", fg="white", borderwidth=5, font="Arial 15 bold", command=convert)
clear_btn.place(x=400, y=350)

return_btn = Button(window, text="Return", bg="blue", fg="white", borderwidth=5, font="Arial 15 bold")
return_btn.place(x=450, y=400)


window.mainloop()

