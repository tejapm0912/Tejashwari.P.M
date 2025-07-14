import undetected_chromedriver as uc
from fastapi import HTTPException
import logging

driver = None

def initialize_driver():
    global driver
    if driver is None:
        options = uc.ChromeOptions()
        try:
            driver = uc.Chrome(options=options)
            logging.info("Driver initialized successfully.")
        except Exception as e:
            logging.error(f"Driver init error: {e}")
            raise HTTPException(status_code=500, detail="Browser initialization failed.")
    return driver

def get_driver():
    return driver

def close_driver():
    global driver
    if driver:
        driver.quit()
        driver = None
