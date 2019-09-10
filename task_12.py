import turtle as t

t.shape('turtle')
t.speed(100)

r_1 = 50
r_2 = 10
N = 4

def arc(r, d_fi = 3):
	for i in range(int(180/d_fi)):
		t.forward(r*3.14/180*d_fi)
		t.right(d_fi)

t.left(90)
for i in range(N):
	arc(r_1)
	arc(r_2)
