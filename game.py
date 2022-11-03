import tkinter as tk
import random

score = 0
time = 0
in_play = False
  
# function that will start the game.
class App():
    def __init__(self, root):
        self.root= root
        # configure the root window
        self.root.title('My Awesome App')
        self.root.geometry('500x400')
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

                    
        self.label = tk.Label(font = ('Helvetica', 60))
        self.label.pack()

        self.root.bind('<Return>', self.startGame)

    def startGame(self,event):
    
        self.in_play = True
        self.countTime()
        self.scoreLabel.config(text = "Score: " + str(score))
        self.timeLabel.config(text = "Time: " + str(time))
        self.hero= Hero()

        # factories
        # spawn player
        # spawn zombies 

    def countTime(self):
        
        if in_play:
            self.time += 1
            
            self.timeLabel.config(text = "Time: "
                                + str(self.time))
                                    
            # run the function again after 1 second.
            self.timeLabel.after(1000, self.countTime)
    
    def endGame(self):
        self.scoreLabel.config(text = "Final Score: " + str(score))
        self.timeLabel.config(text = "Final Time: " + str(time))
        

if __name__ == "__main__":
  root = tk.Tk()
  app = App(root)
  root.mainloop()
            
