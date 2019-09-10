import turtle as t

t.shape('turtle')

R_face = 200
R_eye = 15
R_mouth = 100
nose_length = 25
nose_width = 7
mouth_width = 7
length_between_eyes = 120
eyes_heigh = 60
mouth_heigh = -25


def circle(r, d_fi = 3):
	for i in range(int(360/d_fi)):
		t.forward(r*3.14/180*d_fi)
		t.left(d_fi)

def arc(r, d_fi = 3):
	for i in range(int(180/d_fi)):
		t.forward(r*3.14/180*d_fi)
		t.left(d_fi)

t.penup()
t.forward(R_face)
t.left(90)

t.pendown()
t.fillcolor("yellow")
t.begin_fill()
circle(R_face)
t.end_fill()
t.penup()

t.goto(-length_between_eyes/2+R_eye, eyes_heigh)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
circle(R_eye)
t.end_fill()
t.penup()

t.goto(length_between_eyes/2 + R_eye, eyes_heigh)
t.pendown()
t.begin_fill()
circle(R_eye)
t.end_fill()
t.penup()

t.goto(0, -nose_length/2)
t.left(180)
t.pendown()
t.pensize(nose_width)
t.forward(nose_length)
t.penup()

t.goto(-R_mouth, mouth_heigh)
t.pendown()
t.pensize(mouth_width)
t.pencolor("red")
arc(R_mouth)
