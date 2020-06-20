import time
import datetime


def workCountdown(t):
    t = t * 60 
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Time for a break!\n\n\n\n\n')

def shortBreak(t):
    t = t * 60
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Time for a break!\n\n\n\n\n')

def longBreak(t):
    t = t * 60
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Time for a break!\n\n\n\n\n')

def gameBreak(t):
    t = t * 60
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Time for a break!\n\n\n\n\n')


workCountdown(25)
shortBreak(5)
longBreak(15)
gameBreak(60)