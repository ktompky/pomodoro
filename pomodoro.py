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
    print('Time for a break!\n')

def shortBreak(t):
    t = t * 60
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Time to go back to work!\n')

# def longBreak(t):
#     t = t * 60
#     while t:
#         mins, secs = divmod(t, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         print(timeformat, end='\r')
#         time.sleep(1)
#         t -= 1
#     print('Time for a break!\n\n\n\n\n')

# def gameBreak(t):
#     t = t * 60
#     while t:
#         mins, secs = divmod(t, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         print(timeformat, end='\r')
#         time.sleep(1)
#         t -= 1
#     print('Time for a break!\n\n\n\n\n')
start_cycle = 1 
print("Welcome to the kitty cat pomodoro!\n\nHow long do you want to work? You will pick the number of cycles you want.")
print("A cycle is 30 minutes: A 25 block of work time and a 5 minute block of break time.")

end_cycle = int(input("How many cycles do you want? "))


def cycle(start_cycle, end_cycle):
    workCountdown(25)
    shortBreak(5)
    if start_cycle < end_cycle:
        start_cycle += 1
        cycle(start_cycle,end_cycle)
    else:
        print(start_cycle)
        print("Your work is finished!")

cycle(start_cycle,end_cycle)