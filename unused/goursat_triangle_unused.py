import numpy as np
from skimage import measure
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import plotly
import chart_studio.plotly as py
import plotly.tools as tls
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
from pathlib import Path


def f(x, y, z):
    return x**2 + y**2 + z**2 - 1


xl = np.linspace(-3, 3, 50)
X, Y, Z = np.meshgrid(xl, xl, xl)
F = f(X, Y, Z)

verts, faces, normals, values = measure.marching_cubes(
    F, 0, spacing=[np.diff(xl)[0]] * 3
)
verts -= 3

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2], cmap="jet", lw=0)

plotly_fig = tls.mpl_to_plotly(fig)
plotly.offline.plot(plotly_fig, filename="plotly version of an mpl figure")

plotly_fig.write_html(
    Path(__file__).stem + "_plot.html",
    full_html=False,
)
plotly_fig.show()
