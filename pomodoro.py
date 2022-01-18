import time
from plyer import notification

count = 0
print("The pomodoro timer has started, start working.")



if __name__ == "__main__":
    while True:
        time.sleep(1800)
        count += 1
        notification.notify(
            title = "Good Work, minion.",
            message = "Please actually take a 10 min break. You've completed " + str(count) + "pomodoros so far.",
        )
        time.sleep(600)
        notification.notify(
            title = "Back to work, peon.",
            message = "Try doing another pomodoro.",
        )

