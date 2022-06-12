from turtle import Turtle

STARTING_POSITIONS = [(-20, 0),(-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.snake_body.append(snake)

    def extend(self):
        #with lists in python you can write a negative number to start at the end of the list
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for body_part in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_part -1].xcor()
            new_y = self.snake_body[body_part -1].ycor()
            self.snake_body[body_part].goto(new_x,new_y) 
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)