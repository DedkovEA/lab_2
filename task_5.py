import turtle as t

t.shape('turtle')
delta = 40
first = 100
square_number = 10

for i in range(square_number):
	for j in range(4):
		t.forward(first+i*delta)
		t.left(90)
	t.penup()
	t.goto(-delta*(i+1)/2,-delta*(i+1)/2)
	t.pendown()
