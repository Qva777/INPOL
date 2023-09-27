import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from env_config import USER_EMAIL, USER_PASSWORD, USER_ID
from constants import Selectors
from recaptcha_finder import recaptcha_finder
from selenium_config import chrome_options
from activate_extension import activate_extension

from telegram import send_photo

# Open WebDriver
driver = webdriver.Chrome(options=chrome_options)
time.sleep(5)
activate_extension.run()

# Main URL
url_to_open = 'https://inpol.mazowieckie.pl/'
driver.get(url_to_open)

try:
    element = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, Selectors.USER_EMAIL)))
    element.send_keys(USER_EMAIL)
    print("Input email")

    element = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, Selectors.USER_PASSWORD)))
    element.send_keys(USER_PASSWORD)
    print("Input password")

    element = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, Selectors.UA_LANGUAGE)))
    element.click()
    print("Selected language")

    recaptcha_finder(driver, 120)

    element = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, Selectors.LOGIN)))
    element.click()
    print("Pressed Login")

    time.sleep(4)
    element = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, Selectors.DEAL)))
    element.click()
    print("Deal button")

    element = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, Selectors.PROFILE)))
    element.click()
    print("Selected profile")


    def select_location_and_queue(driver, location_xpath):
        element = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, Selectors.OPEN_CALENDAR)))
        element.click()
        print("Open calendar")

        element = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, Selectors.PLACE_MENU)))
        element.click()
        print("Place menu")

        element = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, location_xpath)))
        element.click()
        print("Selected place")

        element = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, Selectors.QUEUE_MENU)))
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        print("Open queue menu")

        time.sleep(2)
        element = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, Selectors.SELECT_QUEUE)))
        element.click()
        print("Selected queue")

        recaptcha_finder(driver, 30)
        element = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, Selectors.VERIFY)))
        element.click()
        print("Pressed Verify")

        calendar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "reservation__calendar")))
        driver.execute_script("arguments[0].scrollIntoView(true);", calendar)

        clicked_next_month = False

        while True:
            for number_day in range(1, 23):
                xpath = f"(//td[contains(@class, 'mat-calendar-body-cell')][not(contains(@class, 'mat-calendar-body-disabled'))])[{number_day}]"
                print(number_day)
                try:
                    day_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))

                    try:
                        WebDriverWait(driver, 10).until_not(
                            EC.presence_of_element_located((By.CSS_SELECTOR, ".spinner")))
                    except TimeoutException:
                        pass

                    day_element.click()
                    print(f"Clicked on day {number_day}")
                    time.sleep(1)

                    try:
                        recaptcha_finder(driver, 30)

                        element = WebDriverWait(driver, 30).until(
                            EC.visibility_of_element_located((By.XPATH, Selectors.VERIFY)))
                        element.click()
                        print("Pressed Verify - after date")

                    except TimeoutException:
                        print(
                            f"Verify button not found after clicking on day {number_day}, performing default action...")

                    time.sleep(3)
                    img = pyautogui.screenshot()
                    img.save(r"screenshot.png")
                    send_photo(USER_ID, 'screenshot.png')

                    if number_day == 22:
                        try:
                            next_month_button = WebDriverWait(driver, 10).until(
                                EC.visibility_of_element_located((By.XPATH, Selectors.NEXT_MONTH)))
                            next_month_button.click()
                            print("Clicked 'Next month' button")
                            clicked_next_month = True
                            break
                        except TimeoutException:
                            print("Next month button not found, exiting loop...")
                            break

                except TimeoutException:
                    print(f"Date not found for day {number_day}, performing default action...")

                    if not clicked_next_month:
                        try:
                            next_month_button = WebDriverWait(driver, 10).until(
                                EC.visibility_of_element_located((By.XPATH, Selectors.NEXT_MONTH)))
                            next_month_button.click()
                            print("Clicked 'Next month' button")
                            clicked_next_month = True
                            break
                        except TimeoutException:
                            print("Next month button not found, exiting loop...")
                            break

            clicked_next_month = False
            try:
                date = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, Selectors.FREE_DATE)))
            except TimeoutException:
                driver.get("https://inpol.mazowieckie.pl/home/cases/4c4e0296-a163-4568-b93a-4b5fafe1d081")
                break


    select_location_and_queue(driver, Selectors.SELECT_PLACE)
    select_location_and_queue(driver, Selectors.SELECT_PLACE_2)
    select_location_and_queue(driver, Selectors.SELECT_PLACE_3)

except Exception as e:
    print("An error occurred:", str(e))

time.sleep(10)
driver.quit()
