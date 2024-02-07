import tkinter 
import tkintermapview
import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier 

from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()
root.geometry("500x500")

label1 = Label(text="Phone Number Tracker")
label1.pack()

number = Text(height=1)
number.pack()

button = Button(text="Search")
button.pack(pady = 10, padx=100)

result = Text(height=7)
result.pack()

root.mainloop()