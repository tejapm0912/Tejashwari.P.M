from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import logging

def wait_for_element(driver, by, value, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
    except TimeoutException:
        logging.warning(f"Timeout: {by}={value}")
        return None

def find_element_safely(driver, by, value, timeout=5):
    try:
        return wait_for_element(driver, by, value, timeout)
    except Exception:
        return None

def click_element_safely(driver, by, value, timeout=5):
    try:
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
        element.click()
        return True
    except (TimeoutException, NoSuchElementException, StaleElementReferenceException):
        return False
