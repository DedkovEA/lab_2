import turtle as t
import math

t.shape('turtle')

n = 10
a_0 = 40
d_a = 20

def draw_polygon(sides, R):
	t.left(180/sides+90)
	for i in range(sides):
		t.forward(2*R*math.sin(3.14/sides))
		t.left(360/sides)
	t.right(180/sides+90)

t.penup()
t.forward(a_0)
t.pendown()
for i in range(3, n+3):
	draw_polygon(i, a_0 + (i-3)*d_a)
	t.penup()
	t.forward(d_a)
	t.pendown()
