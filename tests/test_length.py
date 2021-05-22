from infrastructure.math import list_positive
import pytest
import logging

@pytest.mark.tier1
def test_length():
    logging.info("test_length")
    assert list_positive[0]+list_positive[1] == 3
