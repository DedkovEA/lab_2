import turtle as t

t.shape('turtle')

def star(n, a = 100):
	for i in range(n):
		t.forward(a)
		t.left(180*(1-1/n))

t.penup()
t.goto(-50, 30)
t.left(180)
t.pendown()
star(5, 150)

t.penup()
t.goto(110,90)
t.left(70)
t.pendown()
star(9, 150)

i = input()
