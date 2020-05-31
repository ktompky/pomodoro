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









 