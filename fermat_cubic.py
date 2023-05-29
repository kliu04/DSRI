import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import plotly.graph_objects as go

plt.style.use("_mpl-gallery")

# Make data
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = np.cbrt(-(X**3) - Y**3 + 1)

fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z)])

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
