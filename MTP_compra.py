from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.saucedemo.com/")
navegador.save_screenshot("open0.png")
navegador.find_element('xpath', '//*[@id="login-button"]').click()
navegador.save_screenshot("open1.png")
navegador.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
navegador.save_screenshot("open2.png")
navegador.find_element('xpath', '//*[@id="password"]').send_keys('secret_sauce')
navegador.save_screenshot("open3.png")
navegador.find_element('xpath', '//*[@id="login-button"]').click()
navegador.save_screenshot("open4.png")
navegador.find_element('xpath', '//*[@id="header_container"]/div[2]/span').is_displayed
navegador.save_screenshot("open5.png")
navegador.find_element('xpath', '//*[@id="item_0_title_link"]/div')
navegador.save_screenshot("open6.png")
navegador.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
navegador.save_screenshot("open7.png")
navegador.find_element('xpath', '//*[@id="shopping_cart_container"]/a').click()
navegador.save_screenshot("open8.png")
navegador.find_element('xpath', '//*[@id="checkout"]').click()
navegador.save_screenshot("open9.png")
navegador.find_element('xpath', '//*[@id="first-name"]').send_keys('Rafael')
navegador.save_screenshot("open10.png")
navegador.find_element('xpath', '//*[@id="last-name"]').send_keys('Leafar')
navegador.save_screenshot("open11.png")
navegador.find_element('xpath', '//*[@id="postal-code"]').send_keys('03620-001')
navegador.save_screenshot("open12.png")
navegador.find_element('xpath', '//*[@id="continue"]').click()
navegador.save_screenshot("open13.png")
navegador.find_element('xpath', '//*[@id="finish"]')
navegador.save_screenshot("open14.png")
navegador.find_element('xpath', '//*[@id="finish"]').click()
navegador.save_screenshot("open15.png")