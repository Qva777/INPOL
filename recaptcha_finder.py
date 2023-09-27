from constants import Selectors
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def recaptcha_finder(driver, time):
    """ Check is reCaptcha passed """
    iframe_element = WebDriverWait(driver, time).until(EC.presence_of_element_located((By.XPATH, Selectors.FRAME)))
    driver.switch_to.frame(iframe_element)
    print("Switch to frame")

    recaptcha_checkbox = WebDriverWait(driver, time).until(
        EC.presence_of_element_located((By.XPATH, Selectors.RECAPTCHA_CHECKBOX)))
    print("reCaptcha checkbox")
    driver.switch_to.default_content()
