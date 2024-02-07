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
    
    ocg = OpenCageGeocode(key)
    query = str(location)
    results = ocg.geocode(query)
    
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    
    my_label = LabelFrame(root)
    my_label.pack(pady=20)
    
    map_widget = tkintermapview.TkinterMapView(my_label, width=450, corner_radius=0)
    map_widget.set_position(lat, lng)
    map_widget.set_marker(lat, lng, text = "Phone Location")
    map_widget.set_zoom(9)
    map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    map_widget.pack()
    
    adr = tkintermapview.convert_coordinates_to_address (lat, lng)
    
    result.insert(END, "The country of this number is: " + location)
    result.insert(END, "\nThe sim card of this number is: " + service_provider)
    
    result.insert(END, "\nLatitude is: " + str(lat))
    result.insert(END, "\nLongitude is: " + str(lng))

number = Text(height=1)
number.pack()

button = Button(text="Search", command=getResult)
button.pack(pady = 10, padx=100)

result = Text(height=7)
result.pack()

root.mainloop()