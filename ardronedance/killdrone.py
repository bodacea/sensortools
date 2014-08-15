import libardrone
from time import sleep

drone= libardrone.ARDrone()

drone.land()
sleep(5)
#drone.reset()
drone.halt()

