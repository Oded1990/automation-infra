import logging
import pytest
import os
from framework.marks import tier1


logger = logging.getLogger(__name__)


class TestUserInterface1(object):
    """
    Test User Interface Validation

    """
    @tier1
    @pytest.mark.parametrize("version_id", [os.getenv("version_web")])
    def test_tier1(self, version_id):
        """
        Validate User Interface
        """
        logger.info(version_id)
        logger.info(f"oded viner 1 version:{version_id}")
        print(f"oded viner 2 version 2:{version_id}")
