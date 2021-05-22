import pytest
import logging

@pytest.mark.tier1
def test_sum():
    logging.info("test_sum")
    assert 1+1 == 2


@pytest.mark.tier2
def test_mul():
    logging.info("test_mul")
    assert 1*1 == 1
