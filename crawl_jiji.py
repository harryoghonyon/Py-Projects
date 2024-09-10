import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

# Load envrionment variables from .env file
load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')


def run(playwright):
    try:
        # Launch the browser
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://jiji.ng")

        try:
            sign_in_button = page.locator('text="Sign In"')
            sign_in_button.click()
        except TimeoutError:
            print("Sign-in button not found")
            return

        overlay = page.locator('fw-fixed-background')
        if overlay.is_visible():
            page.evaluate(
                "document.querySelector('.fw-fixed-background').style.display = 'none';")

        # Click email or phone login button
        try:
            email_or_phone_button = page.locator('.qa-fw-button')
            email_or_phone_button.click()
        except TimeoutError:
            print("Email or phone button not found")
            return

        # Enter email and password
        page.fill('input.qa-login-field', EMAIL)
        page.fill('input.qa-password-field', PASSWORD)

        # Click login button
        login_button = page.locator('button.qa-login-submit')
        login_button.click()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser context
        context.close()


with sync_playwright() as playwright:
    run(playwright)