#todo: движение луны и земли вокруг солнца
from vpython import *
def gforce(p1,p2):
    r_vec=p1.pos-p2.pos
    r_mag=mag(r_vec)
    r_hat=r_vec/r_mag
    force_mag=(p1.mass*p2.mass)/(r_mag**(2))
    force_vec=-force_mag*r_hat
    return force_vec
sun=sphere(pos=vector(0,0,0),color=color.yellow,radius=0.5,mass=2*100,momentum=vector(0,0,0),make_trail=True)
earth=sphere(pos=vector(2,0,0),color=color.blue,radius=0.1,mass=1,momentum=vector(0,(2*100/2)**(0.5),0),make_trail=True)
moon=sphere(pos=vector(2.1,0,0),color=color.white,radius=0.05,mass=0.001,momentum=vector(0,0.001*(2*100/2.1)**(0.5),0.001*(10)**(0.5)),make_trail=True)
t=0
dt=0.00001
while (True):
    rate(10000)
    sun.force=gforce(sun,earth)+gforce(sun,moon)
    earth.force=gforce(earth,sun)+gforce(earth,moon)
    moon.force=gforce(moon,sun)+gforce(moon,earth)
    #updating momenta
    sun.momentum=sun.momentum+sun.force*dt
    earth.momentum=earth.momentum+earth.force*dt
    moon.momentum=moon.momentum+moon.force*dt
    #updating positions
    sun.pos=sun.pos+sun.momentum*dt/sun.mass
    earth.pos=earth.pos+earth.momentum*dt/earth.mass
    moon.pos=moon.pos+moon.momentum*dt/moon.mass
    t=t+dt