from tkinter import Tk, Label
from datetime import datetime

window = Tk()
window.title("Digital Clock")
window.geometry('600x300')
window.configure(bg="steelblue")

label = Label(window, text="Welcome!", font=(
    "white", 78, "bold"), bg="steelblue")
label.pack(pady=100)


def clock():
    time = datetime.now().strftime("%H:%M:%S")
    label.configure(text=time)
    label.after(500, clock)


clock()
window.mainloop()
