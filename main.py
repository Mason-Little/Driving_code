from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import smtplib
from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
for i in range(1, 500):
    last_name = 'Place Holder'
    licence = '11111'
    other_thing = 'Place Holder'

    url = 'https://onlinebusiness.icbc.com/webdeas-ui/login;type=driver'

    driver = webdriver.Chrome("D:\\Home Code\\chromedriver.exe")
    driver.get(url)
    time.sleep(3)

    driver.find_element_by_id("mat-input-0").send_keys(last_name)
    driver.find_element_by_id("mat-input-1").send_keys(licence)
    driver.find_element_by_id("mat-input-2").send_keys(other_thing)
    driver.find_element_by_xpath('//*[@id="mat-checkbox-1"]/label/div').click()
    driver.find_element_by_xpath('/html/body/app-root/app-login/mat-card/mat-card-content/form/div[3]/button[2]').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/app-root/app-driver/div/mat-card/div[5]/div[1]/app-appointments/div/div['
                                 '2]/div/div[4]/button[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div/div[2]/div/mat-dialog-container/app-cancel/div/div/div[2]/button[2]').click()
    driver.find_element_by_id('mat-input-3').send_keys("S")
    time.sleep(.1)
    driver.find_element_by_id('mat-input-3').send_keys("q")
    time.sleep(.1)
    driver.find_element_by_id('mat-input-3').send_keys("u")
    time.sleep(.1)
    driver.find_element_by_id('mat-input-3').send_keys("a")
    time.sleep(.1)
    driver.find_element_by_id('mat-input-3').send_keys("m")
    time.sleep(.1)
    driver.find_element_by_id('mat-input-3').send_keys("i")
    time.sleep(1.5)
    driver.find_element_by_id('mat-input-3').send_keys(Keys.ENTER)
    driver.find_element_by_xpath('/html/body/div/div[1]/div/mat-dialog-container/app-search-modal/div/div/form/div['
                                 '2]/button').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div/div[1]/div/mat-dialog-container/app-search-modal/div[2]/div/div[2]/div[2]').click()
    time.sleep(3)
    textele = driver.find_element_by_xpath('/html/body/div/div[2]/div/mat-dialog-container/app-eligible-tests/div/div[2]/mat-button-toggle-group/div').text
    print(textele)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('python.driving.port@gmail.com', 'somethingsomething')
    server.sendmail('python.driving.port@gmail.com', 'baboom16mll@gmail.com', textele)
    server.quit()
    driver.quit()
    time.sleep(900)
