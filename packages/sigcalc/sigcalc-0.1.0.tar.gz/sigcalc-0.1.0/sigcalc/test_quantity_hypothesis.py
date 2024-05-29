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

"""Quantity hypothesis tests."""

import math
from decimal import ROUND_05UP
from decimal import ROUND_CEILING
from decimal import ROUND_DOWN
from decimal import ROUND_FLOOR
from decimal import ROUND_HALF_DOWN
from decimal import ROUND_HALF_EVEN
from decimal import ROUND_HALF_UP
from decimal import ROUND_UP
from decimal import Decimal
from decimal import InvalidOperation
from decimal import getcontext

import mpmath
import pytest
from hypothesis import HealthCheck
from hypothesis import assume
from hypothesis import given
from hypothesis import settings
from hypothesis import strategies as st
from hypothesis.strategies import composite

from sigcalc import Quantity
from sigcalc import pi

# Reusable decimal constants.
NegThousand = Decimal("-1000")
NegTen = Decimal("-10")
NegOne = Decimal("-1")
Zero = Decimal("0")
One = Decimal("1")
Two = Decimal("2")
Ten = Decimal("10")
Hundred = Decimal("100")
Thousand = Decimal("1000")


@composite
def quantities(draw, min_value=None, max_value=None):
    """Generate quantities."""
    return Quantity(
        draw(
            st.decimals(
                allow_nan=False,
                allow_infinity=False,
                min_value=min_value,
                max_value=max_value,
            )
        ),
        draw(
            st.integers(
                min_value=1,
                max_value=100,
            )
        ),
        draw(st.booleans()),
    )


@composite
def rounding(draw):
    """Generate a rounding mode."""
    return draw(
        st.sampled_from(
            [
                ROUND_CEILING,
                ROUND_DOWN,
                ROUND_FLOOR,
                ROUND_HALF_DOWN,
                ROUND_HALF_EVEN,
                ROUND_HALF_UP,
                ROUND_UP,
                ROUND_05UP,
            ]
        )
    )


@given(
    st.decimals(
        allow_nan=False,
        allow_infinity=False,
    ),
)
def test___init__raises_without_figures_nonconstant(value):
    """Should raise ``TypeError`` without ``figures`` if not constant."""
    with pytest.raises(TypeError):
        Quantity(value)


@given(
    st.decimals(
        allow_nan=False,
        allow_infinity=False,
    ),
    st.integers(
        min_value=1,
        max_value=100,
    ),
)
def test___init__creates_quantity_objects(value, figures):
    """Should create ``Quantity`` objects."""
    q = Quantity(value, Decimal(str(figures)))
    assert q.value == value
    assert q.figures == Decimal(str(figures))
    assert q.constant is False


@given(
    st.decimals(
        allow_nan=False,
        allow_infinity=False,
    ),
    st.integers(
        min_value=1,
        max_value=100,
    ),
)
def test___init__creates_quantity_constants(value, figures):
    """Should create ``Quantity`` objects."""
    q = Quantity(value, Decimal(str(figures)), constant=True)
    assert q.value == value
    assert q.figures == getcontext().prec
    assert q.constant is True


@given(quantities(), rounding())
def test_equality_hypothesis(q, r):
    """Should order ``Quantity`` objects."""
    getcontext().rounding = r
    assert q == q
    assert q <= q
    assert q >= q
    assert not q != q


@given(quantities(), rounding())
def test_ordering_hypothesis(q, r):
    """Should order ``Quantity`` objects."""
    # Zeroes satisfy equality.
    if r == ROUND_DOWN:
        assume(abs(q.value) >= 1)
    else:
        assume(q.value > 0)
    getcontext().rounding = r
    assert q + abs(q) > q
    assert q > q - abs(q)
    assert q < q + abs(q)
    assert q - abs(q) < q


@given(quantities(), rounding())
def test_equality_different_precision_hypothesis(q, r):
    """Should order ``Quantity`` objects."""
    getcontext().rounding = r
    if q.figures == getcontext().prec:
        p = Quantity(q.value, q.figures - One, False)
    else:
        p = Quantity(q.value, q.figures + One, q.constant)

    assert q != p


@given(quantities(), rounding())
def test_almost_equal_self_hypothesis(one, r):
    """Should be almost equal to self."""
    assert one.almosteq(one)


