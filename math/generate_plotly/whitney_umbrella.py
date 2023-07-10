import plotly.graph_objects as go
import numpy as np
from pathlib import Path


# u, v are parameters
u, v = np.mgrid[-1:1:0.01, -1:1:0.01]

# set x, y, z
x = u * v
y = u
z = v * v

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
    rf"3D/plotly_plots/{Path(__file__).stem}_plot.html",
    full_html=False,
)
# fig.show()
