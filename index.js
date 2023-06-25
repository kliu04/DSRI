"use strict";

document.addEventListener("DOMContentLoaded", () => {
  // hold the dark/light mode status in client (default is dark)
  let mode = localStorage.getItem("mode");
  if (mode === null) {
    localStorage.setItem("mode", "dark");
  }

  // adjust appropriate css element on every page
  if (localStorage.getItem("mode") === "dark") {
    document.documentElement.setAttribute("data-bs-theme", "dark");
  } else {
    document.documentElement.setAttribute("data-bs-theme", "light");
  }
});

document.getElementById("btnSwitch").addEventListener("click", () => {
  // switch the state
  if (localStorage.getItem("mode") === "dark") {
    document.documentElement.setAttribute("data-bs-theme", "light");
    localStorage.setItem("mode", "light");
  } else {
    document.documentElement.setAttribute("data-bs-theme", "dark");
    localStorage.setItem("mode", "dark");
  }
});
