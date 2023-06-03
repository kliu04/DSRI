import sympy as sym
from sympy.solvers import solveset
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path

# solve the equation with sympy
x, y, z = sym.symbols("x y z")
eq = sym.Eq(x**2 + y**2 + z**2, 0)

surfaces = []

for e in solveset(eq, z):
    x = np.arange(-10, 10, 0.1)
    y = np.arange(-10, 10, 0.1)
    x, y = np.meshgrid(x, y)
    z = str(e)
    z = z.replace("sqrt", "np.sqrt")
    surfaces.append(go.Surface(x=x, y=y, z=eval(z)))

fig = make_subplots()
for item in surfaces:
    fig.add_trace(item)

fig.update_layout(
    title="Diagram",
    scene=dict(
        xaxis_title="X",
        yaxis_title="Y",
        zaxis_title="Z",
    ),
)

fig.write_html(
    Path(__file__).stem + "_plot.html",
    full_html=False,
)
fig.show()
