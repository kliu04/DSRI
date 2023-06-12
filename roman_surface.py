import numpy as np
import plotly.graph_objects as go
from pathlib import Path

# https://c3d.libretexts.org/CalcPlot3D/index.html?type=implicit;equation=x^2*y^2+y^2*z^2+z^2*x^2-a^2*x*y*z~0;cubes=16;visible=false;fixdomain=false;xmin=-2;xmax=2;ymin=-2;ymax=2;zmin=-2;zmax=2;alpha=-1;hidemyedges=false;view=0;format=normal;constcol=rgb(255,0,0)&type=parametric;parametric=2;x=a^2*cos(u)*cos(v)*sin(v);y=a^2*sin(u)*cos(v)*sin(v);z=a^2*cos(u)*sin(u)*sin(v)*sin(v);visible=true;umin=0;umax=2pi;usteps=30;vmin=0;vmax=pi;vsteps=15;alpha=-1;hidemyedges=false;view=0;format=normal;constcol=rgb(255,0,0)&type=slider;slider=a;value=1;steps=100;pmin=-2;pmax=2;repeat=true;bounce=true;waittime=1;careful=false;noanimate=false;name=-1&type=window;hsrmode=0;nomidpts=true;anaglyph=-1;center=8.236391035463319,4.755282581475766,3.0901699437494745,1;focus=0,0,0,1;up=0,0,2,1;transparent=false;alpha=140;twoviews=false;unlinkviews=false;axisextension=0.7;shownormals=false;shownormalsatpts=false;xaxislabel=x;yaxislabel=y;zaxislabel=z;edgeson=true;faceson=true;showbox=true;showaxes=true;showticks=true;perspective=true;centerxpercent=0.5;centerypercent=0.5;rotationsteps=30;autospin=true;xygrid=false;yzgrid=false;xzgrid=false;gridsonbox=true;gridplanes=false;gridcolor=rgb(128,128,128);xmin=-2;xmax=2;ymin=-2;ymax=2;zmin=-2;zmax=2;xscale=1;yscale=1;zscale=1;zcmin=-4;zcmax=4;xscalefactor=1;yscalefactor=1;zscalefactor=1;tracemode=0;keep2d=false;zoom=1.716

theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)
theta, phi = np.meshgrid(theta, phi)
r = 1  # parameter - not fully implemented
x = r**2 * np.cos(theta) * np.cos(phi) * np.sin(phi)
y = r**2 * np.sin(theta) * np.cos(phi) * np.sin(phi)
z = r**2 * np.cos(theta) * np.sin(theta) * np.cos(phi) ** 2

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
