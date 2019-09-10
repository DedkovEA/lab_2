import turtle as t

t.shape('turtle')

R = 100
N = 6

def draw_circle(r, d_fi = 5):
	for i in range(int(360/d_fi)):
		t.forward(r*d_fi*3.14/180)
		t.left(d_fi)

for i in range(6):
	draw_circle(R)
	t.left(360/N)
