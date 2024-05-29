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

"""Constant tests."""

from decimal import Decimal

import sigcalc


def test_properties_of_e():
    """Should have the correct properties."""
    assert sigcalc.e.value == Decimal("2.7182818284590452353602874713526624977572")
    assert sigcalc.e.figures == Decimal("41")
    assert sigcalc.e.constant is True


def test_properties_of_pi():
    """Should have the correct properties."""
    assert sigcalc.pi.value == Decimal("3.1415926535897932384626433832795028841971")
    assert sigcalc.pi.figures == Decimal("41")
    assert sigcalc.pi.constant is True
