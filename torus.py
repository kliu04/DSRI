import numpy as np
import plotly.graph_objects as go
from pathlib import Path

# Generate torus surface data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
u, v = np.meshgrid(u, v)
R = 3  # Major radius
r = 1  # Minor radius
x = (R + r * np.cos(v)) * np.cos(u)
y = (R + r * np.cos(v)) * np.sin(u)
z = r * np.sin(v)

# Create 3D surface plot
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
