from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv
import requests
import time
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
# user = os.getenv("USERNAME")
password = os.getenv("password")

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://vtop.vitbhopal.ac.in/vtop/login')
title = driver.title

buttons = driver.find_elements(By.CSS_SELECTOR, '.btn.btn-primary.fw-bold')

if buttons:
    first_button = buttons[0]
    first_button.click()
else:
    print("Skill issue. Exiting...")

wait = WebDriverWait(driver, 10)
attempt = 0
max_attempts = 3

while attempt <= max_attempts:
    try:
        image_element = wait.until(EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'data:image/jpeg;base64,') and contains(@aria-describedby, 'button-addon2')]")))
        image_src = image_element.get_attribute("src")
        start_index = image_src.find("data:image/jpeg;base64,") + len("data:image/jpeg;base64,")
        end_index = image_src.find("aria-describedby=")
        base64_string = image_src[start_index:end_index]
        break
    except TimeoutException:
        print("Attempt", attempt, "- Image element not found within the timeout window")
        if attempt < max_attempts:
            print("Reloading the page and retrying...")
            driver.refresh()
            attempt += 1
        else:
            print("Skill issue. Exiting...")
            break

api_key = API_KEY

url = "https://ocr.captchaai.com/solve.php"


data = {
    "method": "base64",
    "key": api_key,
    "body": base64_string
}

response = requests.post(url, data=data)

if response.status_code == 200:
    captcha_id = response.text.split("|")[1]
    print("Captcha ID:", captcha_id)
    captcha_input = driver.find_element(By.CLASS_NAME, 'form-control.form-control-sm')
    captcha_input.send_keys(captcha_id)

    username_input = driver.find_element(By.ID, 'username')
    # ! add your registration number incase the env doesn't work
    username_input.send_keys("Your Registration Number")

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)

    button1 = driver.find_element(By.CSS_SELECTOR, '.btn.btn-sm.btn-primary.float-end')
    button1.click()
    while driver.window_handles:
        pass
    driver.quit()

else:
    print("Error:", response.text)

# time.sleep(30)