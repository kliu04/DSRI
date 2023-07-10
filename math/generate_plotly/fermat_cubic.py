import numpy as np
from pathlib import Path
import plotly.graph_objects as go


# Make data
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
x, y = np.meshgrid(x, y)
z = np.cbrt(-(x**3) - y**3 + 1)

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
    rf"3D/plotly_plots/{Path(__file__).stem}_plot.html",
    full_html=False,
)
# fig.show()
