def create_border(self, position, heading, forward):
    border = Turtle()
    border.color("orange")
    border.ht()
    border.penup()
    border.pensize(width=2)
    border.goto(position)
    border.pendown()
    border.setheading(heading)
    border.forward(forward)

def create_borders(self):
    # Right Border
    self.create_border((290,235), 270, 470)
    # Left Border
    self.create_border((-300, 235), 270, 470)
    # UP Border
    self.create_border((-300, 235), 0, 590)
    # Down Border
    self.create_border((-300, -235), 0, 590)