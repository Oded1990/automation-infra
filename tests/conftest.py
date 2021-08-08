import pytest
import os

from ui.base_ui import login_ui, close_browser


def pytest_addoption(parser):
    parser.addoption("--version_web", action="store", default="default name")


def pytest_configure(config):
    os.environ["version_web"] = config.getoption("version_web")


@pytest.fixture(scope="function")
def setup_ui(request):
    driver = login_ui()

    def finalizer():
        close_browser(driver)

    request.addfinalizer(finalizer)
    return driver