@given(
    quantities(
        min_value=Zero,
        max_value=Ten,
    ),
    rounding(),
)
def test_almost_equal_pass_eps_hypothesis(one, r):
    """Should pass both epsilons."""
    delta = mpmath.mpmathify("1e-25")
    abs_eps = "1"
    rel_eps = "1"

    two = Quantity(
        one.value + delta,
        one.figures,
        constant=one.constant,
    )
    assert one.almosteq(two, rel_eps=rel_eps)
    assert one.almosteq(two, abs_eps=abs_eps)
    assert one.almosteq(two, rel_eps=rel_eps, abs_eps=abs_eps)


@given(quantities(), quantities(), rounding())
def test_almost_equal_hypothesis(one, two, r):
    """Should determine approximate equality."""
    if one.figures == two.figures:
        eps = pow(mpmath.mpf("2"), -getcontext().prec + 4)
        if mpmath.mpmathify(abs(one.value - two.value)) > eps:
            assert not one.almosteq(two)
        else:
            assert one.almosteq(two)
    else:
        assert not one.almosteq(two)


@given(quantities(), rounding())
def test_abs_hypothesis(q, r):
    """Should calculate absolute value of ``Quantity`` objects."""
    getcontext().rounding = r
    p = Quantity(abs(q.value), q.figures, q.constant)
    assert abs(q) == p
    assert abs(abs(q)) == p


@given(quantities(), rounding())
def test_neg_hypothesis(q, r):
    """Should negate ``Quantity`` objects."""
    getcontext().rounding = r
    assert -(-q) == q


@given(quantities(), rounding())
def test_pos_hypothesis(q, r):
    """Should return ``Quantity`` objects."""
    getcontext().rounding = r
    p = Quantity(q.value, q.figures, q.constant)
    assert +q == q
    assert ++q == q
    assert +q == p


@given(quantities(), rounding())
def test_round_hypothesis(q, r):
    """Should round ``Quantity`` objects."""
    getcontext().rounding = r
    assert q.round() == q.round().round()


@given(quantities(), rounding())
def test_additive_identity_hypothesis(q, r):
    """``Quantity`` objects should have an additive identity."""
    getcontext().rounding = r
    id = Quantity("0", "1", True)
    assert q + id == q
    assert id + q == q
    assert id + q + id == q


@given(quantities(), rounding())
def test_subtractive_identity_hypothesis(q, r):
    """``Quantity`` objects should have a subtractive identity."""
    getcontext().rounding = r
    id = Quantity("0", "1", True)
    assert q - id == q


@given(quantities(), rounding())
def test_additive_inverse_hypothesis(q, r):
    """``Quantity`` objects should have an additive inverse."""
    getcontext().rounding = r
    # assert q - q == Quantity("0", q.figures, q.constant)
    assert q + q - q == q
    assert q - q + q == q


@given(quantities(), rounding())
def test_multiplicative_identity_hypothesis(q, r):
    """``Quantity`` objects should have a multiplicative identity."""
    getcontext().rounding = r
    id = Quantity("1", "1", True)
    assert q * id == q
    assert id * q == q
    assert id * q * id == q

    id = Quantity("1", q.figures)
    assert q * id == q
    assert id * q == q
    assert id * q * id == q


@given(quantities(), rounding())
def test_divisive_identity_hypothesis(q, r):
    """``Quantity`` objects should have a divisive identity."""
    getcontext().rounding = r
    id = Quantity("1", "1", True)
    assert q / id == q

    id = Quantity("1", q.figures)
    assert q / id == q


@given(quantities(), rounding(), st.booleans())
def test_constant_setter_hypothesis(q, r, c):
    """Should set the ``constant`` attribute."""
    getcontext().rounding = r
    q.constant = c
    assert q.constant is c


