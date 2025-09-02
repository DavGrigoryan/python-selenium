"""Base Selenium page object with find element with retry logic."""

import time
from typing import Callable, Optional

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Reusable Selenium base page class with utility methods."""

    TIMEOUT: int = 15
    POLLING_INTERVAL: float = 0.5

    def __init__(self, browser: WebDriver) -> None:
        self.browser = browser

    # Find element with retries
    def find_element(
        self,
        locator: tuple,
        condition: Optional[Callable] = None,
        timeout: int = TIMEOUT,
        retries: int = 3,
    ) -> WebElement:
        """
        Find a single element with retry logic.
        """
        last_exception = None
        for _ in range(1, retries + 1):
            try:
                wait = WebDriverWait(self.browser, timeout)
                if condition:
                    return wait.until(condition(locator))
                return self.browser.find_element(*locator)
            except Exception as e:
                last_exception = e
                time.sleep(self.POLLING_INTERVAL)
        raise TimeoutException(
            f"Element {locator} not found after {retries} retries"
        ) from last_exception