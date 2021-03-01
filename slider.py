from drawable import drawable
class slider(drawable):
    def __init__(self, y, x):
        self.slider_length = 7
        super().__init__(y,x)
    def updateLength(self, length):
        self.slider_length = length
    def moveSlider(self,x):
        self.Xcor +=x