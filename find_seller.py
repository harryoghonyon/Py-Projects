from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv('facebook_login.env')

# Fetch phone number and password from .env file
PHONE_NUMBER = os.getenv('PHONE_NUMBER')
PASSWORD = os.getenv('PASSWORD')

# Ensure that the variables are loaded
if not PHONE_NUMBER or not PASSWORD:
    raise ValueError("PHONE_NUMBER and PASSWORD must be set in the .env file")

# Initialize WebDriver
driver = webdriver.Chrome()


def login_facebook():
    try:
        driver.get("https://jiji.ng")

        # Wait for and click the sign-in button
        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "h-flex-center"))
        )
        sign_in_button.click()

        # Wait for the overlay element and set its display to 'none'
        overlay_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "fw-fixed-background"))
        )
        driver.execute_script(
            "arguments[0].style.display = 'none';", overlay_element)
        print("Overlay element removed")

        # Wait for and click on the 'Continue with Facebook' button
        facebook_login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "bc-facebook"))
        )
        facebook_login_button.click()

        # Wait for and enter the phone number and password
        phone_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        phone_field.send_keys(PHONE_NUMBER)

        password_field = driver.find_element(By.ID, "pass")
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.RETURN)

        print("Login successful, proceeding with post-login actions...")

        # Optionally, perform any post-login actions here

    except Exception as e:
        print(f"An error occurred: {e}")

    # finally:
    #     # Wait before closing the browser to verify manually (Optional)
    #     time.sleep(5)
    #     # Close the driver
    #     driver.quit()


if __name__ == "__main__":
    login_facebook()
