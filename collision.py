import global_vars as gb
import ball
import powerUps
import random
import display
import powerUps


class collision:

    def brickLvlDown(self, y, x):
        if gb.display[y][x] == 4:
            if gb.exp or gb.thru:
                gb.score +=1
                og_lvl = gb.display[y][x]
            
                x1 = 0
                while x1 < 4:
                    if gb.display[y][x+x1] == og_lvl:
                        gb.display[y][x+x1] = -1
                    else:
                        x2 = 1
                        while x2 < 4:
                            if gb.display[y][x-x2] == og_lvl:
                                gb.display[y][x-x2] = -1
                            else:
                                break

                            # print(gb.display[y][x-x2], x2)
                            x2 += 1
                        break

                    # print(gb.display[y][x+x1], x1)
                    x1 += 1

        if gb.display[y][x] in range(0, 3):
            gb.score +=1
            og_lvl = gb.display[y][x]
            if not(gb.exp) and not(gb.thru):
                x1 = 0
                while x1 < 4:
                    if gb.display[y][x+x1] == og_lvl:
                        gb.display[y][x+x1] -= 1
                    else:
                        x2 = 1
                        while x2 < 4:
                            if gb.display[y][x-x2] == og_lvl:
                                gb.display[y][x-x2] -= 1
                            else:
                                break

                            # print(gb.display[y][x-x2], x2)
                            x2 += 1
                        break

                    # print(gb.display[y][x+x1], x1)
                    x1 += 1
            else:
                x1 = 0
                while x1 < 4:
                    if gb.display[y][x+x1] == og_lvl:
                        gb.display[y][x+x1] = -1
                    else:
                        x2 = 1
                        while x2 < 4:
                            if gb.display[y][x-x2] == og_lvl:
                                gb.display[y][x-x2] = -1
                            else:
                                break

                            # print(gb.display[y][x-x2], x2)
                            x2 += 1
                        break

                    # print(gb.display[y][x+x1], x1)
                    x1 += 1

            if og_lvl == 0 or gb.exp or gb.thru:    
                a = random.randint(1, 10)
                if a < 5:
                    # print("drop powerUp")
                    gb.no_of_powerups += 1
                    pp = random.randint(1,5)
                    if pp == 1:
                        self.powerup = powerUps.powerupExpandPaddle(y, x)
                    if pp == 2:
                        self.powerup = powerUps.powerupShrinkPaddle(y, x)
                    if pp == 3:
                        self.powerup = powerUps.powerupThruball(y, x)
                    if pp == 4:
                        self.powerup = powerUps.powerupFastBall(y, x)
                    if pp == 5:
                        self.powerup = powerUps.powerupPaddlegrab(y, x)
                    if pp == 6:
                        self.powerup = powerUps.powerupBallMultiplier(y, x)
                    # self.createPowerUP(self.powerup)
                    gb.powerup.append(self.powerup)
        elif gb.display[y][x] == 69:
            gb.exp = True
            gb.score +=1
            og_lvl = gb.display[y][x]
            x1 = 0
            while x1 < 4:
                if gb.display[y][x+x1] == og_lvl:
                    gb.display[y][x+x1] = -1
                else:
                    x2 = 1
                    while x2 < 4:
                        if gb.display[y][x-x2] == og_lvl:
                            gb.display[y][x-x2] = -1
                        else:
                            break

                        # print(gb.display[y][x-x2], x2)
                        x2 += 1
                    break

                # print(gb.display[y][x+x1], x1)
                x1 += 1
            self.brickLvlDown(y,x+5)
            self.brickLvlDown(y,x-5)
            self.brickLvlDown(y+1,x+5)
            self.brickLvlDown(y+1,x-5)
            self.brickLvlDown(y-1,x+5)
            self.brickLvlDown(y-1,x-5)
            self.brickLvlDown(y+1,x)
            self.brickLvlDown(y-1,x)
        



    def ballSpeedChangeOn(self, y, x):
        if gb.display[y][x] == 2019111026:
            x1 = 0
            countF = 0
            countB = 0
            while x1 < gb.tempsliderlen:
                if gb.display[y][x+x1] == 2019111026:
                    countF += 1
                else:
                    x2 = 1
                    while x2 < gb.tempsliderlen:
                        if gb.display[y][x-x2] == 2019111026:
                            countB += 1
                        else:
                            break
                        x2 += 1
                    break
                x1 += 1
            # print(countF, countB)
            if countF == int(gb.tempsliderlen/2) +1:
                gb.Xspeed = 0
            elif countF > countB:
                gb.Xspeed = int(gb.tempsliderlen/2) +1 - countF
                gb.motionRight = False
            elif countB > countF:
                gb.Xspeed = countB - int(gb.tempsliderlen/2) 
                gb.motionRight = True
        if gb.pugrab:
            gb.grab = True

    def withTop(self, y, x):
        if not(gb.thru) or y == 1:
            gb.Yspeed -= gb.Yspeed*2
            print("collison top", gb.display[y][x])
            gb.motionUp = False
            gb.exp = False
            self.brickLvlDown(y, x)
        else:
            self.brickLvlDown(y, x)
            gb.score += 2

    def withBottom(self, y, x):
        if not(gb.thru) or y == 35:
            gb.Yspeed -= gb.Yspeed*2
            print("collison bottom")
            gb.motionUp = True
            gb.exp = False
            self.brickLvlDown(y, x)
            self.ballSpeedChangeOn(y, x)
        else:
            self.brickLvlDown(y, x)
            gb.score +=2

    def withRight(self, y, x):
        if not(gb.thru) or  x >= 121:
            gb.Xspeed -= gb.Xspeed*2
            print("collison right")
            gb.motionRight = False
            gb.exp = False
            self.brickLvlDown(y, x)
        else:
            self.brickLvlDown(y, x)
            gb.score +=2

    def withLeft(self, y, x):
        if not(gb.thru) or x <= 1:
            gb.Xspeed -= gb.Xspeed*2
            print("collison left")
            gb.motionRight = True
            gb.exp = False
            self.brickLvlDown(y, x)
        else:
            self.brickLvlDown(y, x)
            gb.score +=2

    def withTopRight(self, y, x):
        if not(gb.thru):   
            gb.Xspeed -= gb.Xspeed*2
            gb.Yspeed -= gb.Yspeed*2
            print("collison top right")
            gb.motionUp = False
            gb.motionRight = False
            gb.exp = False
            self.brickLvlDown(y, x)
        else:
            self.brickLvlDown(y, x)
            gb.score +=2

    def withTopLeft(self, y, x):
        if not(gb.thru):
            gb.Xspeed -= gb.Xspeed*2
            gb.Yspeed -= gb.Yspeed*2
            print("collison top left")
            gb.motionUp = False
            gb.motionRight = True
            gb.exp = False
            self.brickLvlDown(y, x)
        else:
            self.brickLvlDown(y, x)
            gb.score +=2

    def withBottomRight(self, y, x):
        if not(gb.thru):
            gb.Xspeed -= gb.Xspeed*2
            gb.Yspeed -= gb.Yspeed*2
            print("collison bottom right")
            gb.motionUp = True
            gb.motionRight = False
            gb.exp = False
            self.brickLvlDown(y, x)
        else:
            self.brickLvlDown(y, x)
            gb.score +=2

    def withBottomLeft(self, y, x):
        if not(gb.thru):
            gb.Xspeed -= gb.Xspeed*2
            gb.Yspeed -= gb.Yspeed*2
            print("collison bottom left")
            gb.motionUp = True
            gb.motionRight = True
            gb.exp = False
            self.brickLvlDown(y, x)
        else:
            self.brickLvlDown(y, x)
            gb.score +=2

    def puwithpadle(self,pu, set):
        
        pu.startpu(set)
        gb.actpowerup.append(pu)
        print("pu caught")
