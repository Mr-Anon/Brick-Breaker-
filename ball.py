class ball:
    def __init__(self, y, x):
        self.Xcor = x
        self.Ycor = y
        
    def updateYX(self, y, x):
        # print(self.Xcor,self.Ycor,"Ayush")
        self.Xcor = x
        self.Ycor = y
        # print(self.Ycor,self.Xcor,y,x,"updateXY")