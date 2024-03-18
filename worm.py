from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Worm:

    def __init__(self):
        #attribute segment
        self.segments = []
        self.create_worm()
        #creating a reference for head of the worm
        self.head = self.segments[0]

    def create_worm(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
            new_segment = Turtle("circle")
            new_segment.color("#ffde57","#4584b6")
            new_segment.speed("slow")
            new_segment.penup()
            new_segment.goto(position)
            #need to reference attribute segment
            self.segments.append(new_segment)

    def reset(self):
        #the for loop will take it to a place outside of the screen
        for seg in self.segments:
            seg.goto(1000,1000)
        #clear all segments
        self.segments.clear()
        #recreate the 3 starter skake
        self.create_worm()
        self.head = self.segments[0]

    def extend(self):
        #add new segment to the worm.
        #segment[-1] will go to the last segment of the worm
        #QUESTION: self.add_segment(self.segments[-1].position()) returns the position of the last segment.
        ##########so why it does not add the new segment on top of the last segment?
        #ANSWER: I believe (somebody else might correct me if I'm wrong) that the key explanation here is the move() method of the Worm class.
        ######## When the worm gets extended, a new segment is added to the existing list of segments of the worm. At the
        ######## start this new segment will have, in fact, the same position as the previous last segment.
        ######## Then, the move() method of Worm is called and in the for-loop each segment will move to a new position. The
        ######## new segment (which is now the last segment in the list) will not move (since it will have the same position as
        ######## the former last segment). But the former last segment, which is now the second to last segment, will move to
        ######## the position of the third to last segment.
        ####### So the new segment, which is now the last segment, will have a different position than the second to last
        ####### segment (formerly last segment), which means that they will not appear on top of each other.
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        #here you can see what this will print out: print(self.head.heading())
        #tells if the self head of the worm angle/direction (north (90), south (270)... etc.)
        if self.head.heading() != DOWN:
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







