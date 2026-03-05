from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from utils.screenshotUtils import take_screenshot


def wait_for_visible_locator(page: Page, locator: str, timeout: int = 5000):
    """
    Wait for locator to be visible.
    Auto screenshot on failure.
    """
    try:
        element = page.locator(locator)
        element.wait_for(state="visible", timeout=timeout)
        return element

    except PlaywrightTimeoutError:
        take_screenshot(page, "locator_timeout")
        raise

    except Exception:
        take_screenshot(page, "locator_error")
        raise