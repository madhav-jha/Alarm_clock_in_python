from time import sleep
from datetime import datetime
import winsound


def set_alarm():
    min = int(input("Enter number of minutes to set the alarm: "))

    t = datetime.now()
    print("Current time: ", t.strftime('%m/%d/%y %H:%M'))

    sec = min * 60

    if min >= 0:
        print("Alarm will ring after " + str(min) + ' minute(s)')
        sleep(sec)
        print("Get up!")
        winsound.Beep(1500, 5000)

    else:
        print("Please enter valid value!")


set_alarm()



