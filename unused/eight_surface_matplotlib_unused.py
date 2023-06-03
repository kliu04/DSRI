import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.tri import Triangulation


# Parameters:
u = np.linspace(-10, 10)
v = np.linspace(-10, 10)
u, v = np.meshgrid(u, v)

# Parametrization:
x = np.ravel(np.cos(u) * np.sin(2 * v))
y = np.ravel(np.sin(u) * np.sin(2 * v))
z = np.ravel(np.sin(v))

# Triangulation:
tri = Triangulation(np.ravel(u), np.ravel(v))

ax = plt.axes(projection="3d")
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap="jet", antialiased=True)

plt.show()
