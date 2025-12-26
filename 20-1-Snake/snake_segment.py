class SnakeSegment:
    def __init__(self, position, base_size, size_factor, colour="white"):
        from turtle import Turtle

        self.size = base_size * size_factor
        self.segment = Turtle("square")

        self.segment.color(colour)
        self.segment.speed("fastest")
        self.segment.penup()
        self.segment.goto(position)
        self.last_position = position
        self.segment.resizemode("user")
        self.segment.shapesize(stretch_len=size_factor, stretch_wid=size_factor)

    def increase_speed():
        pass

    def move_forward(self):
        print("moving from position:", self.segment.position())
        self.last_position = self.segment.position()
        self.segment.forward(self.size)
        print("moved to position:", self.segment.position())
    
    def move_to(self, position):
        self.last_position = self.segment.position()
        self.segment.goto(position)

    def turn_left(self):
        self.segment.left(90)

    def turn_right(self):
        self.segment.right(90)

    def face_left(self):
        print("facing left")
        self.segment.setheading(180)

    def face_right(self):
        print("facing right")
        self.segment.setheading(0)

    def face_up(self):
        print("facing up")
        self.segment.setheading(90)

    def face_down(self):
        print("facing down")
        self.segment.setheading(270)

    def get_position(self):
        return self.segment.position()

    def get_last_position(self):
        return self.last_position
