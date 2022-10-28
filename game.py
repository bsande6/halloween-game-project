import tkinter
import random

score = 0
time = 0
in_play = False
  
# function that will start the game.
def startGame(event):
    global in_play
    in_play = True
    countTime()
    scoreLabel.config(text = "Score: " + str(score))
    timeLabel.config(text = "Time: " + str(time))
    # factories
    # spawn player
    # spawn zombies 

def countTime():
  
    global time
  
    if in_play:
        time += 1
          
        timeLabel.config(text = "Time: "
                               + str(time))
                                 
        # run the function again after 1 second.
        timeLabel.after(1000, countTime)
  


root = tkinter.Tk()
  
root.title("Name Placeholder")
  
root.geometry("400x300")
  
# add an instructions label
instructions = tkinter.Label(root, text = "Survive for as long as Possible!",
                                      font = ('Helvetica', 12))
instructions.pack() 
  
# add a score label
scoreLabel = tkinter.Label(root, text = "Press enter to start",
                                      font = ('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root)
timeLabel.pack()

                
label = tkinter.Label(root, font = ('Helvetica', 60))
label.pack()

  
# run the 'startGame' function 
# when the enter key is pressed
root.bind('<Return>', startGame)
  
# start the GUI
root.mainloop()
          