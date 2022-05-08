## Requirements
### Needs both time and the plyer module to notify the user once a cycle has completed.
#
### python3 -m pip install plyer
#
#
### snagged from here - https://dev.to/code_jedi/create-a-simple-pomodoro-timer-in-python-l97
#
### This verson laid out in pomodoro.py is basic, but gets the job done.  When you run the code, it starts the pomodoro work section of the timer. Once that's complete, it will give you a break and then go back into the work cycle. Each time it completes that cycle of work and break, the count increased by 1. 
#
### There is no way to pause the timer nor is there a way to stop the timer beyond ctrl + c to interrupt the while loop.
#
### Future ways I would like to customize this code for my own use-
- Change the work and break sleep timer to keep default times but accept user input of different work and break timers.
- Change the messaging for the pomodoro start, the break start, and the work end.
- Change the code to set a specific number of work cycles. This would be great if there's a specific time that you have to work. Or to set a goal to work a specific number of cycles.
- Creat a flask project for pomodoro that uses docker image so that anyone can run this


