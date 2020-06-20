import time
import datetime

# def workTime():
#     on_minutes = 25 * 60
#     ##Let's use a ranged loop to create the counter
#     for i in range(on_minutes):
#         print(str(datetime.timedelta(on_minutes-i)) + " seconds remaining \n")
#     ##we also need the loop to wait for 1 second between each iteration
#         t.sleep(1)

#     print("Time is up")


# workTime()




def countdown(t):
    t = t * 60 
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Goodbye!\n\n\n\n\n')

countdown(25)