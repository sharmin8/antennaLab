
import numpy as np
import matplotlib.pyplot as plt

# Parameters
lam = 1
d = lam / 2
k = 2 * np.pi / lam
N = 3

# Angle range
theta = np.linspace(0, 2 * np.pi, 1000)

# Array Factor for a broadside array
AF = np.zeros_like(theta, dtype=complex)

for n in range(N):
    AF += np.exp(1j * n * k * d * np.cos(theta))

# Normalize
AF_mag = np.abs(AF)
AF_mag = AF_mag / np.max(AF_mag)

# Plot
plt.figure(figsize=(7, 7))
ax = plt.subplot(111, projection="polar")
ax.plot(theta, AF_mag)

ax.set_title("2D Radiation Pattern of a 3-Element Broadside Array")
ax.set_theta_zero_location("E")
ax.set_theta_direction(1)
ax.set_rmax(1.0)
ax.grid(True)

plt.show()
