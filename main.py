from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://www.linkedin.com/login")

username = driver.find_element(By.ID, value="username")
username.send_keys(os.environ.get("password"))
password = driver.find_element(By.ID, value="password")
password.send_keys(os.environ.get("password"), Keys.ENTER)

time.sleep(12)


job_search_box = driver.find_element(By.CSS_SELECTOR, value='input[aria-label="Search"]')
job_search_box.send_keys("python developer", Keys.ENTER)

time.sleep(4)
see_all_jobs = driver.find_element(By.LINK_TEXT, value='Easy apply')
see_all_jobs.click()

time.sleep(5)
country = driver.find_element(By.CSS_SELECTOR, value='input[aria-label="City, state, or zip code"]')

country.clear()
country.send_keys("Canada", Keys.ENTER)

time.sleep(7)
all_listings = driver.find_elements(By.CLASS_NAME, value='job-card-container--clickable')

print(all_listings)

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(4)

    click_apply = driver.find_element(By.CLASS_NAME, value='jobs-apply-button')
    click_apply.click()

    time.sleep((4))
    next = driver.find_element(By.CSS_SELECTOR, value='button[aria-label="Continue to next step"]')
    next.click()

    time.sleep(4)
    next_resume = driver.find_element(By.CSS_SELECTOR, value='button[aria-label="Continue to next step"]')
    next_resume.click()

    time.sleep(4)
    additional_q = driver.find_element(By.CSS_SELECTOR,value='.artdeco-text-input--input')
    additional_q.clear()
    additional_q.send_keys("1")

    # time.sleep(4)
    # dash_exp = driver.find_element(By.CLASS_NAME, value='.fb-dash-form-element__error-field artdeco-text-input--input')
    # dash_exp.clear()
    # dash_exp.click()

    time.sleep(4)
    review = driver.find_element(By.CSS_SELECTOR, value='button[aria-label="Review your application"]')
    review.click()

    time.sleep(4)
    submit = driver.find_element(By.CSS_SELECTOR, value='button[aria-label="Submit application"]')
    submit.click()

    time.sleep(4)
    cancel_pop_up = driver.find_element(By.CSS_SELECTOR, value='button[aria-label="Dismiss"]')
    cancel_pop_up.click()







    time.sleep(2)



























