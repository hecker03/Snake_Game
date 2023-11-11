from turtle import Turtle
ORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.new_segments = []
        self.create_snake()
        self.head = self.new_segments[0]
        
    def create_snake(self):
        for i in ORDINATES:
            self.add_segment(i)

    def add_segment(self, i):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(i)
        self.new_segments.append(new_seg)

    def extend(self):
        self.add_segment(self.new_segments[-1].position())

    def move(self):
        for b in range(len(self.new_segments) - 1, 0, -1):
            new_x = self.new_segments[b - 1].xcor()
            new_y = self.new_segments[b - 1].ycor()
            self.new_segments[b].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left_(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