# Exponential function tests.
@given(quantities(), rounding())
def test_exp_hypothesis(q, r):
    """Should calculate the exponential of ``Quantity`` objects."""
    # Really need to round-trip with ln, since this repeats the tested
    # logic for significance.

    # Avoid decimal overflow.
    assume(q.value < Thousand)
    assume(q.value > NegThousand)

    # Avoid ambiguous zero warning.
    assume(q.value != Zero)

    # Ensure sufficient precision.
    assume(q.figures > (q.value.adjusted() + One))

    getcontext().rounding = r

    actual = q.exp()

    figures = q.figures

    if q.constant:
        expected = Quantity(
            q.value.exp(),
            constant=q.constant,
        )
    elif abs(q.value) >= One:
        # Magnitude of abscissa is greater than one; chop abscissa places.
        figures = q.figures - (q.value.adjusted() + One)

    expected = Quantity(
        q.value.exp(),
        figures,
        constant=q.constant,
    )

    assert actual.almosteq(expected)
    assert actual.constant == expected.constant


@given(
    st.integers(
        min_value=1,
        max_value=100,
    ),
    st.booleans(),
    rounding(),
)
def test_exp_ambiguous_zero_hypothesis(figures, constant, r):
    """Should warn on ambiguous zero input."""
    getcontext().rounding = r

    q = Quantity("0", figures, constant)
    expected = Quantity("1", "0")

    with pytest.warns(RuntimeWarning):
        actual = q.exp()

    assert actual == expected


@settings(
    suppress_health_check=[
        HealthCheck.filter_too_much,
        HealthCheck.too_slow,
    ],
)
@given(quantities(), rounding())
def test_exp_insufficient_precision_hypothesis(q, r):
    """Should warn on insufficient precision."""
    # Avoid decimal overflow.
    assume(q.value < Thousand)
    assume(q.value > NegThousand)

    # Avoid ambiguous zero warning.
    assume(q.value != Zero)

    # Ensure insufficient precision.
    assume(q.figures <= (q.value.adjusted() + One))

    getcontext().rounding = r

    with pytest.warns(RuntimeWarning):
        actual = q.exp()

    expected = Quantity(
        q.value.exp(),
        Zero,
    )

    assert actual.almosteq(expected)
    assert actual.constant == expected.constant


@given(quantities(), rounding())
def test_exp10_hypothesis(q, r):
    """Should calculate the base 10 exponential of ``Quantity`` objects."""
    # Really need to round-trip with ln, since this repeats the tested
    # logic for significance.

    # Avoid decimal overflow.
    assume(q.value < Thousand)
    assume(q.value > NegThousand)

    # Avoid ambiguous zero warning.
    assume(q.value != Zero)

    # Ensure sufficient precision.
    assume(q.figures > (q.value.adjusted() + One))

    getcontext().rounding = r

    actual = q.exp10()

    figures = q.figures

    if q.constant:
        expected = Quantity(
            pow(Ten, q.value),
            constant=q.constant,
        )
    elif abs(q.value) >= One:
        # Magnitude of abscissa is greater than one; chop abscissa places.
        figures = q.figures - (q.value.adjusted() + One)

    expected = Quantity(
        pow(Ten, q.value),
        figures,
        constant=q.constant,
    )

    assert actual.almosteq(expected)
    assert actual.constant == expected.constant


@given(
    st.integers(
        min_value=1,
        max_value=100,
    ),
    st.booleans(),
    rounding(),
)
def test_exp10_ambiguous_zero_hypothesis(figures, constant, r):
    """Should warn on ambiguous zero input."""
    getcontext().rounding = r

    q = Quantity("0", figures, constant)
    expected = Quantity("1", "0")

    with pytest.warns(RuntimeWarning):
        actual = q.exp10()

    assert actual == expected


@settings(
    suppress_health_check=[
        HealthCheck.filter_too_much,
        HealthCheck.too_slow,
    ],
)
@given(quantities(), rounding())
def test_exp10_insufficient_precision_hypothesis(q, r):
    """Should warn on insufficient precision."""
    # Avoid decimal overflow.
    assume(q.value < Thousand)
    assume(q.value > NegThousand)

    # Avoid ambiguous zero warning.
    assume(q.value != Zero)

    # Ensure insufficient precision.
    assume(q.figures <= (q.value.adjusted() + One))

    getcontext().rounding = r

    with pytest.warns(RuntimeWarning):
        actual = q.exp10()

    expected = Quantity(
        pow(Ten, q.value),
        Zero,
    )

    assert actual.almosteq(expected)
    assert actual.constant == expected.constant


