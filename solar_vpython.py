#todo: движение одной планеты вокруг солнца
from vpython import *
def gforce(p1, p2):
    G = 6.67e-3  # Change to 6.67e-3 to use real-world values.
    # вектор
    r_vec = p1.pos - p2.pos
    # модуль
    r_mag = mag(r_vec)
    r_hat = r_vec / r_mag
    # модуль гравитационной силы
    force_mag = G * p1.mass * p2.mass / r_mag ** 2
    # вектор гравитационной силы
    force_vec = -force_mag * r_hat

    return force_vec

star = sphere( pos=vector(0,0,0), radius=0.07, color=color.yellow,
               mass = 2*1000, momentum=vector(0,0,0), make_trail=True )
planet = sphere( pos=vector(1,0,0), radius=0.0007, color=color.blue,
               mass = 6, momentum=vector(0,15,0), make_trail=True )

dt = 0.0001
t = 0
while (True): #метод эйлера
    rate(500)
    star.force = gforce(star, planet)
    planet.force = gforce(planet, star)
    # импульс
    star.momentum = star.momentum + star.force * dt
    planet.momentum = planet.momentum + planet.force * dt
    # координата
    star.pos = star.pos + (star.momentum / star.mass) * dt
    planet.pos = planet.pos + (planet.momentum / planet.mass) * dt
    t = t + dt





