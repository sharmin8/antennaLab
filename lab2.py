import numpy as np
import matplotlib.pyplot as plt

# Angle values
theta = np.linspace(0, np.pi, 200)
phi = np.linspace(0, 2 * np.pi, 200)

theta, phi = np.meshgrid(theta, phi)

# Isotropic Radiation pattern (Intensity is constant in all directions, R = 1)
R = np.ones_like(theta)

# Coordinate conversion
X = R * np.sin(theta) * np.cos(phi)
Y = R * np.sin(theta) * np.sin(phi)
Z = R * np.cos(theta)

# Plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(X, Y, Z, cmap = "plasma")

ax.set_title("3D Radiation Pattern of Isotropic Antenna")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()