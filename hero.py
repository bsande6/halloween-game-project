class Hero():
    def __init__(root):
        self.root = root
        # spawn in random position??
        self.x = 0
        self.y = 0
        # maybe use these for movement
        self.x_vel=0
        self.y_vel=0
        self.speed = 5

        # temporary sprite
        self.rectangle = self.canvas.create_rectangle(
                         5, 5, 25, 25, fill = "black")
    
    def draw():
        pass

    def movement(self):
 
        # This is where the move() method is called
        # This moves the rectangle to x, y coordinates
        self.canvas.move(self.rectangle, self.x, self.y)
 
        self.canvas.after(100, self.movement)

    def left(self, event):
        print(event.keysym)
        self.x = -5
        self.y = 0
     
    # for motion in positive x direction
    def right(self, event):
        print(event.keysym)
        self.x = 5
        self.y = 0
     
    # for motion in positive y direction
    def up(self, event):
        print(event.keysym)
        self.x = 0
        self.y = -5
     
    # for motion in negative y direction
    def down(self, event):
        print(event.keysym)
        self.x = 0
        self.y = 5