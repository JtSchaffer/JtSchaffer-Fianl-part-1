import csv
from tkinter import *


class GUI:
    def __init__(self, window):

        self.window = window

        self.frame_tips = Frame(self.window)
        self.label_tips = Label(self.frame_tips, text='Tips')
        self.entry_tips = Entry(self.frame_tips)

        self.label_tips.pack(padx=5, side='left')
        self.entry_tips.pack(padx=10, side='left')
        self.frame_tips.pack(anchor='w', pady=10)

        self.frame_hours = Frame(self.window)
        self.label_hours = Label(self.frame_hours, text='Hours')
        self.entry_hours = Entry(self.frame_hours)

        self.label_hours.pack(padx=5, side='left')
        self.entry_hours.pack(padx=0, side='left')
        self.frame_hours.pack(anchor='w', pady=10)

        self.frame_bottom = Frame(self.window)
        self.bottom_text = Label(self.frame_bottom, text='Day')
        self.date_button = IntVar(None)
        self.date_monday = Radiobutton(self.frame_bottom, text='Monday', variable=self.date_button, value=1)
        self.date_tuesday = Radiobutton(self.frame_bottom, text='Tuesday', variable=self.date_button, value=2)
        self.date_wednesday = Radiobutton(self.frame_bottom, text='Wednesday', variable=self.date_button, value=3)
        self.date_thursday = Radiobutton(self.frame_bottom, text='Thursday', variable=self.date_button, value=4)
        self.date_friday = Radiobutton(self.frame_bottom, text='Friday', variable=self.date_button, value=5)
        self.date_saturday = Radiobutton(self.frame_bottom, text='Saturday', variable=self.date_button, value=6)
        self.date_sunday = Radiobutton(self.frame_bottom, text='Sunday', variable=self.date_button, value=7)

        self.bottom_text.pack(padx=5, side='left')
        self.date_monday.pack(padx=5, side='left')
        self.date_tuesday.pack(padx=5, side='left')
        self.date_wednesday.pack(padx=5, side='left')
        self.date_thursday.pack(padx=5, side='left')
        self.date_friday.pack(padx=5, side='left')
        self.date_saturday.pack(padx=5, side='left')
        self.date_sunday.pack(padx=5, side='left')
        self.frame_bottom.pack(anchor='w', pady=10)

        self.frame_save = Frame(self.window)
        self.save = Button(self.frame_save, text='SAVE', command=self.clicked)

        self.frame_save.pack(anchor='s', pady=10)
        self.save.pack()
    def clicked(self):
        tips = self.entry_tips.get()
        hours = self.entry_hours.get()
        day = self.date_button.get()
        hourly = float(tips) / float(hours)
        if day == 1:
            day = 'Monday'
        elif day == 2:
            day = 'Tuesday'
        elif day == 3:
            day = 'Wednesday'
        elif day == 4:
            day = 'Thursday'
        elif day == 5:
            day = 'Friday'
        elif day == 6:
            day = 'Saturday'
        elif day == 7:
            day = 'Sunday'

        with open('records.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([tips, hours, day, hourly])
        self.entry_tips.delete(0, END)
        self.entry_hours.delete(0, END)
        self.date_button.set(None)