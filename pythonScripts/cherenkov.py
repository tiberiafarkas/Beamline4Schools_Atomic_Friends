import numpy as np
import matplotlib.pyplot as plt
import math
# >>>> Constants

# > rest mass of electron
m0_e = 9.109e-31 # [kg]
# > rest mass of proton
m0_p = 1.673e-27 # [kg]
# > speed of light
c = 299792458   # [m/s]
# > refractive index N2
n_N2 = 1.00029
# > refractive index Ar
n_Ar = 1.000281
# > refractive index He
n_He = 1.00036

# >>>> Calculations
# E -> particle energy [J]
# p -> momentum [kg*m/s]
# mo -> rest mass [kg]
# c -> speed of light [m/s]
# v -> particle velocity [m/s]
# B -> velocity relative to speed of light in vacuum

# E*2 = (p*c)2 + (m0*c2)*2
def momentum(m0, E, c):
   E2 = E**2
   c2 = c**2
   print(np.sqrt((E2 - (m0 * c2)**2) / c2))
   return np.sqrt((E2 - (m0 * c2)**2) / c2)

def betta(m0, E, c):
    gamma = np.sqrt(1 + (momentum(m0, E, c) / (m0 * c)) ** 2)
    bettta = np.sqrt(1 - (1 / gamma) ** 2) # initially, you forgot to put sqrt for beta
    print(gamma)
    return bettta

# cos(theta) = 1 / (B*n)
def cherenkovAngle(m0, E, n, c):
    B = betta(m0, E, c)
    print(B)
    try:
        theta = math.acos(1 / (B * n))
        return theta
    except ValueError:
        print("Cherenkov radiation would not be observed in the given conditions")
        return -10

# >>>> Plotting

def draw_cherenkov_ring(E, m0, n, radius=10, ax=None):
    if ax is None:
        fig = plt.figure(figsize=(10, 5))
        ax = fig.add_subplot(121, projection='3d')
        ax_side = fig.add_subplot(122)

    theta = cherenkovAngle(m0, E, n, 3e8)
    
    if theta == -10 :
        return
    
    phi = np.linspace(0, 2*np.pi, 100)
    
    for r in range(0, radius + 1):
        x = r * np.sin(theta) * np.cos(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(theta)

        ax.plot(x, y, z)
        ax_side.plot(x, y)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Cherenkov Ring')

    ax_side.set_xlabel('X')
    ax_side.set_ylabel('Y')
    ax_side.set_aspect('equal', adjustable='box')
    ax_side.set_title('Side View')

    plt.tight_layout()
    plt.show()


def draw_cherenkov_ring_2d(E, m0, n, radius=10):
    fig, ax = plt.subplots(figsize=(8, 6))

    theta = cherenkovAngle(m0, E, n)
    phi = np.linspace(0, 2*np.pi, 100)
    
    for r in range(0, radius + 1):
        x = r * np.sin(theta) * np.cos(phi)
        y = r * np.sin(theta) * np.sin(phi)
        ax.plot(x + r, y + r)

    ax.plot([0, 2*radius], [0, 2*radius], color='black', linestyle='--')

    ax.set_aspect('equal', 'box')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Cherenkov Rings')
    ax.legend()

    plt.show()

draw_cherenkov_ring(1.121e-9, m0_p, 1.33)
