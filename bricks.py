from drawable import drawable
class brick(drawable):
    def __init__(self, y, x):
        super().__init__(y,x)


class bricklvl1(brick):
    def __init__(self, y, x):
        self.lvl = 0
        super().__init__(y,x)



class bricklvl2(brick):
    def __init__(self, y, x):
        self.lvl = 1
        super().__init__(y,x)


class bricklvl3(brick):
    def __init__(self, y, x):
        self.lvl = 2
        super().__init__(y,x)


class brickfixed(brick):
    def __init__(self,y,x):
        self.lvl = 4
        super().__init__(y,x)

class brickExp(brick):
    def __init__(self,y,x):
        self.lvl = 69
        super().__init__(y,x)
