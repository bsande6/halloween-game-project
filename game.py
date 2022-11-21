import tkinter as tk
import random

from PIL import Image, ImageTk

from hero import Hero
from abstract_factory import BasicZombieFactory, RunningZombieFactory


class Cons:
    BOARD_WIDTH = 500
    BOARD_HEIGHT = 400
  
# function that will start the game.
class App():
    def __init__(self, root):
        self.root= root
        # configure the root window
        self.root.title('My Awesome App')
        #self.root.geometry('500x400')
        self.instructions = tk.Label(self.root, text = "Survive for as long as Possible!",
                                        font = ('Helvetica', 12))
        self.instructions.pack() 
        self.scoreLabel = tk.Label(self.root, text = "Press enter to start",
                                        font = ('Helvetica', 12))
        self.scoreLabel.pack()

        self.timeLabel = tk.Label(self.root)
        self.timeLabel.pack()
        self.time =0
        # Could include collecting pumpkins 
        self.score = 0
        self.in_play = False
        self.hero = None
        self.canvas = tk.Canvas(root, bg="green", height=Cons.BOARD_WIDTH, width=Cons.BOARD_HEIGHT)

        self.label = tk.Label(font = ('Helvetica', 60))
        self.label.pack()

        self.root.bind('<Return>', self.startGame)
        

    def startGame(self,event):
        self.root.unbind('<Return>')
        self.in_play = True
        self.countTime()
        self.scoreLabel.config(text = "Score: " + str(self.score))
        self.timeLabel.config(text = "Time: " + str(self.time))
        self.hero= Hero(self.root, self.canvas)
        self.canvas.pack()
        
        self.root.bind("<KeyPress-Left>", lambda e: self.hero.left(e))
        self.root.bind("<KeyPress-Right>", lambda e: self.hero.right(e))
        self.root.bind("<KeyPress-Up>", lambda e: self.hero.up(e))
        self.root.bind("<KeyPress-Down>", lambda e: self.hero.down(e))
        #self.root.bind("<KeyPress-s">, lambda e: self.hero.stop(e))
        self.pumpkin_x = 0
        self.pumpkin_y = 0
        self.pumpkin_img = Image.open("media/pumpkin.jpg")
        self.pumpkin_img=self.pumpkin_img.resize((30, 30))
        self.pumpkin = ImageTk.PhotoImage(self.pumpkin_img)
        self.spawnPumpkin()

        self.checkPumpkinCollision()
        self.basic_zombie_factory = BasicZombieFactory()

        self.basic_zombie_factory.create_zombie()


        # factories
      
        # spawn zombies 
        
    def spawnPumpkin(self):
        self.pumpkin_x = random.randint(40, Cons.BOARD_HEIGHT-30)
        self.pumpkin_y = random.randint(40, Cons.BOARD_WIDTH-30) 
        self.pmpk = self.canvas.create_image(self.pumpkin_x, self.pumpkin_y, image=self.pumpkin)
      

    def countTime(self):
        if self.in_play:
            self.time += 1
           
            self.timeLabel.config(text = "Time: "
                                + str(self.time))
                                    
            # run the function again after 1 second.
            self.timeLabel.after(1000, self.countTime)

    def checkPumpkinCollision(self):
        user_coords = self.canvas.coords(self.hero.getSprite())
        #if user.coords 
        coll = self.canvas.find_overlapping(user_coords[0], user_coords[1], user_coords[2], user_coords[3])
        
        coll = list(coll)   
        coll.remove(self.hero.getSprite())

        if self.pmpk in coll:
            self.score += 1
            self.scoreLabel.config(text = "Score: "
                                + str(self.score))
            self.canvas.delete(self.pmpk)
            self.spawnPumpkin()

        # This might be cpu intense 
        self.root.after(500, self.checkPumpkinCollision)

    def endGame(self):
        self.scoreLabel.config(text = "Final Score: " + str(score))
        self.timeLabel.config(text = "Final Time: " + str(time))
        


if __name__ == "__main__":
  root = tk.Tk()
  app = App(root)
  root.mainloop()
            
