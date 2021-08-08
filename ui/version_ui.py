from ui.views import locators
from ui.base_ui import BaseUI
from helpers.helpers import TimeoutGenerator


class VersionUI(BaseUI):
    """
    User Interface Version

    """

    def __init__(self, driver):
        super().__init__(driver)
        self.version_locators = locators

    def check_version(self, version):
        self.do_send_keys(self.version_locators["text-input"], version)
        self.do_click(self.version_locators["version-button"])
        timeout_generator = TimeoutGenerator(
            timeout=30,
            sleep=2,
            func=self.check_element_text,
            expected_text=version
        )
        timeout_generator.wait_for_value(value=True)

