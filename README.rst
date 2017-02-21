===============================================
Fitting an Ellipse to a Set of Data Points
===============================================

This python program fits an  ellipse through a given set of points.
This ellips is optimal in the least squares sense.

The code is documented in ``fit_ellipse.pdf``.

  * The source is in ``fit_ellipse.Pnw``
  * with `Pweave <http://mpastell.com/pweave/>`_ you can get
    ``fit_ellipse.rst`` as documentation. Just run ``pweave -f rst
    fit_ellipse.Pnw``
  * To get the python file, run ``ptangle fit_ellipse.Pnw``
  * For the pdf file, I ran ``rst2latex fit_ellipse.rst >
    fit_ellipse.tex`` and I compiled the tex file with ``pdflatex``.

In case you would like to contribute, please update only
``fit_ellipse.Pnw`` as this is the source of both the python file and
the documentation.

I would have liked to make the documentation viewable on github right
away, but (as far as I know) github does not support mathjax. Thus, as
a substitute, I provide the pdf file.
