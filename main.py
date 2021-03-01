import setup
import signal
import sys
import time
import bricks
import os
import display
import slider
import ball
import collision
from alarmexception import *
from getchunix import *
import global_vars as gb

start_time = time.time()

getch = GetchUnix()

def endpu(set):
    timeout = 30
    if int(gb.time) > int(gb.expandtime) + timeout:
        for powerup in gb.actpowerup:
            if powerup.powerupNum == 12301:
                powerup.endup(set)
    if int(gb.time) > int(gb.shrinktime) + timeout:
        for powerup in gb.actpowerup:
            if powerup.powerupNum == 12302:
                powerup.endup(set)
    if int(gb.time) > int(gb.thrutime) + timeout:
        for powerup in gb.actpowerup:
            if powerup.powerupNum == 12305:
                powerup.endup(set)
    if int(gb.time) > int(gb.fasttime) + timeout:
        for powerup in gb.actpowerup:
            if powerup.powerupNum == 12304:
                powerup.endup(set)

def alarmHandler(signum, frame):
    raise AlarmException


def input_to(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    # signal.alarm(timeout)
    signal.setitimer(signal.ITIMER_REAL, gb.timeout)
    try:
        text = getch()
        signal.alarm(0)
        signal.setitimer(signal.ITIMER_REAL, 0.2)
        return text
    except AlarmException:
        signal.setitimer(signal.ITIMER_REAL, 0.2)
        # print("\n Prompt timeout. Continuing...")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ""


set = setup.setup()
set.createlvl1()
slider_x = 57
slider_y = 35


while True:
    os.system('clear')
    set.display1.renderDisplay()
    a=2
    while a:
        a-=1
        c = input_to()
        if c == "q":
            # print("your score is", score)
            print("END")
            sys.exit(0)
        elif c == "d":
            if slider_x <= 114:
                slider_x += 1
                set.slider.moveSlider(1)
                if gb.grab == True:
                    set.display1.updateBall(set, set.ball1, 0, 1)
                    set.ball1.updateYX(set.ball1.Ycor, set.ball1.Xcor+1)

            set.display1.updateSlider(set.slider)
            # block.moveRight(sc, bl)
        elif c == ' ':
            gb.grab = False
            gb.display[34] = -1

        elif c == "a":
            if slider_x >= 0:
                slider_x -= 1
                set.slider.moveSlider(-1)
                if gb.grab == True:
                    set.display1.updateBall(set, set.ball1, 0, -1)
                    set.ball1.updateYX(set.ball1.Ycor, set.ball1.Xcor-1)

            set.display1.updateSlider(set.slider)
            # block.moveLeft(sc, bl)
        if c:
            time.sleep(.05)
        

    gb.powerup = set.display1.dropPowerUP(gb.powerup, set)
    if not(gb.grab):
        set.ball1.updateYX(set.ball1.Ycor+gb.Yspeed, set.ball1.Xcor+gb.Xspeed)
        set.display1.updateBall(set, set.ball1, gb.Yspeed, gb.Xspeed)
    gb.time = (time.time() - start_time)//1
    gb.tempsliderlen = set.slider.slider_length
    endpu(set)

