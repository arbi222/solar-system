import turtle
from math import *
import random
import pygame
from pygame import mixer

# adding the song
pygame.init()
mixer.music.load('Solar_music.wav')
mixer.music.play(-1)


# creating the window size and adding a background
window = turtle.Screen()
window.setup(1550,800)
#window.bgcolor('black')
window.bgpic("background.gif")
window.tracer(0)


# Creating the Sun
Sun = turtle.Turtle()
Sun.shape('circle')
Sun.shapesize(5 , 4.7)
Sun.color('#FF0800')


# The class of the planets
class Planet(turtle.Turtle):
	def __init__(self, radius, color, size, star, offset):
		super().__init__(shape = 'circle')
		self.radius = radius
		self._color = color
		self.color(self._color)
		self.size = size
		self.star = star
		self.offset = offset
		self.shapesize(size , size)
		self.angle = 0

	# the moving function for all the planets
	def move(self):
		x = self.offset + (self.radius * cos(self.angle))
		y = self.radius * sin(self.angle) * 0.8
		
		self.goto(self.star.xcor() + x , self.star.ycor() + y)

	# the moving function for the Uranus's rings
	def move_Uranus_rings(self):
		x = self.offset + (self.radius + cos(self.angle)) - 20
		y = self.radius * sin(self.angle) * 0.9

		self.goto(self.star.xcor() + x , self.star.ycor() + y)


# Planets with it's moons		#2400 km
Mercury = Planet(75 , '#A9A9A9' , 0.2 , Sun , -6) # a bit larger than the Moon
								
								# 6000 km
Venus = Planet(-106 , '#eed053' , 0.6 , Sun , 4)

								# 6300 km
Earth = Planet(156 , '#7F9FBC' , 0.63 , Sun , 0)
Moon = Planet(12 , '#F4F6F0' , 0.13 , Earth , 0) # 1700 km

								# 3300 km
Mars = Planet(198 , '#BC2732' , 0.315 , Sun , -10)
Phobos = Planet(10 , '#F7EAC6', 0.058 , Mars , 0) # 11.2 km
Deimos = Planet(13, 'grey', 0.048, Mars, 0) # 6.2 km


# The Asteroid Belt Between Mars and Jupiter
asteroid_list = []
angle = 0.0

for i in range(200):
	Asteroid_Belt = Planet(random.randint(240, 247), 'dark grey', 0.032, Sun , 0)
	Asteroid_Belt.penup()
	asteroid_list.append(Asteroid_Belt)
	Asteroid_Belt.angle += angle
	angle += 0.212421 



								# 70000 km
Jupiter = Planet(-350 , '#E39D1B' , 2.95 , Sun , 5)
IO = Planet(44 , '#fe8a64' , 0.135 , Jupiter , 0) # 1800 km
Europa = Planet(60 , '#C3C2BE' , 0.128 , Jupiter , 0) # 1650 km
Ganymede = Planet(70 , '#b4b1b2' , 0.22 ,Jupiter , 0) # 2650 km
Callisto = Planet(85 , '#564421' , 0.2 , Jupiter , 0) # 2400 km

								# 58000 km
Saturn = Planet(540, '#ab604a' ,  2.36 , Sun , 6)
Saturn_rings = []
angle = 0.0
for i in range(150):
	Rings = Planet(random.randint(33, 33), 'dark grey', 0.02, Saturn , 0)
	Rings.penup()
	Saturn_rings.append(Rings)
	Rings.angle += angle
	angle += 0.912421 
for i in range(120):
	Rings2 = Planet(random.randint(38, 39), 'dark grey', 0.02, Saturn , 0)
	Rings2.penup()
	Saturn_rings.append(Rings2)
	Rings2.angle += angle
	angle += 0.912421 
