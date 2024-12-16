#todo: движение планет и астероидов
from vpython import *
def gforce(p1, p2):
    # Calculate the gravitational force exerted on p1 by p2.
    G = 1  # Change to 6.67e-11 to use real-world values.
    # Calculate distance vector between p1 and p2.
    r_vec = p1.pos - p2.pos
    # Calculate magnitude of distance vector.
    r_mag = mag(r_vec)
    # Calcualte unit vector of distance vector.
    r_hat = r_vec / r_mag
    # Calculate force magnitude.
    force_mag = G * p1.mass * p2.mass / r_mag ** 2
    # Calculate force vector.
    force_vec = -force_mag * r_hat

    return force_vec


star = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.yellow,
              mass=1000, momentum=vector(0, 0, 0), make_trail=True)

planet1 = sphere(pos=vector(1, 0, 0), radius=0.1, color=color.blue,
                 mass=1, momentum=vector(0, 30, 0), make_trail=True)

planet2 = sphere(pos=vector(0, 3, 0), radius=0.09, color=color.red,
                 mass=2, momentum=vector(-35, 0, 0), make_trail=True)

planet3 = sphere(pos=vector(0, -4, 0), radius=0.1, color=color.green,
                 mass=10, momentum=vector(160, 0, 0), make_trail=True)

asteroids = []
rmin = 6
rmax = 9
mmin = 0.01
mmax = 0.10
for i in range(0, 20):
    r = rmin + random() * (rmax - rmin)
    theta = random() * 2 * pi
    mass = mmin + random() * (mmax - mmin)
    momentum = mass * sqrt(star.mass / r)
    ecc = 0.8 + random() * (1.2 - 0.8)  ### REMOVE THIS! ###
    asteroids.append(sphere(pos=r * vector(cos(theta), sin(theta), 0),
                            momentum=ecc * momentum * vector(-sin(theta), cos(theta), 0),
                            mass=mass, color=color.white, radius=0.15))

dt = 0.0001
t = 0
while (True):
    rate(1000)

    # Calculate forces.
    star.force = gforce(star, planet1) + gforce(star, planet2) + gforce(star, planet3)
    planet1.force = gforce(planet1, star) + gforce(planet1, planet2) + gforce(planet1, planet3)
    planet2.force = gforce(planet2, star) + gforce(planet2, planet1) + gforce(planet2, planet3)
    planet3.force = gforce(planet3, star) + gforce(planet3, planet1) + gforce(planet3, planet2)
    for a in asteroids:
        a.force = gforce(a, star) + gforce(a, planet1) + gforce(a, planet2) + gforce(a, planet3)

    # Update momenta.
    star.momentum = star.momentum + star.force * dt
    planet1.momentum = planet1.momentum + planet1.force * dt
    planet2.momentum = planet2.momentum + planet2.force * dt
    planet3.momentum = planet3.momentum + planet3.force * dt
    for a in asteroids:
        a.momentum = a.momentum + a.force * dt

    # Update positions.
    star.pos = star.pos + star.momentum / star.mass * dt
    planet1.pos = planet1.pos + planet1.momentum / planet1.mass * dt
    planet2.pos = planet2.pos + planet2.momentum / planet2.mass * dt
    planet3.pos = planet3.pos + planet3.momentum / planet3.mass * dt
    for a in asteroids:
        a.pos = a.pos + a.momentum / a.mass * dt

    t = t + dt
