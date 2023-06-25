"use strict";

document.addEventListener("DOMContentLoaded", () => {
  let mode = localStorage.getItem("mode");
  if (mode === null) {
    localStorage.setItem("mode", "dark");
  }
});

document.getElementById("btnSwitch").addEventListener("click", () => {
  // if (document.documentElement.getAttribute("data-bs-theme") == "dark") {
  //   document.documentElement.setAttribute("data-bs-theme", "light");
  // } else {
  //   document.documentElement.setAttribute("data-bs-theme", "dark");
  // }

  if (localStorage.getItem("mode") === "dark") {
    document.documentElement.setAttribute("data-bs-theme", "light");
    localStorage.setItem("mode", "light");
  } else {
    document.documentElement.setAttribute("data-bs-theme", "dark");
    localStorage.setItem("mode", "dark");
  }
});
