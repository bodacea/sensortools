#!/usr/bin/env python

# Copyright (c) 2011 Bastian Venthur
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


"""Dance program for the AR Drone 
"""

import pygame
import libardrone
from time import sleep

#Throw some moves

def dad_sideside(drone):
    return

def funk_leftright(drone):
    print "my funky leftright"
    drone.speed = 0.2
    for i in range(1, 10): 
        drone.move_left()
        sleep(0.1)
    drone.hover()
    for i in range(1, 10): 
        drone.move_right()
        sleep(0.1)
    drone.hover()
    return

def formal_waltz(drone):
    print "my waltz move"
    drone.speed = 0.2
    for i in range(1, 10): 
        drone.move_forward()
        sleep(0.1)
    drone.hover()
    for i in range(1, 10): 
        drone.move_right()
        sleep(0.1)
    drone.hover()
    for i in range(1, 10): 
        drone.move_left()
        sleep(0.1)
    drone.hover()
    for i in range(1, 10): 
        drone.move_backward()
        sleep(0.1)
        drone.hover()
    return


def main():
    #pygame.init()
    #W, H = 320, 240
    #screen = pygame.display.set_mode((W, H))

    drone = libardrone.ARDrone()
    drone.takeoff()
    drone.hover()

    print "Make the ardrone dance!"    
    running = True
    while running:
        dance = raw_input("type waltz, boogie or quit> ")
        
        if dance == "boogie":
            print "boogying"
            funk_leftright(drone)

        elif dance == "waltz":
            print "waltzing"
            formal_waltz(drone)

        elif dance == "quit":
            print "quitting"
            running = False

        sleep(10)

    print "Shutting down...",
    drone.halt()
    print "Ok."

if __name__ == '__main__':
    main()

