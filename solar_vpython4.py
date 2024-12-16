#todo: движение кометы и ЗСЭ
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


def ke(p1):
    # Calculate the kinetic energy of p1.
    ke = 0.5 * mag(p1.momentum) ** 2 / p1.mass

    return ke


def gpe(p1, p2):
    # Calculate the gravitational potential energy between p1 and p2.
    G = 1  # Change to 6.67e-11 to use real-world values.
    # Calculate distance vector between p1 and p2.
    r_vec = p1.pos - p2.pos
    # Calculate magnitude of distance vector.
    r_mag = mag(r_vec)
    # Calculate gravitational potential energy.
    gpe = -G * p1.mass * p2.mass / r_mag

    return gpe


star = sphere(pos=vector(0, 0, 0), radius=0.2, color=color.yellow,
              mass=1000, momentum=vector(0, 0, 0), make_trail=True)

planet1 = sphere(pos=vector(1, 0, 0), radius=0.05, color=color.blue,
                 mass=1, momentum=vector(0, 30, 0), make_trail=True)

planet2 = sphere(pos=vector(0, 3, 0), radius=0.075, color=color.red,
                 mass=2, momentum=vector(-35, 0, 0), make_trail=True)

planet3 = sphere(pos=vector(0, -4, 0), radius=0.1, color=color.green,
                 mass=10, momentum=vector(160, 0, 0), make_trail=True)

comet = sphere(pos=vector(-6, 6, 0), radius=0.05, color=color.white,
               mass=0.5, momentum=vector(-1, -1, 0), make_trail=True)

tail = cone(pos=comet.pos, axis=comet.pos - star.pos,
            size=vector(1, 1, 1) * comet.radius, color=color.white)

print("planet1 energy = ", ke(planet1) + gpe(planet1, star))
print("planet2 energy = ", ke(planet2) + gpe(planet2, star))
print("planet3 energy = ", ke(planet3) + gpe(planet3, star))
print("comet energy = ", ke(comet) + gpe(comet, star))

dt = 0.00000001
t = 0
while (True):
    rate(10000000000000)

    # Calculate forces.
    star.force = gforce(star, planet1) + gforce(star, planet2) + gforce(star, planet3)
    planet1.force = gforce(planet1, star) + gforce(planet1, planet2) + gforce(planet1, planet3)
    planet2.force = gforce(planet2, star) + gforce(planet2, planet1) + gforce(planet2, planet3)
    planet3.force = gforce(planet3, star) + gforce(planet3, planet1) + gforce(planet3, planet2)
    comet.force = gforce(comet, star)

    # Update momenta.
    star.momentum = star.momentum + star.force * dt
    planet1.momentum = planet1.momentum + planet1.force * dt
    planet2.momentum = planet2.momentum + planet2.force * dt
    planet3.momentum = planet3.momentum + planet3.force * dt
    comet.momentum = comet.momentum + comet.force * dt

    # Update positions.
    star.pos = star.pos + star.momentum / star.mass * dt
    planet1.pos = planet1.pos + planet1.momentum / planet1.mass * dt
    planet2.pos = planet2.pos + planet2.momentum / planet2.mass * dt
    planet3.pos = planet3.pos + planet3.momentum / planet3.mass * dt
    comet.pos = comet.pos + comet.momentum / comet.mass * dt
    tail.pos = comet.pos + comet.radius * vector(1, 1, 1)
    tail.axis = comet.pos - star.pos
    tail.axis = tail.axis / mag(tail.axis)

    # Update energy graphs.
    star.grph.plot(pos=(t,ke(star)))
    planet1.grph.plot(pos=(t,ke(planet1)))
    planet2.grph.plot(pos=(t,ke(planet2)))
    planet3.grph.plot(pos=(t,ke(planet3)))
    comet.grph.plot(pos=(t,ke(comet)))
    total_e = ke(star)+ke(planet1)+ke(planet2)+ke(planet3)+ke(comet)
    total_e = total_e+gpe(star,planet1)+gpe(star,planet2)+gpe(star,planet3)+gpe(star,comet)
    total_e = total_e+gpe(planet1,planet2)+gpe(planet1,planet3)+gpe(planet1,comet)
    total_e = total_e+gpe(planet2,planet3)+gpe(planet2,comet)+gpe(planet3,comet)
    total.plot(pos=(t,total_e))

    t = t + dt