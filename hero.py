from tkinter import *
from PIL import ImageTk, Image
class Hero():
    def __init__(self, root, canvas):
        self.root = root
        # spawn in random position??
        self.x = 0
        self.y = 0
        self.inplay = True
        # maybe use these for movement
        self.x_vel=0
        self.y_vel=0
        self.speed = 5
        self.canvas = canvas
        # temporary sprite
        # maybe spawn in center of board

        self.PILimg1 = Image.open("media/cat.png")
        self.PILimg1 = self.PILimg1.resize((32, 28))
        self.tkimg = ImageTk.PhotoImage(self.PILimg1)

        self.heroimg = self.canvas.create_image((0,0),image=self.tkimg)

        self.width = int(self.canvas.cget("width"))
        self.height = int(self.canvas.cget("height"))
        self.movement()

    
    def movement(self):
        if self.inplay == True:
            coords = self.canvas.coords(self.heroimg)
            if coords[0] < 10 and self.x < 0:
                self.x = 0
            elif coords[0] > (self.width - 30) and self.x > 0:
                self.x = 0
            if coords[1] < 10 and self.y < 0:
                self.y =0
            elif coords[1] > (self.height - 30) and self.y > 0:
                self.y = 0

            self.canvas.move(self.heroimg, self.x, self.y)
            self.canvas.after(5, self.movement)

    def left(self, event):
        self.x = -5
        self.y = 0
     
    # for motion in positive x direction
    def right(self, event):
        #if self.canvas.coords(self.rectangle) >
        self.x = 5
        self.y = 0
     
    # for motion in positive y direction
    def up(self, event):
        self.x = 0
        self.y = -5
     
    # for motion in negative y direction
    def down(self, event):
        self.x = 0
        self.y = 5

    def stop(self, event):
        self.x = 0
        self.y = 0

    def getSprite(self):
        return self.heroimg

    def setInPlay(self, inplay):
        self.inplay = inplay

