from turtle import Turtle
X_AXIS = [0,-20,-40] # positions of each turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """Create snake"""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Step 1: Create a snake body
    # create 3 turtles: each turtle should be a white square size: 20x20
    def create_snake(self):
        seg = [Turtle(shape="square") for _ in range(3)]
        for i in range(0, 3):
            seg[i].penup()
            seg[i].color("white")
            seg[i].goto(x=X_AXIS[i], y=0)
            self.segments.append(seg[i])

    # Step 2: Move the snake
    def move(self):
        for i in range(len(self.segments)-1,0,-1):  # range(start=2 ,stop=0 ,step=-1) -- reverse order (step is how to get from start to stop)
            new_x = self.segments[i - 1].xcor()  # seg3 replaces position of seg2 and seg2 replaces seg1
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)  # move current seg to previous location of the segment before it
        self.head.forward(MOVE_DISTANCE)  # move first seg to direction we want

    def up(self):
        if self.head.heading() != DOWN: #self.head.setheading() doesn't return the current heading.
                                        #setheading() is a setter,not a getter—it sets the heading,but doesn’t return it
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_seg(self):
        seg = Turtle(shape="square")
        seg.penup()
        seg.color("white")
        seg.goto(self.segments[-1].position()) # self.segment[-1] is last segment on list and
                                               # .position() to get x-y coordinate of it
        self.segments.append(seg)

    def restart_snake(self):
        for seg in self.segments:
            seg.hideturtle()  # make each segment invisible
        self.segments.clear() # clear the list (same as self.segments = [])
        self.create_snake()
        self.head = self.segments[0]