@given(quantities(), quantities(), rounding())
def test_power_hypothesis(base, exp, r):
    """Should calculate powers of ``Quantity`` objects."""
    # Avoid indeterminancy of zeroes.
    assume(base.value != Zero)

    # Avoid overflow/underflow.
    assume(abs(base.value) < Thousand)
    assume(abs(exp.value) < Hundred)

    getcontext().rounding = r

    if base.value < Zero and Decimal(int(exp.value)) != exp.value:
        with pytest.raises(InvalidOperation):
            actual = pow(base, exp)
    else:
        actual = pow(base, exp)

        if base.constant:
            expected = Quantity(
                pow(base.value, exp.value),
                constant=base.constant,
            )
        else:
            expected = Quantity(
                pow(base.value, exp.value),
                base.figures,
            )

        assert actual.almosteq(expected)
        assert actual.constant == expected.constant


@given(quantities(), rounding())
def test_sqrt_hypothesis(q, r):
    """Should calculate the square root of ``Quantity`` objects."""
    # Avoid domain problems.
    assume(q.value > Zero)

    getcontext().rounding = r
    e = q.sqrt()

    assert q.value.sqrt() == e.value
    assert q.figures == e.figures
    assert q.constant == e.constant


# Logarithmic function tests.
@given(quantities(), rounding())
def test_ln_hypothesis(q, r):
    """Should calculate the natural logarithm of ``Quantity`` objects."""
    # Avoid logarithm domain problems.
    assume(q.value > Zero)
    assume(not math.isnan(q.value))

    getcontext().rounding = r
    actual = q.ln()

    # Calculate significant figures.
    if not q.constant and (abs(q.value) >= One.exp() or abs(q.value) <= NegOne.exp()):
        # Include abscissa digits.
        a = q.value.ln().adjusted() + 1
    else:
        # No abscissa digits.
        a = 0

    expected = Quantity(
        q.value.ln(),
        q.figures + a,
        q.constant,
    )

    assert actual.almosteq(expected)
    assert actual.constant == expected.constant


@given(quantities(), rounding())
def test_log10_hypothesis(q, r):
    """Should calculate the base 10 logarithm of ``Quantity`` objects."""
    # Avoid logarithm domain problems.
    assume(q.value > Zero)
    assume(not math.isnan(q.value))

    getcontext().rounding = r

    actual = q.log10()

    # Calculate significant figures.
    if not q.constant and (abs(q.value) >= Ten or abs(q.value) <= Decimal("0.1")):
        # Include abscissa digits.
        a = q.value.log10().adjusted() + One
    else:
        # No abscissa digits.
        a = Zero

    expected = Quantity(
        q.value.log10(),
        q.figures + a,
        q.constant,
    )

    assert actual.almosteq(expected)
    assert actual.constant == expected.constant


# Logarithmic/exponential round trip tests.
@given(quantities(), rounding())
def test_ln_exp_hypothesis(expected, mode):
    """Should round trip exponential of natural logarithm."""
    # Avoid logarithm domain problems.
    assume(expected.value > Zero)
    # Avoid ambiguous zero.
    assume(expected.value != One)

    # Set rounding context.
    getcontext().rounding = mode

    actual = expected.ln().exp()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(quantities(), rounding())
def test_exp_ln_hypothesis(expected, mode):
    """Should round trip natural logarithm of exponential."""
    # Avoid decimal overflow.
    assume(expected.value < Thousand)
    assume(expected.value > NegThousand)

    # Avoid ambiguous zero warning.
    assume(expected.value != Zero)

    # Ensure sufficient precision.
    assume(expected.figures > (expected.value.adjusted() + One))

    # Set rounding context.
    getcontext().rounding = mode

    actual = expected.exp().ln()

    assert actual.almosteq(expected, "1e-25")
    assert actual.constant == expected.constant


# Trigonometric function tests.
@given(quantities(), rounding())
def test_sin_hypothesis(q, r):
    """Should calculate the sine of ``Quantity`` objects."""
    e = q.sin()

    # Duplication; no need to test mpmath.
    assert (
        Decimal(mpmath.nstr(mpmath.sin(mpmath.mpmathify(q.value)), mpmath.mp.dps))
        == e.value
    )
    assert q.figures == e.figures
    assert q.constant == e.constant


