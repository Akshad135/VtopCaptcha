# import requests

# response = requests.get('https://vtop.vitbhopal.ac.in/vtop/login')

# def find_between(s, start, end):
#     try:
#         start_index = s.index(start) + len(start)
#         end_index = s.index(end, start_index)
#         return s[start_index:end_index]
#     except ValueError:
#         return None

# # Update start and end strings to match the correct patterns
# # image_string = find_between(response.text, 'base64,', '" aria-describedby=')
# image_string = find_between(response.text, 'btn btn-info fw-bold"', '</button>')
# print(image_string)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://vtop.vitbhopal.ac.in/vtop/login')
# title = driver.title

# # Find buttons with specific class
# buttons = driver.find_elements(By.CSS_SELECTOR, '.btn.btn-primary.fw-bold')
# num_buttons = len(buttons)

# time.sleep(5)

# print(title)
# print(num_buttons)



