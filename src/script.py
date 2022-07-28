from tkinter import *
from datetime import time

"""
GROUND STATION GUI Version 0.9-beta
Author: Calista Greenway
Since: 06/19/2022
Created for University of Massachusetts Rocket Team (Payload Sub-Team)
This program parses and displays data from sensors onboard the launch vehicle. 
"""

root = Tk()
root.geometry('1920x1080')
root.title("Ground Station")

# Program Counter
counter = 0
counter_label = Label(root, width=20, bg='#ffffff')
counter_label.place(relx=1.0, rely=1.0, anchor='se')

def program_counter():
    global counter

    seconds = counter % 60
    minutes = (counter // 60) % 60
    hours = (counter // (60 * 60)) % (60 * 60)

    dt = time(second=seconds, minute=minutes, hour=hours)
    string = dt.isoformat(timespec='auto')
    display = string

    counter_label.config(text="T+//"+display)
    counter += 1
    
    root.after(1000, program_counter)  # loop counter

# Main Functions
program_counter()

# Execute Tkinter
root.mainloop()
