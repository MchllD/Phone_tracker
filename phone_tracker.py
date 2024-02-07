import tkinter 
import tkintermapview
import phonenumbers
import opencage

from key import key

from phonenumbers import geocoder
from phonenumbers import carrier 

from tkinter import *
from tkinter import messagebox

from opencage.geocoder import OpenCageGeocode

root = tkinter.Tk()
root.geometry("500x500")

label1 = Label(text="Phone Number Tracker")
label1.pack()

def  getResult():
    num = number.get("1.0", END)
    num1 = phonenumbers.parse(num,)
    
    location = geocoder.description_for_number(num1, "en")
    service_provider = carrier.name_for_number(num1, "en")
    
    
    
    result.insert(END, "The country of this number is: " + location)
    result.insert(END, "\nThe sim card of this number is: " + service_provider)

number = Text(height=1)
number.pack()

button = Button(text="Search", command=getResult)
button.pack(pady = 10, padx=100)

result = Text(height=7)
result.pack()

root.mainloop()