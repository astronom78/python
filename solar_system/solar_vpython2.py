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


# star = sphere( pos=vector(0,0,0), radius=0.2, color=color.yellow,
#               mass = 2.0*1000, momentum=vector(0,0,0), make_trail=True )
# planet = sphere( pos=vector(1,1,1), radius=0.05, color=color.blue,
#               mass = 1, momentum=vector(0,50,0), make_trail=True )
#
# dt = 0.0001
# t = 0
# while (True):
#    rate(500)
#
#    # Calculate forces.
#    star.force = gforce(star,planet)
#    planet.force = gforce(planet,star)
#    # Update momenta.
#    star.momentum = star.momentum + star.force*dt
#    planet.momentum = planet.momentum + planet.force*dt
#    # Update positions.
#    star.pos = star.pos + star.momentum/star.mass*dt
#    planet.pos = planet.pos + planet.momentum/planet.mass*dt
#    t = t + dt
sun = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.yellow,
             mass=4 * 1000, momentum=vector(0, 0, 0), make_trail=True)

mercury = sphere(pos=vector(2, 0, 0), radius=0.005, color=color.orange,
                 mass=1, momentum=vector(0, 30, 0), make_trail=True)

venus = sphere(pos=vector(3.5, 0, 0), radius=0.01, color=color.white,
               mass=2, momentum=vector(0, 50, 0), make_trail=True)

earth = sphere(pos=vector(4, 0, 0), radius=0.01, color=color.blue,
               mass=2, momentum=vector(0, 50, 0), make_trail=True)

mars = sphere(pos=vector(4.5, 0, 0), radius=0.01, color=color.red,
              mass=1.7, momentum=vector(0, 40, 0), make_trail=True)

jupyter = sphere(pos=vector(10, 0, 0), radius=0.15, color=color.orange,
                 mass=7, momentum=vector(0, 150, 0), make_trail=True)

saturn = sphere(pos=vector(12, 0, 0), radius=0.15, color=color.magenta,
                mass=6.5, momentum=vector(0, 120, 0), make_trail=True)

uran = sphere(pos=vector(13, 0, 0), radius=0.1, color=color.blue,
              mass=5, momentum=vector(0, 110, 0), make_trail=True)

neptune = sphere(pos=vector(16, 0, 0), radius=0.1, color=color.purple,
                 mass=4, momentum=vector(0, 70, 0), make_trail=True)
#
dt = 0.0001
t = 0
while (True):
    rate(5000)

    # Calculate forces.
    sun.force = gforce(sun, mercury) + gforce(sun, venus) + gforce(sun, earth) + gforce(sun, mars) + gforce(sun,
                                                                                                            jupyter) + gforce(
        sun, saturn) + gforce(sun, uran) + gforce(sun, neptune)
    mercury.force = gforce(mercury, sun) + gforce(mercury, venus) + gforce(mercury, earth) + gforce(mercury,
                                                                                                    mars) + gforce(
        mercury, jupyter) + gforce(mercury, saturn) + gforce(mercury, uran) + gforce(mercury, neptune)
    venus.force = gforce(venus, sun) + gforce(venus, mercury) + gforce(venus, earth) + gforce(venus, mars) + gforce(
        venus, jupyter) + gforce(venus, saturn) + gforce(venus, uran) + gforce(venus, neptune)
    earth.force = gforce(earth, sun) + gforce(earth, mercury) + gforce(earth, venus) + gforce(earth, mars) + gforce(
        earth, jupyter) + gforce(earth, saturn) + gforce(earth, uran) + gforce(earth, neptune)
    mars.force = gforce(mars, sun) + gforce(mars, mercury) + gforce(mars, venus) + gforce(mars, earth) + gforce(mars,
                                                                                                                jupyter) + gforce(
        mars, saturn) + gforce(mars, uran) + gforce(mars, neptune)
    jupyter.force = gforce(jupyter, sun) + gforce(jupyter, mercury) + gforce(jupyter, venus) + gforce(jupyter,
                                                                                                      earth) + gforce(
        jupyter, mars) + gforce(jupyter, saturn) + gforce(jupyter, uran) + gforce(jupyter, neptune)
    saturn.force = gforce(saturn, sun) + gforce(saturn, mercury) + gforce(saturn, venus) + gforce(saturn,
                                                                                                  earth) + gforce(
        saturn, mars) + gforce(saturn, jupyter) + gforce(saturn, uran) + gforce(saturn, neptune)
    uran.force = gforce(uran, sun) + gforce(uran, jupyter) + gforce(uran, saturn) + gforce(uran, neptune) + gforce(uran,
                                                                                                                   mercury) + gforce(
        uran, venus) + gforce(uran, earth) + gforce(uran, mars)
    neptune.force = gforce(neptune, sun) + gforce(neptune, jupyter) + gforce(neptune, saturn) + gforce(neptune,
                                                                                                       uran) + gforce(
        neptune, mercury) + gforce(neptune, venus) + gforce(neptune, earth) + gforce(neptune, mars)

    # Update momenta.
    sun.momentum = sun.momentum + sun.force * dt
    mercury.momentum = mercury.momentum + mercury.force * dt
    venus.momentum = venus.momentum + venus.force * dt
    earth.momentum = earth.momentum + earth.force * dt
    mars.momentum = mars.momentum + mars.force * dt
    jupyter.momentum = jupyter.momentum + jupyter.force * dt
    saturn.momentum = saturn.momentum + saturn.force * dt
    uran.momentum = uran.momentum + uran.force * dt
    neptune.momentum = neptune.momentum + neptune.force * dt

    # Update positions.
    sun.pos = sun.pos + sun.momentum / sun.mass * dt
    mercury.pos = mercury.pos + mercury.momentum / mercury.mass * dt
    venus.pos = venus.pos + venus.momentum / venus.mass * dt
    earth.pos = earth.pos + earth.momentum / earth.mass * dt
    mars.pos = mars.pos + mars.momentum / mars.mass * dt
    jupyter.pos = jupyter.pos + jupyter.momentum / jupyter.mass * dt
    saturn.pos = saturn.pos + saturn.momentum / saturn.mass * dt
    uran.pos = uran.pos + uran.momentum / uran.mass * dt
    neptune.pos = neptune.pos + neptune.momentum / neptune.mass * dt

    t = t + dt