@given(quantities(), rounding())
def test_asin_hypothesis(q, r):
    """Should calculate the inverse sine of ``Quantity`` objects."""
    assume(q.value >= -1 and q.value <= 1)
    e = q.asin()

    # Duplication; no need to test mpmath.
    assert (
        Decimal(mpmath.nstr(mpmath.asin(mpmath.mpmathify(q.value)), mpmath.mp.dps))
        == e.value
    )
    assert q.figures == e.figures
    assert q.constant == e.constant


@given(quantities(), rounding())
def test_asin_of_sin_hypothesis(expected, r):
    """Should return input."""
    assume(expected.value >= -pi.value / Two and expected.value <= pi.value / Two)
    actual = expected.sin().asin()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(quantities(), rounding())
def test_sin_of_asin_hypothesis(expected, r):
    """Should return input."""
    assume(expected.value >= -1 and expected.value <= 1)
    actual = expected.asin().sin()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(quantities(), rounding())
def test_cos_hypothesis(q, r):
    """Should calculate the cosine of ``Quantity`` objects."""
    e = q.cos()

    # Duplication; no need to test mpmath.
    assert (
        Decimal(mpmath.nstr(mpmath.cos(mpmath.mpmathify(q.value)), mpmath.mp.dps))
        == e.value
    )
    assert q.figures == e.figures
    assert q.constant == e.constant


@given(quantities(), rounding())
def test_acos_hypothesis(q, r):
    """Should calculate the inverse cosine of ``Quantity`` objects."""
    assume(q.value >= -1 and q.value <= 1)
    e = q.acos()

    # Duplication; no need to test mpmath.
    assert (
        Decimal(mpmath.nstr(mpmath.acos(mpmath.mpmathify(q.value)), mpmath.mp.dps))
        == e.value
    )
    assert q.figures == e.figures
    assert q.constant == e.constant


@given(quantities(), rounding())
def test_acos_of_cos_hypothesis(expected, r):
    """Should return input."""
    assume(expected.value >= Zero and expected.value <= pi.value)
    actual = expected.cos().acos()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(quantities(), rounding())
def test_cos_of_acos_hypothesis(expected, r):
    """Should return input."""
    assume(expected.value >= -1 and expected.value <= 1)
    actual = expected.acos().cos()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(quantities(), rounding())
def test_tan_hypothesis(q, r):
    """Should calculate the tangent of ``Quantity`` objects."""
    e = q.tan()

    # Duplication; no need to test mpmath.
    assert (
        Decimal(mpmath.nstr(mpmath.tan(mpmath.mpmathify(q.value)), mpmath.mp.dps))
        == e.value
    )
    assert q.figures == e.figures
    assert q.constant == e.constant


@given(quantities(), rounding())
def test_atan_hypothesis(q, r):
    """Should calculate the inverse tangent of ``Quantity`` objects."""
    e = q.atan()

    # Duplication; no need to test mpmath.
    assert (
        Decimal(mpmath.nstr(mpmath.atan(mpmath.mpmathify(q.value)), mpmath.mp.dps))
        == e.value
    )
    assert q.figures == e.figures
    assert q.constant == e.constant


@given(quantities(), rounding())
def test_atan_of_tan_hypothesis(expected, r):
    """Should return input."""
    assume(expected.value >= -pi.value / Two and expected.value <= pi.value / Two)
    actual = expected.tan().atan()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(quantities(), rounding())
def test_tan_of_atan_hypothesis(expected, r):
    """Should return input."""
    actual = expected.atan().tan()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(quantities(), rounding())
def test_csc_hypothesis(q, r):
    """Should calculate the cosecant of ``Quantity`` objects."""
    assume(q.value >= -pi.value and q.value <= pi.value)
    assume(q.value != Zero)

    actual = q.csc()
    expected = Quantity(
        Decimal(mpmath.nstr(mpmath.csc(mpmath.mpmathify(q.value)), mpmath.mp.dps)),
        q.figures,
        constant=q.constant,
    )

    assert actual == expected


@given(quantities(), rounding())
def test_acsc_hypothesis(q, r):
    """Should calculate the inverse cosecant of ``Quantity`` objects."""
    assume(q.value >= One or q.value <= NegOne)

    actual = q.acsc()
    expected = Quantity(
        Decimal(mpmath.nstr(mpmath.acsc(mpmath.mpmathify(q.value)), mpmath.mp.dps)),
        q.figures,
        constant=q.constant,
    )

    assert actual == expected


