from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://vtop.vitbhopal.ac.in/vtop/login')
title = driver.title


buttons = driver.find_elements(By.CSS_SELECTOR, '.btn.btn-primary.fw-bold')


if buttons:
  first_button = buttons[0]
  first_button.click()
  print("Clicked the first button with class 'btn btn-primary fw-bold'")
else:
  print("No buttons found with class 'btn btn-primary fw-bold'")

wait = WebDriverWait(driver, 10)

expected_condition = EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'data:image/jpeg;base64,') and contains(@aria-describedby, 'button-addon2')]"))

try:

  image_element = wait.until(expected_condition)

  image_src = image_element.get_attribute("src")
  start_index = image_src.find("data:image/jpeg;base64,") + len("data:image/jpeg;base64,")
  end_index = image_src.find("aria-describedby=")
  base64_string = image_src[start_index:end_index]

  print("Extracted base64 string:", base64_string)
except TimeoutException:
  print("Image element not found within the timeout window")

time.sleep(20)  

print(title)

