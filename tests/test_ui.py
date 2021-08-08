import logging
import pytest
import os
from framework.marks import ui_mark

from ui.version_ui import VersionUI

logger = logging.getLogger(__name__)


class TestUserInterface(object):
    """
    Test User Interface Validation

    """

    @ui_mark
    @pytest.mark.parametrize("version_id", [os.getenv("version_web")])
    def test_version_ui(self, setup_ui, version_id):
        """
        Validate User Interface

        Args:
            setup_ui: login function on conftest file

        """
        version_ui = VersionUI(setup_ui)
        version_ui.check_version(version=version_id)


