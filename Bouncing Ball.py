import turtle
import random
import math


class Ball(turtle.Turtle):
    def __init__(self, x=0, y=800):
        super().__init__()
        self.damp = 0.98
        self.gravity = -0.05
        self.y_velocity = random.randint(-100, 100) / 10 
        self.x_velocity = random.randint(-100, 100) / 10
        self.setposition(x,y)
        self.size = 25
        self.radius = self.size / 2
        self.color("sky blue")
        self.penup
   
    def draw(self):
        self.clear()
        self.dot(self.size)

    def move(self):
        self.y_velocity += self.gravity
        self.sety(self.ycor() + self.y_velocity)
        self.setx(self.xcor() + self.x_velocity)
    
    def bounce_floor(self, floor_y):
        if self.ycor() < floor_y:
            self.y_velocity = -self.y_velocity*self.damp
            self.sety(floor_y)

    def bounce_wall(self, wall_x):
        if abs(self.xcor()) > wall_x:
            self.x_velocity = -self.x_velocity * self.damp
            sign = self.xcor() / abs(self.xcor())
            self.setx(wall_x * sign)

    def collision_check(self, other):
        distance = math.sqrt((self.xcor()-other.xcor())**2 + (self.ycor() - other.ycor()) **2 )
        if distance < self.radius + other.radius:
            return True
        else:
            return False

    def collision_resolve(self, other):
        nx = other.xcor() - self.xcor()
        ny = other.ycor() - self.ycor()
        distance = math.sqrt(nx**2 + ny**2)
        nx /= distance
        ny /= distance

        p = self.x_velocity * nx + self.y_velocity *ny - other.x_velocity * nx - other.y_velocity * ny

        self.x_velocity -= p*nx
        self.y_velocity -= p*ny
        other.x_velocity += p*nx
        other.y_velocity += p*ny
    


width = 400
height = 800

window = turtle.Screen()
window.setup(width, height)
window.tracer(0)

balls = [Ball() for i in range(100)]
counter = 0


while True: # Number of frames to capture
    for i, ball in enumerate(balls):
        ball.draw()
        ball.move()
        ball.bounce_floor(-height/2)
        ball.bounce_wall(width/2)

        for other_ball in balls[i+1:]:
            if ball.collision_check(other_ball):
                ball.collision_resolve(other_ball)

    window.update()



