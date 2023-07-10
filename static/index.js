"use strict";

document.addEventListener("DOMContentLoaded", () => {
  // hold the dark/light theme status in client (default is dark)
  let theme = localStorage.getItem("theme");
  if (theme === null) {
    localStorage.setItem("theme", "dark");
  }

  // adjust appropriate css element on every page
  if (localStorage.getItem("theme") === "dark") {
    document.documentElement.setAttribute("data-bs-theme", "dark");
  } else {
    document.documentElement.setAttribute("data-bs-theme", "light");
  }

  window.MathJax = {
    output: {
      displayAlign: "left",
      font: "mathjax-tex",
      displayOverflow: "linebreak",
      linebreaks: {
        inline: true,
        width: "100%",
        lineleading: 0.2,
        LinebreakVisitor: null,
      },
    },
  };
});

document.getElementById("btnSwitch").addEventListener("click", () => {
  // switch the state
  if (localStorage.getItem("theme") === "dark") {
    document.documentElement.setAttribute("data-bs-theme", "light");
    localStorage.setItem("theme", "light");
  } else {
    document.documentElement.setAttribute("data-bs-theme", "dark");
    localStorage.setItem("theme", "dark");
  }
});
