import turtle as t

t.shape('turtle')
n = 12
l = 60

for i in range(n):
	t.forward(l)
	t.stamp()
	t.left(180)
	t.forward(l)
	t.right(180+360/n)

