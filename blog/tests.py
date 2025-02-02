from django.test import TestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get(url='http://127.0.0.1:8000/admin')


def element_is_clickable():
    driver.find_element(
        By.XPATH, value='//*[@id="id_username"]').send_keys("wolkt")
    driver.find_element(
        by=By.XPATH, value='//*[@id="id_password"]').send_keys("58583993")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="user-tools"]/a[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/nav/div/a/span').click()


# element_is_clickable()
# time.sleep(20)

def response_check(page_weight, file_path):
    height = 768  # nie ma znaczenia, ważna jest szerokość strony
    driver.set_window_size(page_weight, height)
    driver.save_screenshot(file_path)


response_check(900, "test900.png")
response_check(1200, "test1200.png")
response_check(1800, "test1800.png")
response_check(600, "test600.png")