Mimas = Planet(50 , 'dark grey', 0.05 , Saturn , 0) # 200 km 
Enceladus = Planet(70 , 'dark grey' , 0.06 , Saturn , 0) # 252 km
Dione = Planet(80 , 'dark grey' , 0.099 , Saturn , 0 ) # 561 km
Titan = Planet(-100 , '#D2941B' , 0.23 , Saturn , 0) # 2560 km

								# 25500 km
Uranus = Planet(-700 , '#4FD0E7' , 1.3 , Sun , 10)
Uranus_rings = []
angle = 0.0
for i in range(100):
	Rings = Planet(random.randint(19, 19), '#B22222', 0.02, Uranus , 0)
	Rings.penup()
	Uranus_rings.append(Rings)
	Rings.angle += angle
	angle += 0.612421
Umbriel = Planet(25 , 'dark grey', 0.11 , Uranus , 0) # 584 km 
Titania = Planet(35 , 'dark grey' , 0.116 , Uranus , 0) # 788 km
Ariel = Planet(42 , 'dark grey' , 0.1 , Uranus , 0 ) # 578 km

								# 24600 km
Neptune = Planet(790 , '#4b70dd' , 1.2 , Sun , 5)
Triton = Planet(-30 , '#328cba' , 0.121 , Neptune , 2) # 1350 km


# Creating the asteroid belt after the Neptune planet
asteroid_list2 = []
angle = 0.0

for i in range(100):
	Kuiper_Belt = Planet(random.randint(800, 900), 'dark grey', 0.10009, Sun , 0)
	Kuiper_Belt.penup()
	asteroid_list2.append(Kuiper_Belt)
	Kuiper_Belt.angle += angle
	angle += 0.512421 

# # List with all the planets and their moons
Object_list = [ Mercury, 
				Venus , 
				Earth , Moon , 
				Mars , Phobos , Deimos , 
				Jupiter , IO , Europa , Ganymede , Callisto ,
				Saturn , Mimas , Enceladus , Dione , Titan ,
				Uranus , Umbriel , Titania , Ariel ,
				Neptune , Triton]


for i in Object_list:
    i.penup()
    i.goto(i.radius + i.offset , 0)
    if i.star == Sun:   # remove the hashtag if you want the planets to show their pathways
        i.pendown()  


# Making the objects in the Screen move 
while True:
    window.update()
    for i in Object_list:
        i.move()

    # clockwise with minus 
    Mercury.angle += 0.082954 # 88 days 
    
    Venus.angle -= 0.0325892  # 224 days 
    
    Earth.angle += 0.02 # 365 days 
    Moon.angle -= 0.2607142857	# 28 days
    
    Mars.angle += 0.0106259098 # 687 days
    Phobos.angle += 21.9  # 8 hours
    Deimos.angle += 7.84  # 30 hours

    for i in asteroid_list:
    	i.move()
    	i.angle += 0.005 # 4 years 

    Jupiter.angle += 0.0016666 # 12 years
    IO.angle += 7.2 # 43 hours
    Europa.angle += 2.0857142 # 3.5 days
    Ganymede.angle += 1.0195530 # 7.16 days
    Callisto.angle += 0.4371257 # 16.7 days

    Saturn.angle += 0.0006896552  # 29 years
    for i in Saturn_rings:
    	i.move()
    	i.angle += 0.0000001
    Mimas.angle += 7.6 # 23 hours	
    Enceladus.angle += 7.82 # 33 hours
    Dione.angle += 2.6545 # 66 hours
    Titan.angle += 0.45625 # 16 days

    Uranus.angle -= 0.0002380952 # 84 years
    for i in Uranus_rings:
    	i.move_Uranus_rings()
    	i.angle -= 0.0000001
    Umbriel.angle += 1.7696969 # 99 hours
    Titania.angle += 0.838277512 # 209 hours
    Ariel.angle += 2.6556 # 60 hours

    Neptune.angle += 0.0001212121 # 165 years
    Triton.angle += 1.2425531915 # 141 hours

    for i in asteroid_list2:
    	i.move()
    	i.angle += 0.00009
    	
	