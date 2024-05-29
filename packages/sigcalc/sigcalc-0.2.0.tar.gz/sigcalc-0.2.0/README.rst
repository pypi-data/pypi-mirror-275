.. *****************************************************************************
..
.. sigcalc, significant figures calculations
..
.. Copyright 2023-2024 Jeremy A Gray <gray@flyquackswim.com>.
..
.. All rights reserved.
..
.. SPDX-License-Identifier: GPL-3.0-or-later
..
.. *****************************************************************************

=========
 sigcalc
=========

Sigcalc is a python module for expressing quantities with significant
figures and performing calculations on quantities based on the rules
of significant figures.

..
   .. image:: https://badge.fury.io/py/sigcalc.svg
      :target: https://badge.fury.io/py/sigcalc
      :alt: PyPI Version
   .. image:: https://readthedocs.org/projects/sigcalc/badge/?version=latest
      :target: https://sigcalc.readthedocs.io/en/latest/?badge=latest
      :alt: Documentation Status

Installation
============

Install sigcalc with pip::

  pip install sigcalc

or with poetry::

  poetry add sigcalc

``sigcalc`` depends on the internal ``decimal``
`module <https://docs.python.org/3/library/decimal.html>`_
for arithmetic and `mpmath <https://mpmath.org/>`_ for transcendental
and other functions.

Usage
=====

Import the ``Quantity`` class::

  >>> from sigcalc import Quantity
  >>> from decimal import getcontext
  >>> getcontext().prec = 28

Create ``Quantity`` objects as necessary::

  >>> a = Quantity("3.14", "3")
  >>> b = Quantity("2.72", "3")

The precision of the underlying ``decimal`` context should adjust
automatically to contain the number of digits specified or the number
of significant figures, within the limits of the ``decimal`` module.

Alternatively, create a ``Quantity`` object from a ``Decimal``::

  >>> a = Quantity.from_decimal("3.14")
  >>> b = Quantity("3.14", "3")
  >>> a == b
  True

The resulting significant figures is derived from the places in the
specified value.

Or generate randomly over a range::

  >>> a = Quantity.random("273.15", "373.15")

which is helpful for generating exercises for classes.

Arithmetic for ``Quantity`` objects is implemented on the usual magic
methods::

  >>> from sigcalc import Quantity
  >>> from decimal import getcontext
  >>> from decimal import ROUND_HALF_EVEN
  >>> getcontext().prec = 28
  >>> getcontext().rounding = ROUND_HALF_EVEN
  >>> a = Quantity("3.14", "3")
  >>> b = Quantity("2.72", "3")
  >>> a + b
  Quantity("5.86", "3")
  >>> a - b
  Quantity("0.42", "2")
  >>> a * b
  Quantity("8.5408", "3")
  >>> a / b
  Quantity("1.154411764705882352941176471", "3")
  >>> abs(a)
  Quantity("3.14", "3")
  >>> -a
  Quantity("-3.14", "3")
  >>> +a
  Quantity("3.14", "3")

Beware that rounding is not performed during calculations and that
reported significant figures for calculated values are for the
unrounded value.  For example, a calculation that resulted in a result
of ``Quantity("99.9", "3")`` could round to ``Quantity("100.0",
"4")``, depending on the current rounding mode.

Note that ``__floordiv__`` is not implemented as it is not useful for
significant figures calculations::

  >>> a // b
  Traceback (most recent call last):
  TypeError: unsupported operand type(s) for //: 'Quantity' and 'Quantity'

Comparisons behave as expected for real numbers, with the exception
equality and significance.  Since quantities with different
significance have different meanings, they are not equal as quantity
objects::

  >>> from sigcalc import Quantity
  >>> a = Quantity("3.135", "3")
  >>> b = Quantity("3.135", "4")
  >>> c = Quantity("3.145", "3")
  >>> a == a
  True
  >>> a == b
  False
  >>> a != b
  True
  >>> a < b
  False
  >>> a <= b
  False

Equal constants should be equal regardless of the significant figures
of the instance.

Rounding affects comparisons as well::

  >>> from decimal import ROUND_HALF_EVEN
  >>> from decimal import ROUND_HALF_UP
  >>> from decimal import getcontext
  >>> getcontext().rounding = ROUND_HALF_EVEN
  >>> a < c
  False
  >>> a == c
  True
  >>> a <= c
  True
  >>> getcontext().rounding = ROUND_HALF_UP
  >>> a < c
  True
  >>> a == c
  False
  >>> a <= c
  True

Rounding and output are tied together.  Typically, rounding is
unnecessary except for output but is available::

  >>> a = Quantity("3.14", "2")
  >>> a.round()
  Quantity("3.1", "2")
  >>> a
  Quantity("3.14", "2")

