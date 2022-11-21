import tkinter as tk
import random

from PIL import Image, ImageTk

from hero import Hero
#from abstract_factory import BasicZombieFactory, RunningZombieFactory, RandomZombieFactory
from abstract_factory import ZombieFactory

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
        # this label will not show up if i do not create it here
        self.restartLabel = tk.Label(self.root, text = "",
                                        font = ('Helvetica', 12))
        self.restartLabel.pack()
        self.time =0 
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
        self.root.bind("<space>", lambda e: self.hero.stop(e))

        self.pumpkin_x = 0
        self.pumpkin_y = 0
        self.pumpkin_img = Image.open("media/pumpkin.jpg")
        self.pumpkin_img=self.pumpkin_img.resize((30, 30))
        self.pumpkin = ImageTk.PhotoImage(self.pumpkin_img)
        self.spawnPumpkin()

        self.checkPumpkinCollision()
        self.factory = ZombieFactory()
        self.zombie = self.spawnZombie()

    def spawnZombie(self):
        # choose what type of zombie in this function either randomly or based on score/time
        # probably should have made a gameboard class which has canvas as an attribute that we can get it from but im just gonna pass it in for ease
        # at this point
        zombie = self.factory.create_zombie("random", self.canvas)
        zombie.draw()
        zombie.movement()
        return zombie

        
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
        if self.in_play:
            user_coords = self.canvas.coords(self.hero.getSprite())
            #if user.coords 
            coll = self.canvas.find_overlapping(user_coords[0], user_coords[1], user_coords[2], user_coords[3])
            
            coll = list(coll)   
            coll.remove(self.hero.getSprite())

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

            # This might be cpu intense 
            self.root.after(500, self.checkPumpkinCollision)

    def restart(self, event):
        self.root.destroy()
        root = tk.Tk()
        app = App(root)
        root.mainloop()

    def endGame(self):
        # show scores then prompt to play again
        #self.canvas.delete("all")
        self.in_play= False
        self.root.unbind("<KeyPress-Left>")
        self.root.unbind("<KeyPress-Right>")
        self.root.unbind("<KeyPress-Up>")
        self.root.unbind("<KeyPress-Down>")

        self.hero.setInPlay(False)
        self.zombie.setInPlay(False)
    
        # destroy hero and zombies to prevent errors in move functions
        #del self.hero

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
            
