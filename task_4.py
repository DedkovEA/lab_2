import turtle as t

rad = 100
N = 100 #Number of edges
t.shape('turtle')

side = rad*2*3.14/N

for i in range(N):
	t.forward(side)
	t.left(360/N)
