from selenium.webdriver.common.by import By

locators = {
    "text-input": ('input[data-test="text-input"]', By.CSS_SELECTOR),
    "version-button": ('input[data-test="version-button"]', By.CSS_SELECTOR),
}
