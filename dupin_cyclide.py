import plotly.graph_objects as go
import numpy as np
from pathlib import Path

# https://en.wikipedia.org/wiki/Dupin_cyclide

# parameters
# a, b are semi-major and semi-minor axes
# d can be considered as the average radius of the generating spheres
a, b, d = 1, 0.98, 0.3

# c is the linear eccentricity of the ellipse
c = np.sqrt(a**2 - b**2)

u, v = np.mgrid[0 : 2 * np.pi : 100j, 0 : 2 * np.pi : 100j]
x = (d * (c - a * np.cos(u) * np.cos(v)) + b**2 * np.cos(u)) / (
    a - c * np.cos(u) * np.cos(v)
)
y = b * np.sin(u) * (a - d * np.cos(v)) / (a - c * np.cos(u) * np.cos(v))
z = b * np.sin(v) * (c * np.cos(u) - d) / (a - c * np.cos(u) * np.cos(v))

fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])

# Set layout and axis labels
fig.update_layout(
    title="Diagram",
    scene=dict(
        xaxis_title="X",
        yaxis_title="Y",
        zaxis_title="Z",
    ),
)

# Save plot as HTML file
fig.write_html(
    Path(__file__).stem + "_plot.html",
    full_html=False,
)
fig.show()
