import turtle as t

t.shape('turtle')

n = 10
a = 10

for i in range(4*n):
	t.forward(a*(i+1))
	t.left(90)
