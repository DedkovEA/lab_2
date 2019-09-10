import turtle as t

t.shape('turtle')

R_0 = 50
dr = 5
N = 10

def draw_circle(r, left=True, d_fi = 5):
	if left:
		for i in range(int(360/d_fi)):
			t.forward(r*d_fi*3.14/180)
			t.left(d_fi)
	else:
		for i in range(int(360/d_fi)):
			t.forward(r*d_fi*3.14/180)
			t.right(d_fi)

t.left(90)
for i in range(N):
	draw_circle(R_0 + i*dr, True)
	draw_circle(R_0 + i*dr, False)
