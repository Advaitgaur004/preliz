import pytest
import numpy as np
from numpy.testing import assert_almost_equal

from preliz.distributions import (
    Normal,
    Beta,
    Gamma,
    LogNormal,
    Exponential,
    Student,
    Binomial,
    NegativeBinomial,
    Poisson,
)


@pytest.mark.parametrize(
    "distribution, params",
    [
        (Normal, (0, 1)),
        (Beta, (2, 5)),
        (Gamma, (1, 0.5)),
        (LogNormal, (0, 0.5)),
        (Exponential, (0.5,)),
        # (Student, (4, 0, 1)),
        # (Student, (1000, 0, 1)),
        (Binomial, (2, 0.5)),
        (Binomial, (2, 0.1)),
        (NegativeBinomial, (2, 0.9)),
        (NegativeBinomial, (2, 0.1)),
        (Poisson, (4.5,)),
    ],
)
def test_moments(distribution, params):
    dist = distribution(*params)
    dist_ = distribution()
    dist_.fit_moments(dist.rv_frozen.mean(), dist.rv_frozen.std())

    tol = 7
    if dist.name == "binomial":
        tol = 0
    assert_almost_equal(dist.rv_frozen.mean(), dist_.rv_frozen.mean(), tol)
    assert_almost_equal(dist.rv_frozen.std(), dist_.rv_frozen.std(), tol)
    if dist.name == "student":
        assert_almost_equal(params[1:], dist_.params[1:], 0)
    else:
        assert_almost_equal(params, dist_.params, 0)


@pytest.mark.parametrize(
    "distribution, params",
    [
        (Normal, (0, 1)),
        (Beta, (2, 5)),
        (Gamma, (1, 0.5)),
        (LogNormal, (0, 0.5)),
        (Exponential, (0.5,)),
        (Student, (4, 0, 1)),
        (Student, (1000, 0, 1)),
        (Binomial, (2, 0.5)),
        (Binomial, (2, 0.1)),
        # (NegativeBinomial, (2, 0.9)),
        # (NegativeBinomial, (2, 0.1)),
        (Poisson, (4.5,)),
    ],
)
def test_mle(distribution, params):
    dist = distribution(*params)
    sample = dist.rv_frozen.rvs(10000)
    dist_ = distribution()
    dist_.fit_mle(sample)

    assert_almost_equal(dist.rv_frozen.mean(), dist_.rv_frozen.mean(), 1)
    assert_almost_equal(dist.rv_frozen.std(), dist_.rv_frozen.std(), 1)
    if dist.name == "student":
        assert_almost_equal(params[1:], dist_.params[1:], 0)
    else:
        assert_almost_equal(params, dist_.params, 0)


# def test check_endpoints()
