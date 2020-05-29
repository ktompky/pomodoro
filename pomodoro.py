import time

#display the programs instructions

print("Press enter to begin. Then press enter again to click the stopwatch. Press ctrl-c to quit.")


input() #this is when you would press enter to begin

print('Started')

startTime = time.time() #get first laps start time
lastTime = startTime
lapNum = 1
#need to track lap times