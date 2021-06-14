from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.title("Lottery Machine")
window.geometry("800x600")
window.config(bg="yellow")

banks = Combobox(window)
banks.pack()
banks["values"] = "Capitec", "ABSA", "FNB", "Nedbank"
value_label = Label(window, text="Congratulations !", font=("Arial", 25))
value_label.config(bg="yellow")
value_label.pack()

value_label = Label(window, text="Claim Your Reward Here", font=("Arial", 25))
value_label.config(bg="yellow")
value_label.pack()

window.mainloop()
