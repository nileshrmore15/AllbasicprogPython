from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_test1():


    serv_obj = Service("D:\Gdrivers\chromdriver.exe")
    driver = webdriver.Chrome(service=serv_obj)

    driver.get("https://www.facebook.com/")
    driver.maximize_window()

    inputemail= driver.find_element(By.ID, "email")
    inputemail.send_keys("abc@gmail.com")

    driver.find_element(By.ID, "pass").send_keys("abc123")

    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button").click()

    driver.close()

def test_test2():

    option = webdriver.ChromeOptions()
    option.experimental_options("detach", True)

    serv_obj = Service("D:\Gdrivers\chromdriver.exe")
    driver = webdriver.Chrome(service=serv_obj, options=option)
    driver.maximize_window()

    inputemail= driver.find_element(By.ID, "email")
    inputemail.send_keys("abc@gmail.com")

    driver.find_element(By.ID, "pass").send_keys("abc123")

    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button").click()

    driver.close()