Rounding constants has no effect::

  >>> a = Quantity("3.145", "3", constant=True)
  >>> a.round()
  Quantity("3.145", "28", constant=True)

String output uses the underlying ``decimal`` module's string output
after rounding to the correct significant figures::

  >>> from decimal import ROUND_HALF_EVEN
  >>> from decimal import ROUND_HALF_UP
  >>> from decimal import getcontext
  >>> a = Quantity("3.145", "3")
  >>> getcontext().rounding = ROUND_HALF_UP
  >>> str(a)
  '3.15'
  >>> getcontext().rounding = ROUND_HALF_EVEN
  >>> str(a)
  '3.14'

The rounding mode is controlled by the ``decimal`` module contexts and
context managers.  The default rounding mode for the ``decimal``
module is ``decimal.ROUND_HALF_EVEN`` while the rounding used in most
textbook discussions of significant figures is
``decimal.ROUND_HALF_UP``, so beware.

Likewise with formatting::

  >>> getcontext().rounding = ROUND_HALF_UP
  >>> format(a, ".2e")
  '3.15e+0'
  >>> getcontext().rounding = ROUND_HALF_EVEN
  >>> format(b, ".2e")
  '3.14e+0'

Power and Square Root Functions
-------------------------------

The power and square root (``__pow__()`` and ``sqrt()``) functions and
are implemented as wrappers around the appropriate functions from
``decimal.Decimal``, calculating results based on the ``value`` of a
``Quantity`` combined with the correct significant figures, following
the "significance in, significance out" rule for both functions.

Exponential and Logarithmic Functions
-------------------------------------

The exponential and logarithmic (``exp()``, ``exp10()``, ``ln()``, and
``log10()``) functions are implemented as wrappers around the
corresponding functions from ``decimal`` to calculate the ``value`` of
a ``Quantity`` combined with the correct significant figures.
Abscissa digits are treated as placeholders so a logarithm will
increase significance by the number of significant abscissa digits;
exponentials will decrease the significance by the number of
significant abscissa digits.  Consequently, if a ``Quantity`` has
significant figures less than or equal to the number of abscissa
digits, a ``RuntimeWarning`` will be raised and a ``Quantity`` with
zero significant figures will be returned.  See the references for
more information.

Transcendental Functions
------------------------

The transcendental functions and their inverses are implemented as
wrappers around the appropriate functions from ``mpmath``, calculating
results based on the ``value`` of a ``Quantity`` combined with the
correct significant figures, following the "significance in,
significance out" rule.

Hyperbolic Functions
--------------------

The hyperbolic functions and their inverses are implemented as
wrappers around the appropriate functions from ``mpmath``, calculating
results based on the ``value`` of a ``Quantity`` combined with the
correct significant figures, following the "significance in,
significance out" rule.

References
==========

``sigcalc`` implements significant figures calculations as commonly
described in high school and undergraduate chemistry and physics
textbooks, examples of which may be found at:

1. `Significant Figures at Wikipedia <https://en.wikipedia.org/wiki/Significant_figures>`_
2. `Significance Arithmetic at Wikipedia <https://en.wikipedia.org/wiki/Significance_arithmetic>`_
3. Myers, R.T.; Tocci, S.; Oldham, K.B., Holt Chemistry, Holt, Rinehart and Winston: 2006.
4. `"How many significant figures in 0.0" <https://math.stackexchange.com/questions/2149316/>`_

Thanks to the developers of Python's ``decimal``
`module <https://docs.python.org/3/library/decimal.html>`_,
the `mpmath <https://mpmath.org/>`_ library, and the
`hypothesis <https://hypothesis.readthedocs.io/>`_ testing library,
without which, this would be a much smaller and less functional
library.

Thanks also to LibreTexts Mathematics for their reference on `hyperbolic functions <https://math.libretexts.org/Courses/Monroe_Community_College/MTH_211_Calculus_II/Chapter_6%3A_Applications_of_Integration/6.9%3A_Calculus_of_the_Hyperbolic_Functions>`_.

Remember, calculating with significant figures is not a substitute for
repetition of measurements and proper statistical analysis.

Copyright and License
=====================

SPDX-License-Identifier: `GPL-3.0-or-later <https://spdx.org/licenses/GPL-3.0-or-later.html>`_

sigcalc, significant figures calculations

Copyright (C) 2023-2024 `Jeremy A Gray <gray@flyquackswim.com>`_.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see https://www.gnu.org/licenses/.

Author
======

`Jeremy A Gray <gray@flyquackswim.com>`_
