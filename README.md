# DSRI 2023

## Project Structure

- The 2D folder contains all the static HTML for each 2D curve.
- The 3D folder contains all the static HTML for each 3D surface.
- The math folder has 2 subdirectories:
  
  **Note!** All parameters are replaced with the fixed value $a=101$, $b=97$, and $c=103$.
  
  - The 2D_solvers folder contains the code to generate the invariants from every curve on [Katie's Website](https://people.math.carleton.ca/~cingalls/studentProjects/Katie's%20Site/html/All%20Curves.html).

    - `parse.py` takes an equation copied from Katie's website and formats it for `M2`.
    - `solve_a.m2` and `solve_b.py` calculate the invariants for a given curve.
    - `wrapper.py` takes an equation in `M2` format and returns a dict with all invariants calculated.
    - `scraper.py` scrapes Katie's Website, runs `wrapper.py` on each curve and creates a file `parsed_data.json` with all the data.
    - `create_sites.py` takes `parsed_data.json` and creates the webpage for each site, using find and replace on `template.txt`, and then creates the `index.html` file from `index_template.txt`, listing each curve in a table.

      **Warning!** Running this file will overwrite any custom changes to any `HTML` files.

  - The 3D_solvers folder contains the code to generate the invariants from curves in the `surfaces.json` file.
    - The overall structure is similar to 2D above, with a few notable differences.
    - `surfaces.json` contains at least all equations and titles for each surface.
    - `run_solvers.py` generates all invariants for each surface in `surfaces.json` and adds the data to that file.
  - The static folder contains `JS` (light/dark mode, sorting tables using [sorttable](https://www.kryogenix.org/code/browser/sorttable/)) and `CSS` (overriding [Bootstrap 5.3](https://getbootstrap.com/)), as well as the help and info files.

## Acknowledgements

This project was made possible by the [Dean's Summer Research Internship](https://science.carleton.ca/students/undergraduate-resources/deans-summer-research-internships/) program at [Carleton University](https://carleton.ca/), [Dr. Colin Ingalls](https://people.math.carleton.ca/~cingalls/), [Dr. Nathan Grieve](https://sites.google.com/view/nathan-grieve), the [Desmos Calculator](https://www.desmos.com/calculator) for 2D images, and [CalcPlot3D](https://c3d.libretexts.org/CalcPlot3D/index.html) for 3D images, [KaTeX](https://katex.org/) for TeX support, [Macaulay2](http://www2.macaulay2.com/Macaulay2/), [SymPy](https://www.sympy.org/en/index.html), Katie Cunningham - who made the precursor to this site, and my partners Andrew Cameron and Dongxu Hu.

## Known Issues

Please get in touch or make a issue / pull request if you find any errors/want to improve the site!

- Incorrect computation of invariants for Ranunculoid.
- Incorrect computation of Delta Invariant.
- A web framework like `Flask` or `Django` can improve the templates from just using search and replace.