@given(quantities(), rounding())
def test_acsc_of_csc_hypothesis(expected, r):
    """Should return input."""
    assume(expected.value >= -pi.value / Two and expected.value <= pi.value / Two)
    assume(expected.value != Zero)

    actual = expected.csc().acsc()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(quantities(), rounding())
def test_csc_of_acsc_hypothesis(expected, r):
    """Should return input."""
    assume(expected.value <= -1 or expected.value >= 1)
    actual = expected.acsc().csc()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(quantities(), rounding())
def test_sec_hypothesis(q, r):
    """Should calculate the secant of ``Quantity`` objects."""
    assume(q.value >= Zero and q.value <= pi.value)
    assume(q.value != pi.value / Two)

    actual = q.sec()
    expected = Quantity(
        Decimal(mpmath.nstr(mpmath.sec(mpmath.mpmathify(q.value)), mpmath.mp.dps)),
        q.figures,
        constant=q.constant,
    )

    assert actual == expected


@given(quantities(), rounding())
def test_asec_hypothesis(q, r):
    """Should calculate the inverse secant of ``Quantity`` objects."""
    assume(q.value >= One or q.value <= NegOne)

    actual = q.asec()
    expected = Quantity(
        Decimal(mpmath.nstr(mpmath.asec(mpmath.mpmathify(q.value)), mpmath.mp.dps)),
        q.figures,
        constant=q.constant,
    )

    assert actual == expected


@given(quantities(), rounding())
def test_asec_of_sec_hypothesis(expected, r):
    """Should return input."""
    assume(expected.value >= Zero and expected.value <= pi.value)
    assume(expected.value != pi.value / Two)

    actual = expected.sec().asec()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(quantities(), rounding())
def test_sec_of_asec_hypothesis(expected, r):
    """Should return input."""
    assume(expected.value <= -1 or expected.value >= 1)
    actual = expected.asec().sec()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(quantities(), rounding())
def test_cot_hypothesis(q, r):
    """Should calculate the cotangent of ``Quantity`` objects."""
    assume(q.value > Zero and q.value < pi.value)

    actual = q.cot()
    expected = Quantity(
        Decimal(mpmath.nstr(mpmath.cot(mpmath.mpmathify(q.value)), mpmath.mp.dps)),
        q.figures,
        constant=q.constant,
    )

    assert actual == expected


@given(quantities(), rounding())
def test_acot_hypothesis(q, r):
    """Should calculate the inverse cotangent of ``Quantity`` objects."""
    e = q.acot()

    # Duplication; no need to test mpmath.
    assert (
        Decimal(mpmath.nstr(mpmath.acot(mpmath.mpmathify(q.value)), mpmath.mp.dps))
        == e.value
    )
    assert q.figures == e.figures
    assert q.constant == e.constant


@given(
    quantities(
        min_value=Decimal("0.0000000001"),
        max_value=pi.value - Decimal("0.0000000001"),
    ),
    rounding(),
)
def test_acot_of_cot_hypothesis(expected, r):
    """Should return input."""
    assume(
        mpmath.acot(mpmath.cot(mpmath.mpmathify(expected.value))) > 0
        and mpmath.acot(mpmath.cot(mpmath.mpmathify(expected.value)))
        < mpmath.mpmathify(pi.value)
    )

    actual = expected.cot().acot()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(quantities(), rounding())
def test_cot_of_acot_hypothesis(expected, r):
    """Should return input."""
    actual = expected.acot().cot()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


# Hyperbolic function tests.
@given(quantities(), rounding())
def test_sinh_hypothesis(q, r):
    """Should calculate the hyperbolic sine of ``Quantity`` objects."""
    # Avoid decimal overflow/underflow.
    assume(q.value > NegThousand and q.value < Thousand)

    actual = q.sinh()
    expected = Quantity(
        Decimal(mpmath.nstr(mpmath.sinh(mpmath.mpmathify(q.value)), mpmath.mp.dps)),
        q.figures,
        constant=q.constant,
    )

    assert actual == expected


@given(quantities(), rounding())
def test_asinh_hypothesis(q, r):
    """Should calculate the inverse hyperbolic sine of ``Quantity`` objects."""
    actual = q.asinh()
    expected = Quantity(
        Decimal(mpmath.nstr(mpmath.asinh(mpmath.mpmathify(q.value)), mpmath.mp.dps)),
        q.figures,
        constant=q.constant,
    )

    assert actual == expected


