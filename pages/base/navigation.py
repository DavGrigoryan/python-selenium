"""Base Selenium page object with navigation support."""

import allure
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """Reusable Selenium base page class with utility methods."""

    def __init__(self, browser: WebDriver) -> None:
        self.browser = browser

    def navigate_to(self, url: str) -> None:
        """Navigate to a specific URL."""
        with allure.step(f"Navigate to {url}"):
            self.browser.get(url)