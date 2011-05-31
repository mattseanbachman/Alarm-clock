import subprocess
import time
import os

not_executed = 1

i_hour = int(input("Hour?\n"))
i_minute = int(input("Minute?\n"))
ap = input("AM or PM?\n")
if ap == "PM":
	i_hour += 12


while(not_executed):
	dt = list(time.localtime())
	hour = dt[3]
	minute = dt[4]
	if hour == i_hour and minute == i_minute:
		subprocess.Popen("vlc ./v.mp3", shell=True)
		not_executed = 0
	time.sleep(30)

