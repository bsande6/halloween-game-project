from PIL import Image, ImageTk
import random
import copy
from abc import ABC, abstractmethod
# building pumpkin class to allow us to clone 
# ensure there is only one pumpkin available and that we have a 
# reference to it so that we can effectively check for the collision of a pumpkin

class Prototype(ABC):
    # Constructor:
    def __init__(self, canvas):
        
        self.canvas = canvas
        self.width = int(self.canvas.cget("width"))
        self.height = int(self.canvas.cget("height"))

    # Clone Method:
    @abstractmethod
    def clone(self):
        pass  

class Pumpkin(Prototype):
    def __init__(self, canvas):
        super(Pumpkin, self).__init__(canvas)
        # self.canvas = canvas
        # self.width = int(self.canvas.cget("width"))
        # self.height = int(self.canvas.cget("height"))
        self.pumpkin_img = Image.open("media/pumpkin.png")
        self.pumpkin_img=self.pumpkin_img.resize((40, 30))
        self.pumpkin = ImageTk.PhotoImage(self.pumpkin_img)
        self.x = 0
        self.y = 0
        
    def draw(self):
        self.x = random.randint(100, self.height-100)
        self.y = random.randint(100, self.width-100)
        return self.canvas.create_image(self.x, self.y, image=self.pumpkin)

    def clone(self):
        return copy.copy(self)