@given(quantities(), rounding())
def test_asinh_of_sinh_hypothesis(expected, r):
    """Should return input."""
    # Avoid decimal overflow/underflow.
    assume(expected.value > NegThousand and expected.value < Thousand)

    actual = expected.sinh().asinh()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(quantities(), rounding())
def test_sinh_of_asinh_hypothesis(expected, r):
    """Should return input."""
    actual = expected.asinh().sinh()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(
    quantities(
        min_value=NegThousand,
        max_value=Thousand,
    ),
    rounding(),
)
def test_cosh_hypothesis(q, r):
    """Should calculate the hyperbolic cosine of ``Quantity`` objects."""
    actual = q.cosh()
    expected = Quantity(
        Decimal(mpmath.nstr(mpmath.cosh(mpmath.mpmathify(q.value)), mpmath.mp.dps)),
        q.figures,
        constant=q.constant,
    )

    assert actual == expected


@given(
    quantities(
        min_value=One,
        max_value=Thousand,
    ),
    rounding(),
)
def test_acosh_hypothesis(q, r):
    """Should calculate the inverse hyperbolic cosine of ``Quantity`` objects."""
    actual = q.acosh()
    expected = Quantity(
        Decimal(mpmath.nstr(mpmath.acosh(mpmath.mpmathify(q.value)), mpmath.mp.dps)),
        q.figures,
        constant=q.constant,
    )

    assert actual == expected


@given(
    quantities(
        min_value=One,
        max_value=Thousand,
    ),
    rounding(),
)
def test_acosh_of_cosh_hypothesis(expected, r):
    """Should return input."""
    actual = expected.cosh().acosh()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(
    quantities(
        min_value=One,
        max_value=Thousand,
    ),
    rounding(),
)
def test_cosh_of_acosh_hypothesis(expected, r):
    """Should return input."""
    actual = expected.acosh().cosh()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(
    quantities(
        min_value=NegThousand,
        max_value=Thousand,
    ),
    rounding(),
)
def test_tanh_hypothesis(q, r):
    """Should calculate the hyperbolic tangent of ``Quantity`` objects."""
    actual = q.tanh()
    expected = Quantity(
        Decimal(mpmath.nstr(mpmath.tanh(mpmath.mpmathify(q.value)), mpmath.mp.dps)),
        q.figures,
        constant=q.constant,
    )

    assert actual == expected


@given(
    quantities(
        min_value=Decimal("-0.99"),
        max_value=Decimal("0.99"),
    ),
    rounding(),
)
def test_atanh_hypothesis(q, r):
    """Should calculate the inverse hyperbolic tangent of ``Quantity`` objects."""
    actual = q.atanh()
    expected = Quantity(
        Decimal(mpmath.nstr(mpmath.atanh(mpmath.mpmathify(q.value)), mpmath.mp.dps)),
        q.figures,
        constant=q.constant,
    )

    assert actual == expected


@given(
    quantities(
        min_value=NegTen,
        max_value=Ten,
    ),
    rounding(),
)
def test_atanh_of_tanh_hypothesis(expected, r):
    """Should return input."""
    actual = expected.tanh().atanh()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(
    quantities(
        min_value=NegOne,
        max_value=One,
    ),
    rounding(),
)
def test_tanh_of_atanh_hypothesis(expected, r):
    """Should return input."""
    actual = expected.atanh().tanh()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(
    quantities(
        min_value=NegThousand,
        max_value=Thousand,
    ),
    rounding(),
)
def test_csch_hypothesis(q, r):
    """Should calculate the hyperbolic cosecant of ``Quantity`` objects."""
    # Singularity.
    assume(q.value != Zero)

    actual = q.csch()
    expected = Quantity(
        Decimal(mpmath.nstr(mpmath.csch(mpmath.mpmathify(q.value)), mpmath.mp.dps)),
        q.figures,
        constant=q.constant,
    )

    assert actual == expected


