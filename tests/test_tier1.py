import logging
import pytest
import os
from framework.marks import ui_mark, tier1

from ui.version_ui import VersionUI

logger = logging.getLogger(__name__)


class TestUserInterface1(object):
    """
    Test User Interface Validation

    """
    @ui_mark
    @pytest.mark.parametrize("version_id", [os.getenv("version_web")])
    def test_ui(self, setup_ui, version_id):
        """
        Validate User Interface

        Args:
            setup_ui: login function on conftest file

        """
        version_ui = VersionUI(setup_ui)
        version_ui.check_version(version=version_id)

    @tier1
    @pytest.mark.parametrize("version_id", [os.getenv("version_web")])
    def test_tier1(self, setup_ui, version_id):
        """
        Validate User Interface

        Args:
            setup_ui: login function on conftest file

        """
        version_ui = VersionUI(setup_ui)
        version_ui.check_version(version=version_id)