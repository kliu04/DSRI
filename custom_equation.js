"use strict";
function handleSubmit(event) {
    let uri = "https://c3d.libretexts.org/CalcPlot3D/index.html?type=";
    if (z.checked) {
        uri += "z;z=" + encodeURI(equation_input.value);
    }
    else if (parametric.checked) {
        uri += "parametric;parametric=2;" + encodeURI(equation_input.value) + ";visible=true;umin=-2pi;umax=2pi;usteps=25;vmin=-2pi;vmax=2pi;vsteps=25;";
    }
    else if (implicit.checked) {
        uri += "implicit;equation=" + encodeURI(equation_input.value.replace("=", "~")) + ";cubes=16;visible=true;";
    }
    equation_input.value = "";
    console.log(uri);
    event.preventDefault();
    let iframe = document.createElement("iframe");
    iframe.src = uri;
    iframe.width = "1200";
    iframe.height = "1000";
    const node = document.getElementById("iframe");
    node.innerHTML = "";
    node.appendChild(iframe);
}
function changePlaceholder() {
    if (z.checked) {
        equation_input.placeholder = "z=";
    }
    else if (parametric.checked) {
        equation_input.placeholder = "x=;y=;z=;";
    }
    else if (implicit.checked) {
        equation_input.placeholder = "f(x,y,z)";
    }
    else {
        equation_input.placeholder = "Select an equation type";
    }
}
let z = document.getElementById("z");
let parametric = document.getElementById("parametric");
let implicit = document.getElementById("implicit");
let equation_input = document.getElementById("equation");
let equation_form = document.getElementById("equation-form");
equation_form.addEventListener("submit", handleSubmit);