@given(
    quantities(
        min_value=NegThousand,
        max_value=Thousand,
    ),
    rounding(),
)
def test_acsch_hypothesis(q, r):
    """Should calculate the inverse hyperbolic cosecant of ``Quantity`` objects."""
    # Singularity.
    assume(q.value != Zero)

    actual = q.acsch()
    expected = Quantity(
        Decimal(mpmath.nstr(mpmath.acsch(mpmath.mpmathify(q.value)), mpmath.mp.dps)),
        q.figures,
        constant=q.constant,
    )

    assert actual == expected


@given(
    quantities(
        min_value=NegThousand,
        max_value=Thousand,
    ),
    rounding(),
)
def test_acsch_of_csch_hypothesis(expected, r):
    """Should return input."""
    # Singularity.
    assume(expected.value != Zero)

    actual = expected.csch().acsch()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(
    quantities(
        min_value=NegThousand,
        max_value=Thousand,
    ),
    rounding(),
)
def test_csch_of_acsch_hypothesis(expected, r):
    """Should return input."""
    # Singularity.
    assume(expected.value != Zero)

    actual = expected.acsch().csch()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(
    quantities(
        min_value=NegThousand,
        max_value=Thousand,
    ),
    rounding(),
)
def test_sech_hypothesis(q, r):
    """Should calculate the hyperbolic secant of ``Quantity`` objects."""
    actual = q.sech()
    expected = Quantity(
        Decimal(mpmath.nstr(mpmath.sech(mpmath.mpmathify(q.value)), mpmath.mp.dps)),
        q.figures,
        constant=q.constant,
    )

    assert actual == expected


@given(
    quantities(
        min_value=Decimal("0.001"),
        max_value=Decimal("0.999"),
    ),
    rounding(),
)
def test_asech_hypothesis(q, r):
    """Should calculate the inverse hyperbolic secant of ``Quantity`` objects."""
    actual = q.asech()
    expected = Quantity(
        Decimal(mpmath.nstr(mpmath.asech(mpmath.mpmathify(q.value)), mpmath.mp.dps)),
        q.figures,
        constant=q.constant,
    )

    assert actual == expected


@given(
    quantities(
        min_value=Zero,
        max_value=Thousand,
    ),
    rounding(),
)
def test_asech_of_sech_hypothesis(expected, r):
    """Should return input."""
    actual = expected.sech().asech()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))


@given(
    quantities(
        min_value=Decimal("0.001"),
        max_value=Decimal("0.999"),
    ),
    rounding(),
)
def test_sech_of_asech_hypothesis(expected, r):
    """Should return input."""
    actual = expected.asech().sech()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))


@given(
    quantities(
        min_value=NegThousand,
        max_value=Thousand,
    ),
    rounding(),
)
def test_coth_hypothesis(q, r):
    """Should calculate the hyperbolic cotangent of ``Quantity`` objects."""
    # Singularity.
    assume(q.value != Zero)

    actual = q.coth()
    expected = Quantity(
        Decimal(mpmath.nstr(mpmath.coth(mpmath.mpmathify(q.value)), mpmath.mp.dps)),
        q.figures,
        constant=q.constant,
    )

    assert actual == expected


@given(
    quantities(
        min_value=NegThousand,
        max_value=Thousand,
    ),
    rounding(),
)
def test_acoth_hypothesis(q, r):
    """Should calculate the inverse hyperbolic cotangent of ``Quantity`` objects."""
    assume(q.value < NegOne or q.value > One)

    actual = q.acoth()
    expected = Quantity(
        Decimal(mpmath.nstr(mpmath.acoth(mpmath.mpmathify(q.value)), mpmath.mp.dps)),
        q.figures,
        constant=q.constant,
    )

    assert actual == expected


@given(
    quantities(
        min_value=NegTen,
        max_value=Ten,
    ),
    rounding(),
)
def test_acoth_of_coth_hypothesis(expected, r):
    """Should return input."""
    # Singularity.
    assume(expected.value != Zero)

    actual = expected.coth().acoth()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant


@given(
    quantities(
        min_value=NegThousand,
        max_value=Thousand,
    ),
    rounding(),
)
def test_coth_of_acoth_hypothesis(expected, r):
    """Should return input."""
    assume(expected.value < NegOne or expected.value > One)

    actual = expected.acoth().coth()

    assert actual.almosteq(expected, mpmath.mpf("1e-25"))
    assert actual.constant == expected.constant
