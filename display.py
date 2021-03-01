import colorama
import numpy
import bricks
import slider
import sys
import ball
import collision
import global_vars as gb


class display:
    def __init__(self):
        # gb.display = [[-1]*122]*36
        gb.display = numpy.array(gb.display)
        self.length = 0

    def createlvl(self, bricks):
        for brick in bricks:
            x = 0
            while x < 4:
                gb.display[brick.Ycor][brick.Xcor+x] = brick.lvl
                x += 1

    def createPowerUP(self, powerUp, set):

        if powerUp.Ycor < 32:
            gb.display[powerUp.Ycor+3][powerUp.Xcor] = powerUp.powerupNum
            gb.display[powerUp.Ycor+1][powerUp.Xcor] = -1
            print(gb.display[powerUp.Ycor][powerUp.Xcor], "pu below")
            if gb.display[powerUp.Ycor+5][powerUp.Xcor] == 2019111026:
                collision1 = collision.collision()
                collision1.puwithpadle(powerUp, set)
        elif powerUp.Ycor < 34:
            gb.display[powerUp.Ycor][powerUp.Xcor] = -1
            gb.display[powerUp.Ycor+1][powerUp.Xcor] = -1

    def updateSlider(self, slider):
        # print(slider,"display")
        self.length = slider.slider_length
        # print(self.length, slider.slider_length, "len")
        if slider.Xcor > 0 and slider.Xcor < 114:
            x = 0
            while x < slider.slider_length:
                gb.display[slider.Ycor][slider.Xcor+x] = 2019111026
                x += 1
            for a in range(0, slider.Xcor):
                gb.display[slider.Ycor][a] = -1
            for b in range(slider.Xcor+slider.slider_length, 122):
                gb.display[slider.Ycor][b] = -1

    def dropPowerUP(self, powerups, set):
        for powerup in powerups:
            powerup = powerup.dpp()
            self.createPowerUP(powerup, set)
        return powerups

    def updateBall(self, set, ball, Yspeed, Xspeed):
        col = True
        if ball.Xcor-1 <= 0:
            collision1 = collision.collision()
            collision1.withLeft(ball.Ycor, ball.Xcor)
        elif ball.Xcor+Xspeed >= 122:
            collision1 = collision.collision()
            collision1.withRight(ball.Ycor, ball.Xcor)
        elif ball.Ycor-1 == 0:
            collision1 = collision.collision()
            collision1.withTop(ball.Ycor, ball.Xcor)
        elif ball.Ycor+1 > 35:
            gb.display[34] = -1
            gb.lives -= 1
            ball.updateYX(set.slider.Ycor-1, set.slider.Xcor+3)
            gb.Xspeed = 0
            gb.Yspeed = -1
            gb.motionUp = True
            gb.grab = True
            gb.thru = False
            gb.motionRight = True
            if gb.lives < 0:
                print("Game Over")
                sys.exit(0)
        else:
            if gb.motionUp and col:
                if gb.display[ball.Ycor-1][ball.Xcor] != -1 and ( gb.display[ball.Ycor-1][ball.Xcor] != 12301 or gb.display[ball.Ycor-1][ball.Xcor] != 12302 or gb.display[ball.Ycor-1][ball.Xcor] != 12303 or gb.display[ball.Ycor-1][ball.Xcor] != 12304 or gb.display[ball.Ycor-1][ball.Xcor] != 12305 or gb.display[ball.Ycor-1][ball.Xcor] != 12306):
                    collision1 = collision.collision()
                    col = False
                    collision1.withTop(ball.Ycor-1, ball.Xcor)

            elif not(gb.motionUp) and col:
                print(ball.Xcor, ball.Ycor, "debug")
                if gb.display[ball.Ycor+1][ball.Xcor] != -1 and (gb.display[ball.Ycor+1][ball.Xcor] != 12301 or gb.display[ball.Ycor+1][ball.Xcor] != 12302 or gb.display[ball.Ycor+1][ball.Xcor] != 12303 or gb.display[ball.Ycor+1][ball.Xcor] != 12304 or gb.display[ball.Ycor+1][ball.Xcor] != 12305 or gb.display[ball.Ycor+1][ball.Xcor] != 12306):
                    collision1 = collision.collision()
                    col = False
                    collision1.withBottom(ball.Ycor+1, ball.Xcor)

            if gb.motionRight and col:
                if gb.display[ball.Ycor][ball.Xcor+1] != -1 and gb.display[ball.Ycor][ball.Xcor+1] != 2019111026 and (  gb.display[ball.Ycor][ball.Xcor+1] != 12301 or gb.display[ball.Ycor][ball.Xcor+1] != 12302 or gb.display[ball.Ycor][ball.Xcor+1] != 12303 or gb.display[ball.Ycor][ball.Xcor+1] != 12304 or gb.display[ball.Ycor][ball.Xcor+1] != 12305 or gb.display[ball.Ycor][ball.Xcor+1] != 12306):
                    collision1 = collision.collision()
                    col = False
                    collision1.withRight(ball.Ycor, ball.Xcor+1)

            elif not(gb.motionRight) and col:
                if gb.display[ball.Ycor][ball.Xcor-1] != -1 and gb.display[ball.Ycor][ball.Xcor-1] != 2019111026:
                    collision1 = collision.collision()
                    col = False
                    collision1.withLeft(ball.Ycor, ball.Xcor-1)

            if gb.motionUp and gb.motionRight and col:
                if gb.display[ball.Ycor-1][ball.Xcor+1] != -1:
                    collision1 = collision.collision()
                    col = False
                    collision1.withTopRight(ball.Ycor-1, ball.Xcor+1)

            elif not(gb.motionUp) and not(gb.motionRight) and col:
                if gb.display[ball.Ycor+1][ball.Xcor-1] != -1 and gb.display[ball.Ycor+1][ball.Xcor-1] != 2019111026:
                    collision1 = collision.collision()
                    col = False
                    collision1.withBottomLeft(ball.Ycor+1, ball.Xcor-1)

            elif not(gb.motionRight) and gb.motionUp and col:
                if gb.display[ball.Ycor-1][ball.Xcor-1] != -1:
                    collision1 = collision.collision()
                    col = False
                    collision1.withTopLeft(ball.Ycor-1, ball.Xcor-1)

            elif gb.motionRight and not(gb.motionUp) and col:
                if gb.display[ball.Ycor+1][ball.Xcor+1] != -1 and gb.display[ball.Ycor+1][ball.Xcor+1] != 2019111026:
                    collision1 = collision.collision()
                    col = False
                    collision1.withBottomRight(ball.Ycor+1, ball.Xcor+1)

        # if gb.display[ball.Ycor - Yspeed][ball.Xcor -Xspeed] != 123 and gb.display[ball.Ycor + Yspeed][ball.Xcor +Xspeed] != 123:
            # gb.display[ball.Ycor][ball.Xcor] = 8011
        # else:
        gb.display[ball.Ycor - Yspeed][ball.Xcor - Xspeed] = -1
        gb.display[ball.Ycor][ball.Xcor] = 8011

    def renderDisplay(self):
        isBrick = False    
        print("                                  Lives: ",gb.lives,"          Score: ",gb.score,"          Time: ",gb.time)
        for y in range(0, 36):
            x = 0
            print("|", end='')
            while x < 122:
                if gb.display[y][x] == -1:
                    print(' ', end='')
                    x += 1
                elif gb.display[y][x] == 2019111026:
                    a = 0
                    while a < self.length:
                        print(colorama.Back.LIGHTWHITE_EX+' ', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        x += 1
                        a += 1
                elif gb.display[y][x] == 8011:
                    if gb.thru:
                        print(colorama.Fore.LIGHTRED_EX+'\u2B24', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        x += 1
                    else:
                        print(colorama.Fore.LIGHTCYAN_EX+'\u2B24', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        x += 1
                elif gb.display[y][x] == 12305:
                    print('\U0001F525', end='')
                    print(colorama.Style.RESET_ALL, end='')
                    x += 2
                elif gb.display[y][x] == 12302:
                    print('\U00002195 	', end='')
                    print(colorama.Style.RESET_ALL, end='')
                    x += 2
                elif gb.display[y][x] == 12301:
                    print('\U00002194', end='')
                    print(colorama.Style.RESET_ALL, end='')
                    x += 2
                elif gb.display[y][x] == 12304:
                    print('↯', end='')
                    print(colorama.Style.RESET_ALL, end='')
                    x += 2
                elif gb.display[y][x] == 12306:
                    print('✋', end='')
                    print(colorama.Style.RESET_ALL, end='')
                    x += 2
                else:
                    
                    if gb.display[y][x] == 0:
                        isBrick = True
                        print(colorama.Back.YELLOW+'____', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        print(' ', end='')
                    elif gb.display[y][x] == 1:
                        isBrick = True
                        print(colorama.Back.RED+'____', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        print(' ', end='')
                    elif gb.display[y][x] == 2:
                        isBrick = True
                        print(colorama.Back.BLUE+'____', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        print(' ', end='')
                    elif gb.display[y][x] == 4:
                        print(colorama.Back.MAGENTA+'____', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        print(' ', end='')
                    elif gb.display[y][x] == 69:
                        isBrick = True
                        print(colorama.Back.LIGHTGREEN_EX+'____', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        print(' ', end='')
                    
                    print(colorama.Style.RESET_ALL, end='')
                    x += 5
                # print(x)
            print('|\n', end='')

        if not(isBrick):
            print("Winner Winnner Chicken Dinner!!!")