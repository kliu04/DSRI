import plotly.graph_objects as go
import numpy as np
from pathlib import Path

# https://mathworld.wolfram.com/EightSurface.html

# u, v are parameters
u, v = np.mgrid[-10:10:0.1, -10:10:0.1]

# set x, y, z
x = np.cos(u) * np.sin(2 * v)
y = np.sin(u) * np.sin(2 * v)
z = np.sin(v)

fig = go.Figure(data=go.Surface(x=x, y=y, z=z))

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
