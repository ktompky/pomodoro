import time
import datetime as dt

import tkinter
from tkinter import messagebox
import winsound

#current time
t_now  = dt.datetime.now()
#pomodoro time
t_pom = 25*60
#time delta in mins
t_delta = dt.timedelta(0,t_pom)
#ending pomodoro
t_fut = t_now + t_delta
#break time
delta_sec = 5*60
#ya final time.
t_fin = t_now + dt.timedelta(0,t_pom+t_delta)

#hides the main window for tkinter, only shows alert message box
root = tkinter.Tk()
root.withdraw 
#alert message
messagebox.showinfo("Pomodoro Started!", "\nIt is now " + t_now.strftime("%H:%M") +
" hrs \nTimer set for 25 mins.")

#initialize counters
total_pomodoros = 0
breaks = 0

while True:
    if t_now < t_fut:
        print('pomodoro')
    elif t_fut <= t_now <= t_fin:
        print('in break')
        if breaks ==0:
            print('if break')
            for i in range(5):
                winsound.Beep((i+100), 700)
            print('Break time!')
            breaks+= 1









 