#turtle3.py
import turtle
w = turtle.Screen()
w.bgcolor("#c6e2ff")
t = turtle.Turtle()
t.color("#dd00dd")

def thepoly(size):
	for i in range(40000):
		t.fd(size)
		t.left(280)
		size = size + 1
		t.speed()
		
thepoly(50)
holdit = input();
