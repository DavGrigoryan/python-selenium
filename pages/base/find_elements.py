"""Base Selenium page object with support for finding multiple elements."""

from typing import Callable, Optional

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Reusable Selenium base page class with utility methods."""

    TIMEOUT: int = 15

    def __init__(self, browser: WebDriver) -> None:
        self.browser = browser

    def find_elements(
        self,
        locator: tuple,
        condition: Optional[Callable] = None,
        timeout: int = TIMEOUT,
        allure_desc: str = "Find multiple elements"
    ) -> list[WebElement]:
        """
        Find multiple elements on the page.

        Args:
            locator (tuple): Locator strategy and value, e.g., (By.ID, "username").
            condition (Callable, optional): Selenium expected condition.
            timeout (int, optional): Maximum wait time in seconds.
            allure_desc (str, optional): Description for Allure reporting.

        Returns:
            list[WebElement]: A list of located WebElements.

        Raises:
            TimeoutException: If no elements match the locator within the timeout.
        """
        with allure.step(allure_desc):
            wait = WebDriverWait(self.browser, timeout)
            if condition:
                return wait.until(condition(locator))
            return self.browser.find_elements(*locator)
