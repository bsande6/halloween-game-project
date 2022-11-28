import tkinter as tk
import random

from PIL import Image, ImageTk

from hero import Hero
from pumpkin import Pumpkin
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
        self.canvas = tk.Canvas(root, height=Cons.BOARD_WIDTH, width=Cons.BOARD_HEIGHT)
        # self.background = tk.Canvas(root, height=Cons.BOARD_WIDTH, width=Cons.BOARD_HEIGHT)

        #load background img
        self.dirt_img = Image.open("media/dirt1.png")
        #self.dirt_img = self.dirt_img.resize(())
        self.dirtimg = ImageTk.PhotoImage(self.dirt_img)

        self.bg = self.canvas.create_image(0,0, image=self.dirtimg, anchor="nw")

        # self.backgroundLabel = tk.Label(self.canvas, image=self.dirtimg)
        # self.backgroundLabel.place(x=0,y=0,relwidth=1, relheight=1)

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
        # self.background.place(x=self.canvas.winfo_rootx(), y=self.canvas.winfo_rooty())
        
        self.root.bind("<KeyPress-Left>", lambda e: self.hero.left(e))
        self.root.bind("<KeyPress-Right>", lambda e: self.hero.right(e))
        self.root.bind("<KeyPress-Up>", lambda e: self.hero.up(e))
        self.root.bind("<KeyPress-Down>", lambda e: self.hero.down(e))
        self.root.bind("<space>", lambda e: self.hero.stop(e))

        # self.pumpkin_x = 0
        # self.pumpkin_y = 0
        # self.pumpkin_img = Image.open("media/pumpkin.jpg")
        # self.pumpkin_img=self.pumpkin_img.resize((30, 30))
        # self.pumpkin = ImageTk.PhotoImage(self.pumpkin_img)
        self.pumpkin_template = Pumpkin(self.canvas)
        self.spawnPumpkin()

        self.checkPumpkinCollision()
        self.factory = ZombieFactory()
        self.zombie = self.spawnZombie()

    def spawnZombie(self):
        # choose what type of zombie in this function either randomly or based on score/time
        # probably should have made a gameboard class which has canvas as an attribute that we can get it from but im just gonna pass it in for ease
        # at this point

        # randomly determine what kind of zombie spawns
        # num = random.randint(1, 4)
        num = 4 # for testing
        ztype = "random"
        if( num == 1 or num == 2 ):
            ztype = "random"
        elif( num == 3 ):
            ztype = "large"
        elif( num == 4 ):
            ztype = "running"

        zombie = self.factory.create_zombie(ztype, self.canvas, self.hero)
        zombie.setInPlay(True)
        zombie.draw()
        zombie.movement()
        return zombie

    def spawnPumpkin(self):
        # clone pattern shuold allow this to be faster
        pumpkin_clone = self.pumpkin_template.clone() 
        self.pmpk = pumpkin_clone.draw()
        #self.pumpkin_x = random.randint(40, Cons.BOARD_HEIGHT-30)
        #self.pumpkin_y = random.randint(40, Cons.BOARD_WIDTH-30) 
        #self.pmpk = self.canvas.create_image(self.pumpkin_x, self.pumpkin_y, image=self.pumpkin)

    def countTime(self):
        if self.in_play:
            self.time += 1
           
            self.timeLabel.config(text = "Time: "
                                + str(self.time))
                                    
            # run the function again after 1 second.
            self.timeLabel.after(1000, self.countTime)
        if self.time % 5 == 0:
            self.spawnZombie()



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

            # This might be cpu intense 
            # collisions are not perfect becuase of the rate of the funciton calls, this can be increased if desired 
            self.root.after(5, self.checkPumpkinCollision)

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
            
