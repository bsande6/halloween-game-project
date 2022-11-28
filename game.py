import tkinter as tk
import random

from PIL import Image, ImageTk

from hero import Hero
from pumpkin import Pumpkin
from abstract_factory import ZombieFactory

class Cons:
    BOARD_WIDTH = 500
    BOARD_HEIGHT = 400
  

class App():
    def __init__(self, root):
        self.root= root
        # configure the root window
        self.root.title('Post-Apocalyptic Survival Game')
        self.instructions = tk.Label(self.root, text = 
        "Run Away From Zombies! Collect Pumpkins!\nStay Alive as Long as Possible! Use Arrow Keys to Move",
                                        font = ('Helvetica', 12))
        self.instructions.pack() 
        self.scoreLabel = tk.Label(self.root, text = "Press enter to start",
                                        font = ('Helvetica', 12))
        self.scoreLabel.pack()
        self.timeLabel = tk.Label(self.root)
        self.timeLabel.pack()

        self.levelLabel = tk.Label(self.root, text = "", font = ('Helvetica', 14))
        self.levelLabel.pack(side="bottom")
        self.restartLabel = tk.Label(self.root, text = "", font = ('Helvetica', 12))
        self.restartLabel.pack()
        self.time =0 
        self.score = 0

        self.level = 1
        self.spawn_interval = 7

        #probabilities for zombies to spawn (change with each level)
        self.zRandomProb = 0.75
        self.zLargeProb = 0.20
        self.zRunningProb = 0.5

        self.in_play = False
        self.hero = None
        self.canvas = tk.Canvas(root, height=Cons.BOARD_WIDTH, width=Cons.BOARD_HEIGHT)
        #load background img
        self.dirt_img = Image.open("media/dirt1.png")
      
        self.dirtimg = ImageTk.PhotoImage(self.dirt_img)

        self.bg = self.canvas.create_image(0,0, image=self.dirtimg, anchor="nw")
        self.label = tk.Label(font = ('Helvetica', 60))
        self.label.pack()
        self.root.bind('<Return>', self.startGame)
        

    def startGame(self,event):
        self.root.unbind('<Return>')
        self.in_play = True
        self.countTime()
        self.scoreLabel.config(text = "Score: " + str(self.score))
        self.timeLabel.config(text = "Time: " + str(self.time))
        self.levelLabel.config(text= "Level 1")
       
        self.hero= Hero(self.root, self.canvas)
        self.canvas.pack()
        
        self.root.bind("<KeyPress-Left>", lambda e: self.hero.left(e))
        self.root.bind("<KeyPress-Right>", lambda e: self.hero.right(e))
        self.root.bind("<KeyPress-Up>", lambda e: self.hero.up(e))
        self.root.bind("<KeyPress-Down>", lambda e: self.hero.down(e))
        #self.root.bind("<space>", lambda e: self.hero.stop(e))
        
        #hack key to get to level three for demo:
        self.root.bind("t", lambda e: self.level3())

        self.pumpkin_template = Pumpkin(self.canvas)
        self.spawnPumpkin()

        self.checkPumpkinCollision()
        self.factory = ZombieFactory()
        self.zombie = self.spawnZombie()

    def spawnZombie(self):
        # randomly determine what kind of zombie spawns based on zProbabilites
        num = random.random()
        ztype = "random"
        if( num < self.zRandomProb ):
            ztype = "random"
        elif( num < (self.zRandomProb+self.zLargeProb) ):
            ztype = "large"
        else:
            ztype = "running"

        zombie = self.factory.create_zombie(ztype, self.canvas, self.hero)
        zombie.setInPlay(True)
        zombie.draw()
        zombie.movement()
        return zombie

    def spawnPumpkin(self):
        # clone pattern allows this to be faster
        pumpkin_clone = self.pumpkin_template.clone() 
        self.pmpk = pumpkin_clone.draw()

    def countTime(self):
        if self.in_play:
            self.time += 1
           
            self.timeLabel.config(text = "Time: "
                                + str(self.time))
                                    
            # run the function again after 1 second.
            self.timeLabel.after(1000, self.countTime)

        if self.time == 30 or self.score == 10:
            if( self.level != 3):
                self.level2()

        if self.time == 60 or self.score == 20:
            self.level3()

        if self.time % self.spawn_interval == 0:
            self.spawnZombie()

    def level1(self):
        self.level = 1
        self.levelLabel.config(text="Level 2")
        self.spawn_interval = 5
        self.zRandomProb = 0.33
        self.zLargeProb = 0.33
        self.zRunningProb = 0.33

    # function to change difficulty parameters for level 2 difficulty
    def level2(self):
        self.level = 2
        self.levelLabel.config(text="Level 2")
        self.spawn_interval = 5
        self.zRandomProb = 0.33
        self.zLargeProb = 0.33
        self.zRunningProb = 0.33

    # function to change difficulty parameters for level 3 difficulty
    def level3(self):
        self.level = 3
        self.levelLabel.config(text="Level 3")
        self.spawn_interval = 5
        self.zRandomProb = 0.10
        self.zLargeProb = 0.15
        self.zRunningProb = 0.75


    def checkPumpkinCollision(self):
        
        if self.in_play:
            user_coords = self.canvas.bbox(self.hero.getSprite()) #self.canvas.coords(self.hero.getSprite())
            #if user.coords 
            coll = self.canvas.find_overlapping(user_coords[0], user_coords[1], user_coords[2], user_coords[3])
            
            coll = list(coll)   
            coll.remove(self.hero.getSprite())
            coll.remove(self.bg)

            if self.pmpk in coll:
                self.score += 1
                self.scoreLabel.config(text = "Score: "
                                    + str(self.score))
                coll.remove(self.pmpk)
                self.canvas.delete(self.pmpk)
                self.spawnPumpkin()
            
            if len(coll) > 0:
                # must be colliding with zombie
                self.endGame()

            # collisions are not perfect becuase of the rate of the funciton calls, this can be increased if desired 
            self.root.after(5, self.checkPumpkinCollision)

    def restart(self, event):
        self.root.destroy()
        root = tk.Tk()
        app = App(root)
        root.mainloop() 

    def endGame(self):
        # show scores then prompt to play again
        self.in_play= False
        self.root.unbind("<KeyPress-Left>")
        self.root.unbind("<KeyPress-Right>")
        self.root.unbind("<KeyPress-Up>")
        self.root.unbind("<KeyPress-Down>")

        self.hero.setInPlay(False)
        self.zombie.setInPlay(False)
        
    
        # destroy hero and zombies to prevent errors in move functions
        del self.hero
        del self.zombie

        self.canvas.delete('all')
        self.instructions.config(text = "Game Over!", font = ('Helvetica', 20))
        self.scoreLabel.config(text = "Final Score: " + str(self.score))
        self.timeLabel.config(text = "Final Time: " + str(self.time))
        self.restartLabel.config(text="Press enter to restart")
        
        
        self.root.bind('<Return>', self.restart)    

if __name__ == "__main__":
  root = tk.Tk()
  app = App(root)
  root.mainloop()
            
