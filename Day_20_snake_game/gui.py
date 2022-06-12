import tkinter as tk
from tkinter import messagebox
import calendar
from datetime import datetime, date, time, timedelta
import math

today = date.today()
data = date.today
data = 1

def getNextDay():
    #today = today + timedelta(days=1)
    messagebox.showinfo('Message', 'You clicked the next button!')


#Root
root = tk.Tk()
root.title("Calendar")
root.geometry("600x600")
root.iconphoto(False, tk.PhotoImage(file='C:\\Users\\Simão\\Downloads\\Calendar-Logo-Transparent-File.png'))
root.configure(bg='black')

for i in range(3):
    root.columnconfigure(i,weight=1)
    root.rowconfigure(i,weight=1)

#Menu
menubar = tk.Menu(root)
#Menu file dropdown
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save as...")
filemenu.add_command(label="Close" )
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
#Menu edit dropdown
helpmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...")
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
    
#Containers
container1 = tk.Frame(root, bg="black")
container2 = tk.Frame(root,bg="black")
container3 = tk.Frame(root)
container1.grid(row=0, column=1)
container2.grid(row=1, column=1, sticky=tk.N)
container3.grid(row=2, column=1, sticky=tk.N)

#Next and previous button
previous = tk.Button(container1, text="<--",bg="gold", fg="red",font=('Helvatical bold',10))
previous.grid(row=0, column=1, padx=5)
text = tk.Label(container1, text=today.strftime('%A, %B %d, %Y'), bg="black", fg="gold", font=('Helvatical bold',20))
text.grid(row=0, column=2)
next_bttn = tk.Button(container1, text="-->",bg="gold", fg="green",font=('Helvatical bold',10), command=getNextDay)
next_bttn.grid(row=0, column=3, padx=5)

now = datetime.now()
month_days = calendar.monthrange(now.year, now.month)[1]
row_number = math.ceil(month_days/7)


i = 1
for r in range(row_number):
   for c in range(7):
        tk.Button(container2, text=i,
        borderwidth=1,bg="gold", fg="brown", width=5).grid(row=r,column=c,)
        i = i + 1
        if i > month_days:
            break

print("now", now)
print("number of days in month",calendar.monthrange(now.year, now.month)[1])


var = tk.StringVar()
label = tk.Label( container3, textvariable=var, relief=tk.RAISED,padx=10,pady=10, bg="gold", fg="brown")
var.set("Today: " + str(today))
label.grid(row=10, column=0, sticky=tk.N, )



#Function



root.config(menu=menubar)
root.mainloop()