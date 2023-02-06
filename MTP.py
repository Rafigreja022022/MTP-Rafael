from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.saucedemo.com/")
navegador.save_screenshot("open21.png")
navegador.find_element('xpath', '//*[@id="user-name"]').send_keys('locked_out_user')
navegador.save_screenshot("open22.png")
navegador.find_element('xpath', '//*[@id="password"]').send_keys('secret_sauce')
navegador.save_screenshot("open23.png")
navegador.find_element('xpath','//*[@id="login-button"]').click()
navegador.save_screenshot("open24.png")
navegador.find_element('xpath', '//*[@id="login_button_container"]/div/form/div[3]')
navegador.find_element('xpath','//*[@id="login_button_container"]/div/form/div[3]/h3/button').click()
