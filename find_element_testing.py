from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://www.facebook.com")

# # 1: TAG_NAME
# element_text = driver.find_element(By.TAG_NAME, value="h2")
# print(element_text.text)
#
# # 2: ID
# email = driver.find_element(By.ID, value="email")
# email.send_keys("haha")
#
# # 3: NAME
# email = driver.find_element(By.NAME, value="email")
# email.send_keys("buhaha")
#
# # 4: XPATH
# password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
# password.send_keys("acv")
#
# # 5: CSS_SELECTOR
# email = driver.find_element(By.CSS_SELECTOR, value='input[id="email"]')
# email.send_keys("acv")
#
# # 6: CLASS_NAME
# email = driver.find_element(By.CLASS_NAME, value="inputtext _55r1 _6luy _9npi")
# email.send_keys("CLASS_NAME")
#
# # 7: LINK_TEXT
# forgot_password = driver.find_element(By.LINK_TEXT, value="Forgot password?")
# forgot_password.click()
#
# # 8: PARTIAL_LINK_TEXT
# forgot_password = driver.find_element(By.PARTIAL_LINK_TEXT, value="Forgot")
# forgot_password.click()


# 6: CLASS_NAME
email = driver.find_elements(By.CLASS_NAME, value="inputtext")
print(email)

for email in email:
    email.send_keys("keys")












