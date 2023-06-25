function handleSubmit(event : Event)
{
    // base string
    let uri : string = "https://c3d.libretexts.org/CalcPlot3D/index.html?type=";

    // check what kind of equation it is
    if (z.checked)
    {
        uri += "z;z=" + encodeURI(equation_input.value);
    }
    else if (parametric.checked)
    {
        uri += "parametric;parametric=2;" + encodeURI(equation_input.value) + ";visible=true;umin=-2pi;umax=2pi;usteps=25;vmin=-2pi;vmax=2pi;vsteps=25;";

    }
    else if (implicit.checked)
    {
        uri += "implicit;equation=" + encodeURI(equation_input.value.replace("=", "~")) + ";cubes=16;visible=true;";
    }

    // clear the text submission box
    equation_input.value = "";

    // make new iframe to open calcplot3d
    let iframe = document.createElement("iframe");
    iframe.src = uri;
    iframe.width = "1200";
    iframe.height = "1000";

    // add it to the HTML and clear existing frames (if any)
    const node : HTMLElement = document.getElementById("iframe")!;
    node.innerHTML = "";
    node.appendChild(iframe);

    // stop page refresh
    event.preventDefault();

}

function changePlaceholder() {

    // format for equations
    // TODO: more robust syntax explanations
    if (z.checked)
    {
        equation_input.placeholder = "z=";
    }
    else if (parametric.checked)
    {
        equation_input.placeholder = "x=;y=;z=;";
    }
    else if (implicit.checked) {
        equation_input.placeholder = "f(x,y,z)";
    }
    else {
        equation_input.placeholder = "Select an equation type";
    }
}

// HTML elements on page
let z : HTMLInputElement = <HTMLInputElement> document.getElementById("z")!;
let parametric : HTMLInputElement = <HTMLInputElement> document.getElementById("parametric")!;
let implicit : HTMLInputElement = <HTMLInputElement> document.getElementById("implicit")!;
let equation_input : HTMLInputElement = <HTMLInputElement> document.getElementById("equation");
let equation_form : HTMLFormElement = <HTMLFormElement> document.getElementById("equation-form");
equation_form.addEventListener("submit", handleSubmit);
