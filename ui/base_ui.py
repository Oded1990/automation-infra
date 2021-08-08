from pathlib import Path
import datetime
import logging
import os
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from framework import config


logger = logging.getLogger(__name__)


class BaseUI:
    """
    Base Class for UI Tests

    """

    def __init__(self, driver):
        self.driver = driver
        self.screenshots_folder = os.path.join(
            os.path.expanduser(config.RUN["log_dir"]),
            f"screenshots_ui_{config.RUN['run_id']}",
            os.environ.get("PYTEST_CURRENT_TEST").split(":")[-1].split(" ")[0],
        )
        if not os.path.isdir(self.screenshots_folder):
            Path(self.screenshots_folder).mkdir(parents=True, exist_ok=True)
        logger.info(f"screenshots pictures:{self.screenshots_folder}")

    def do_click(self, locator, timeout=30, enable_screenshot=False):
        """
        Click on Button/link on OpenShift Console

        locator (set): (GUI element needs to operate on (str), type (By))
        timeout (int): Looks for a web element repeatedly until timeout (sec) happens.
        enable_screenshot (bool): take screenshot
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(ec.element_to_be_clickable((locator[1], locator[0])))
            screenshot = (
                config.UI_SELENIUM.get("screenshot") and enable_screenshot
            )
            if screenshot:
                self.take_screenshot()
            element.click()
        except TimeoutException as e:
            self.take_screenshot()
            logger.error(e)
            raise TimeoutException

    def do_send_keys(self, locator, text, timeout=30):
        """
        Send text to element on OpenShift Console

        locator (set): (GUI element needs to operate on (str), type (By))
        text (str): Send text to element
        timeout (int): Looks for a web element repeatedly until timeout (sec) happens.

        """
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(ec.element_to_be_clickable((locator[1], locator[0])))
        element.send_keys(text)

    def check_element_text(self, expected_text, element="*"):
        """
        Check if the text matches the expected text.

        Args:
            expected_text (string): The expected text.

        return:
            bool: True if the text matches the expected text, False otherwise

        """
        element_list = self.driver.find_elements_by_xpath(
            f"//{element}[contains(text(), '{expected_text}')]"
        )
        return len(element_list) > 0

    def take_screenshot(self):
        """
        Take screenshot using python code

        """
        time.sleep(1)
        filename = os.path.join(
            self.screenshots_folder,
            f"{datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S.%f')}.png",
        )
        logger.info(f"Creating snapshot: {filename}")
        self.driver.save_screenshot(filename)
        time.sleep(0.5)


def login_ui():
    """
    Login to OpenShift Console

    return:
        driver (Selenium WebDriver)

    """
    logger.info("Get URL of OCP console")
    console_url = config.UI_SELENIUM.get("url")

    browser = config.UI_SELENIUM.get("browser_type")
    if browser == "chrome":
        logger.info("chrome browser")
        chrome_options = Options()

        ignore_ssl = config.UI_SELENIUM.get("ignore_ssl")
        if ignore_ssl:
            chrome_options.add_argument("--ignore-ssl-errors=yes")
            chrome_options.add_argument("--ignore-certificate-errors")
            chrome_options.add_argument("--allow-insecure-localhost")
            capabilities = chrome_options.to_capabilities()
            capabilities["acceptInsecureCerts"] = True

        # headless browsers are web browsers without a GUI
        headless = config.UI_SELENIUM.get("headless")
        if headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("window-size=1920,1400")

        chrome_browser_type = config.UI_SELENIUM.get("chrome_type")
        driver = webdriver.Chrome(
            ChromeDriverManager(chrome_type=chrome_browser_type).install(),
            options=chrome_options,
        )
    else:
        raise ValueError(f"Not Support on {browser}")
    driver.maximize_window()
    driver.get(console_url)
    return driver


def close_browser(driver):
    """
    Close Selenium WebDriver

    Args:
        driver (Selenium WebDriver)

    """
    logger.info("Close browser")
    driver.close()
