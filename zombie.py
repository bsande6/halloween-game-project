""" Contains class implementations for Zombie Types"""

class BasicZombie():
    def __init__(self):
        # spawn in random position??
        self.x_pos=0
        self.y_pos=0
        # maybe use these for movement
        self.x_vel=0
        self.y_vel=0
        self.speed = 5
    
        # self.rectangle = self.canvas.create_rectangle(
        #                  5, 5, 25, 25, fill = "tan")
        
    
class RunningZombie():
    def __init__(self):
        # spawn in random position??
        self.x_pos=0
        self.y_pos=0
        # maybe use these for movement
        self.x_vel=0
        self.y_vel=0
        self.speed = 10

class RandomZombie():
    def __init__(self):
        # spawn in random position??
        self.x=0
        self.y=0
        # maybe use these for movement
        self.x_vel=0
        self.y_vel=0
        self.speed = 10
        self.movement()

    def movement(self):
        self.x = rand.randint(0, 5)
        self.y = rand.randint(0, 5)
        # coords = self.canvas.coords(self.rectangle)
        # if coords[0] < 10 and self.x < 0:
        #     self.x = 0
        # elif coords[0] > (self.width - 30) and self.x > 0:
        #     self.x = 0
        # if coords[1] < 10 and self.y < 0:
        #     self.y =0
        # elif coords[1] > (self.height - 30) and self.y > 0:
        #     self.y = 0

        # either return x and y or pass in canvas during init 
        # self.canvas.move(self.rectangle, self.x, self.y)
 
        # self.canvas.after(1000, self.movement)
    
