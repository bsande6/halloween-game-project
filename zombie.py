import random
import abc

""" Contains class implementations for Zombie Types"""

class Zombie():
    __inplay = True
    
    def __init__(self, canvas):
        self.x = 0
        self.y = 0
        
        # maybe set static variable for max number of zombies allowed on board

        # should not have to resave this for each new zombie
        # maybe make static and only pass once somehow
        self.canvas = canvas
        self.width = int(self.canvas.cget("width"))
        self.height = int(self.canvas.cget("height"))
       
    
    @abc.abstractmethod
    def draw(self):
        """draw each type of zombie slightly differently"""
        pass

    @abc.abstractmethod
    def movement(self):
        """implements different movement patterns for different zombie types"""
        pass
    
    def getCanvas():
        return self.canvas

    @staticmethod
    def getInPlay():
        return Zombie.__inplay

    @staticmethod
    def setInPlay(inplay):
        
        # this needs to change inplay for all instances 
        Zombie.__inplay = inplay

    

class BasicZombie(Zombie):
    def __init__(self):
        self.max_speed = 5
    
    def draw(self):
        # spawn in random positon, adjust size slightly
        self.circle = self.canvas.create_oval(
                         250, 250, 200, 200, fill = "gray")
    def movement(self):
        # needs to follow user
        pass
    
class LargeZombie(Zombie):
     def __init__(self):
        self.max_speed = 3

     def draw(self):
        # make larger and slower than other zombies
        # spawn in random positon, adjust size slightly
        self.circle = self.canvas.create_oval(
                         250, 250, 200, 200, fill = "gray")


        
class RunningZombie(Zombie):
    def __init__(self):
        self.max_speed = 7

    def draw(self):
        self.circle = self.canvas.create_oval(
                         250, 250, 200, 200, fill = "purple")
    
    def movement(self):
        # needs to follow user positions
        pass

class RandomZombie(Zombie):
    def __init__(self, canvas):
        super(RandomZombie, self).__init__(canvas)
        self.max_speed = 5
        self.xbias = random.randint(-1, 1)
        self.ybias = random.randint(-1, 1)
        self.resetBias = False
        
    
    def draw(self):
        # spawn in random position??
        self.circle = self.canvas.create_oval(
                         250, 250, 200, 200, fill = "brown")

    def movement(self):
        if Zombie.getInPlay():
            self.x = random.randint(-1*self.max_speed, self.max_speed)
            self.y = random.randint(-1*self.max_speed, self.max_speed)

            if random.randint(1,4) < 4: # adding movement bias to make zombies better
                self.x = self.xbias * self.max_speed
                self.y = self.ybias * self.max_speed
            #print( "self x: " + str(self.x) + " self y: " + str(self.y))
            coords = self.canvas.coords(self.circle)
            if coords[0] < 10 and self.x < 0:
                self.x = 0
                self.resetBias = True
            elif coords[0] > (self.width - 30) and self.x > 0:
                self.x = 0
                self.resetBias = True
            if coords[1] < 10 and self.y < 0:
                self.y =0
                self.resetBias = True
            elif coords[1] > (self.height - 30) and self.y > 0:
                self.y = 0
                self.resetBias = True

            if self.resetBias:
                self.xbias = random.randint(-1, 1)
                self.ybias = random.randint(-1, 1)
                self.resetBias = False
                print("resetting bias")

            # either return x and y or pass in canvas during init 
            self.canvas.move(self.circle, self.x, self.y)
            # new random input
            self.canvas.after(100, self.movement)

        
