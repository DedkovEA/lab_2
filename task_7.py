import turtle as t
import math


t.shape('turtle')

N = 10 #Number of turns
k = 10/(2*3.14) #r=k*fi
d_fi = 0.1 #Step of fi
start = 30 #Start distance from centre




t.penup()
t.forward(start)
t.pendown()
t.left(90)

for i in range(int(2*3.14/d_fi * N)):
	r = start + d_fi*i*k
	t.forward(r*d_fi)
	t.left(d_fi*180/3.14)
