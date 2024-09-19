from selenium import webdriver
from selenium.webdriver.common.by import By

def test_buy():
    browser = webdriver.Firefox()
    browser.get('https://www.saucedemo.com/')
    user_name = browser.find_element(By.XPATH, '//*[@id="user-name"]')
    user_name.send_keys('standard_user')
    password = browser.find_element(By.XPATH, '//*[@id="password"]')
    password.send_keys('secret_sauce')
    login = browser.find_element(By.XPATH, '//*[@id="login-button"]')
    login.click()
    browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    browser.find_element(By.XPATH, '//*[@id="checkout"]').click()
    browser.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('username')
    browser.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
    browser.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('1')
    browser.find_element(By.XPATH, '//*[@id="continue"]').click()
    browser.find_element(By.XPATH, '//*[@id="finish"]').click()

    text_value = browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/h2').text
    assert text_value == "Thank you for your order!"
