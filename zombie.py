import random
import abc
from PIL import Image, ImageTk
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
        self.framecounter = 0
       
    
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
    def __init__(self, canvas):
        super(LargeZombie, self).__init__(canvas)
        self.max_speed = 1
        self.xbias = random.randint(-1, 1)
        self.ybias = random.randint(-1, 1)
        self.resetBias = False

        #load sprite images
        self.PILimg1 = Image.open("media/zombie1.png")
        self.PILimg1 = self.PILimg1.resize((64, 84)) 
        self.PILimg2 = Image.open("media/zombie2.png")
        self.PILimg2 = self.PILimg2.resize((84, 104)) 
        self.PILimg3 = Image.open("media/zombie3.png")
        self.PILimg3 = self.PILimg3.resize((84, 104)) 
        
    
    def draw(self):
        # spawn in random position??
        # self.circle = self.canvas.create_oval(
        #                  250, 250, 200, 200, fill = "brown")

        #picking zombie sprite
        num = random.randint(1,3)
        if num == 1:
            self.tkimg = ImageTk.PhotoImage(self.PILimg1)
        elif num == 2:
            self.tkimg = ImageTk.PhotoImage(self.PILimg2)
        else:
            self.tkimg = ImageTk.PhotoImage(self.PILimg3)
        
        self.img = self.canvas.create_image((random.randint(45,325),random.randint(45,425)),image=self.tkimg)

    def movement(self):
        if Zombie.getInPlay():
            self.x = random.randint(-1*self.max_speed, self.max_speed)
            self.y = random.randint(-1*self.max_speed, self.max_speed)

            if random.randint(1,4) < 4: # adding movement bias to make zombies better
                self.x = self.xbias * self.max_speed
                self.y = self.ybias * self.max_speed
            #print( "self x: " + str(self.x) + " self y: " + str(self.y))
            coords = self.canvas.coords(self.img)
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
            self.canvas.move(self.img, self.x, self.y)
            # new random input
            self.canvas.after(100, self.movement)


        
class RunningZombie(Zombie):
    def __init__(self, canvas, hero):
        super(RunningZombie, self).__init__(canvas)
        self.max_speed = 7
        self.player = hero

        #load sprite images
        self.PILimg1 = Image.open("media/angry_zombie.png")
        self.PILimg1 = self.PILimg1.resize((32, 42))
        self.PILimg2 = Image.open("media/angry_zombie.png")
        self.PILimg2 = self.PILimg2.resize((32, 42))
        self.PILimg3 = Image.open("media/angry_zombie.png")
        self.PILimg3 = self.PILimg3.resize((32, 42))

    def draw(self):
        #picking zombie sprite
        num = random.randint(1,3)
        if num == 1:
            self.tkimg = ImageTk.PhotoImage(self.PILimg1)
        elif num == 2:
            self.tkimg = ImageTk.PhotoImage(self.PILimg2)
        else:
            self.tkimg = ImageTk.PhotoImage(self.PILimg3)
        
        self.img = self.canvas.create_image((random.randint(45,325),random.randint(45,425)),image=self.tkimg)
    
    def movement(self):
        # needs to follow user positions
        if Zombie.getInPlay():
            # determine x and y based on player position
            player_pos = self.canvas.coords(self.player.getSprite())
            zombie_pos = self.canvas.coords(self.img)

            self.x = (zombie_pos[0] - player_pos[0])*-1
            self.y = (zombie_pos[1] - player_pos[1])*-1

            if (abs(self.x) > self.max_speed):
                if(self.x > 0): self.x = self.max_speed
                elif(self.x < 0): self.x = self.max_speed*-1

            if (abs(self.y) > self.max_speed):
                if(self.y > 0): self.y = self.max_speed
                elif(self.y < 0): self.y = self.max_speed*-1


            # then move
            self.canvas.move(self.img, self.x, self.y)
            # new random input
            self.canvas.after(100, self.movement)

class RandomZombie(Zombie):
    def __init__(self, canvas):
        super(RandomZombie, self).__init__(canvas)
        self.max_speed = 5
        self.xbias = random.randint(-1, 1)
        self.ybias = random.randint(-1, 1)
        self.resetBias = False

        #load sprite images
        self.PILimg1 = Image.open("media/zombie1.png")
        self.PILimg1 = self.PILimg1.resize((32, 42))
        self.PILimg2 = Image.open("media/zombie2.png")
        self.PILimg2 = self.PILimg2.resize((32, 42))
        self.PILimg3 = Image.open("media/zombie3.png")
        self.PILimg3 = self.PILimg3.resize((32, 42))
        
    
    def draw(self):

        #picking zombie sprite
        num = random.randint(1,3)
        if num == 1:
            self.tkimg = ImageTk.PhotoImage(self.PILimg1)
        elif num == 2:
            self.tkimg = ImageTk.PhotoImage(self.PILimg2)
        else:
            self.tkimg = ImageTk.PhotoImage(self.PILimg3)
        
        self.img = self.canvas.create_image((random.randint(45,325),random.randint(45,425)),image=self.tkimg)

    def movement(self):
        if Zombie.getInPlay():
            self.x = random.randint(-1*self.max_speed, self.max_speed)
            self.y = random.randint(-1*self.max_speed, self.max_speed)

            if random.randint(1,4) < 4: # adding movement bias to make zombies better
                self.x = self.xbias * self.max_speed
                self.y = self.ybias * self.max_speed
            #print( "self x: " + str(self.x) + " self y: " + str(self.y))
            coords = self.canvas.coords(self.img)
    
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

            # either return x and y or pass in canvas during init 
            # self.canvas.move(self.circle, self.x, self.y)

            self.canvas.move(self.img, self.x, self.y)
            # new random input
            self.canvas.after(100, self.movement)

        
