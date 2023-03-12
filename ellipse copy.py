from turtle import *
from math import pi, cos, sin, sqrt, atan, tan
import matplotlib.pyplot as plt
speed("fastest")
shape("turtle")
color("red")
shapesize(1)
pensize(6)




def dessine_ellipse(a,b):
    for alpha in range(1, int(200 * pi), int(pi)):
        x = a * cos(alpha / 100)
        y = b * sin(alpha / 100)
        forward(x)
        left(90)
        forward(y)
        forward(-y)
        right(90)
        forward(-x)





rliste = []
arliste = []
xangle = []
aliste = []
yrho = []
listalpha = []
yphi = []
a = 160
b = 120
r = sqrt(a ** 2 - b ** 2)
speed("fastest")
shape("turtle")
color("red")
shapesize(1)
pensize(6)
coordonné = []
eliptique = []


dessine_ellipse(a,b)

listecorde = []



for angle in range(1, int(100 * pi), int(pi)):

    x = a * cos(angle / 100)
    y = b * sin(angle / 100)

    """color("red")
    forward(r)
    forward(x)
    left(90)
    forward(y)
    forward(-y)
    right(90)
    forward(-x)
    forward(-r)
    """
    coordonné += [(angle / 100, x, y)]
    phi = pi/2-atan((a * cos(angle / 100)+sqrt(a ** 2 - b ** 2))/(b * sin(angle / 100)))
    rho = sqrt((x + r) ** 2 + y ** 2)
    eliptique += [(phi, rho)]

    xangle.append(phi / pi * 180)

    color("blue")
    left(180 * phi / pi)
    forward(rho)
    forward(-rho)
    right(180 * phi / pi)  
    tau = sqrt((r - x) ** 2 + y ** 2)
    listecorde += [rho + tau]
    yrho.append(rho)
    rliste.append(a - r)
    arliste.append(a + r)
    aliste.append(a)
    yphi.append(atan(y / (x + r)) * 180 / pi)
    listalpha.append(angle * 180 / 100 / pi)
print(eliptique)
print(listecorde)


# 2. créer le dessin (ici ax)

fig, ax = plt.subplots(figsize=(20, 5))
ax.set_title("rayon depuis un foyer au point en fonction de l'angle")
ax.set_xlabel("angle phi")
ax.set_ylabel("rayonrho")
ax.plot(xangle, yrho)

ax.plot(xangle, rliste)
ax.plot(xangle, arliste)
ax.plot(xangle, aliste)


fig, bx = plt.subplots(figsize=(20, 5))
bx.set_xlabel("angle alpha")
bx.set_ylabel("angle phi")
bx.plot(listalpha, xangle)

fig, cx = plt.subplots(figsize=(20, 5))
cx.set_xlabel("angle alpha")
cx.set_ylabel("rayon rho")
cx.plot(listalpha, yrho)

fig, dx = plt.subplots(figsize=(20, 5))
dx.set_xlabel("angle alpha")
dx.set_ylabel("angle phi")
dx.plot(listalpha, yphi)


# 2.2 les légendes


# 3. ajouter des choses au dessin


plt.grid(True)
# 4. représenter le graphique
plt.show()

done()
