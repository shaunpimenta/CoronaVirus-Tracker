import request_module
import pandas as pd
import numpy as np
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

window = Tk()
window.minsize(300, 300)
window.title("Corona Virus Tracker")
logo = PhotoImage(file="Vector.png")
window.iconphoto(False, logo)
imageLabel = Label(window, image=logo)
imageLabel.grid()

textLabel = Label(window, text="Enter the name of country")
textLabel.grid()

CountryName = StringVar()
entry = Entry(window, width=30, textvariable=CountryName)
entry.grid()


def get_cases():
    nameOfCountry = CountryName.get()
    response = request_module.perform_requests(nameOfCountry)
    messagebox.showinfo("Covid Data","No Confirmed Cases : " + str(response[0]["confirmed"]) + "\nNo of Recovered Cases : " + str(response[0]["recovered"]) + "\nNo of Critical Cases : " + str(
            response[0]["critical"]) + "\nNo of Deaths : " + str(response[0]["deaths"]))


getCasesButton = Button(window, text="Get Data", command=get_cases)
getCasesButton.grid()
