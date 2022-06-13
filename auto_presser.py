from cgi import test
from msilib import text
import tkinter as tk
from tkinter import scrolledtext
import keyboard
import time
from datetime import datetime
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Never_Away")
        self.root.geometry("600x600")
        self.root['bg'] = "black"
        #self.root.iconphoto(False, tk.PhotoImage(file='C:\\Users\\bonva\\Desktop\\Projects\\keyboard_automatic_presser\\icons8-active-64.png'))
        self.root.protocol("WM_DELETE_WINDOW", self.root.iconify)
        self.mainMenu()
        self.time_in_minutes = 0
        self.root.mainloop()

    def mainMenu(self):
        var = tk.StringVar()
        var.set("Keeping your computer active...")
        self.label = tk.Label(master=self.root, textvariable=var, fg="gold", bg="black", font=("Arial", 16)).place(x=190, y=255)
        self.button = tk.Button(master=self.root, text="Set Timer", command=self.setTimer, bg="gold", font=("Comic Sans MS", 8)).place(x=265
        , y=295)
        self.button = tk.Button(master=self.root, text="Exit", command=self.root.destroy, bg="gold", font=("Comic Sans MS", 8)).place(x=330, y=295)
        self.textField = scrolledtext.ScrolledText(self.root, height=15, width=62)
        self.textField.place(x=55, y=10)
        

    def setTimer(self):
        self.textField.delete("1.0",tk.END)
        self.windowConfirmTime = tk.Toplevel()
        self.windowConfirmTime.geometry("475x250")
        self.windowConfirmTime['bg'] = "black"
        timeLabel = tk.Label(master=self.windowConfirmTime,fg="gold", bg="black", text="How long do you want to stay active (minutes)?", font=("Arial", 16))
        timeLabel.place(x=15, y=100)
        self.timeInput = tk.Entry(master=self.windowConfirmTime)
        self.timeInput.place(x=180, y=145)
        timeStartButton = tk.Button(master=self.windowConfirmTime, text="Start", bg="gold", fg="black", command=self.startTimer)
        timeStartButton.place(x=225, y=170)


    def update_text(self):
        minute = "minute" if self.time_in_minutes == 1 else "minutes"
        current_time = self.get_current_time()
        self.textField.insert(tk.END, f"Active for {self.time_in_minutes} {minute} {current_time}.\n")
        keyboard.press('f15')
        if int(self.time_in_minutes) == int(self.selectedTime):
            self.textField.insert(tk.END, "Program over.")
            return
        self.time_in_minutes += 1
        self.root.after(60000, self.update_text)

    def get_current_time(self):
        self.time = datetime.now()
        self.time.strftime("%H:%M:%S")
        return self.time

    def startTimer(self):
        self.selectedTime = self.timeInput.get()
        self.windowConfirmTime.destroy()
        self.textField.focus()
        self.textField.insert(tk.END, "Program Start...\n")
        self.update_text()

App()