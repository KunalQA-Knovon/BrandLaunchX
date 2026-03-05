import os
import allure
from datetime import datetime
from playwright.sync_api import Page

def take_screenshot(page: Page, name: str = "failure"):
    """
    Capture screenshot, save locally, and attach to Allure report.
    """
    try:
        if not page or page.is_closed():
            return

        # Ensure screenshots folder exists
        os.makedirs("screenshots", exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"{name}_{timestamp}.png"
        file_path = os.path.join("screenshots", file_name)

        # Save screenshot to disk
        page.screenshot(path=file_path, full_page=True)

        # Attach to Allure
        with open(file_path, "rb") as f:
            allure.attach(
                f.read(),
                name=file_name,
                attachment_type=allure.attachment_type.PNG
            )

    except Exception as e:
        allure.attach(
            str(e),
            name="screenshot_error",
            attachment_type=allure.attachment_type.TEXT
        )
