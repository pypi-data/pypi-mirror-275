# ******************************************************************************
#
# sigcalc, significant figures calculations
#
# Copyright 2023-2024 Jeremy A Gray <gray@flyquackswim.com>.
#
# All rights reserved.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# ******************************************************************************

"""sigcalc constants."""

from decimal import Decimal

from .quantity import Quantity

pi = Quantity(
    Decimal("3.1415926535897932384626433832795028841971"),
    constant=True,
)
"""pi, as a constant, with forty decimal digits.

See `"How Many Decimals of Pi Do We Really Need?" <https://www.jpl.nasa.gov/edu/news/2016/3/16/how-many-decimals-of-pi-do-we-really-need/>`_ if you think you need more.
"""  # noqa: E501

e = Quantity(
    Decimal("2.7182818284590452353602874713526624977572"),
    constant=True,
)
"""Euler's number, as a constant, with forty decimal digits.

See `"How Many Decimals of Pi Do We Really Need?" <https://www.jpl.nasa.gov/edu/news/2016/3/16/how-many-decimals-of-pi-do-we-really-need/>`_ if you think you need more.
"""  # noqa: E501
