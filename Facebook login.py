#not working currently mayhe later
#has problem from some kind of warning module.
from selenium import webdriver
from getpass import getpass
from webdriver_manager.chrome import ChromeDriverManager
username=input("Enter your username/email-id/phone number of Facebook:")
pwd=getpass("Enter your Facebook Password:")

driver=webdriver.Chrome(ChromeDriverManager().install)
driver=webdirver.Chrome(executable_path='C:/chromedriver')
driver.get('https://www.facebook.com/')

txtusername=driver.find_element_by_id('email')
txtusername.send_keys(username)

txtpwd=driver.find_element_by_id('pass')
txtpwd.send_keys(pwd)

btnLogin=driver.find_element_by_id('u_0_d_Nc')
btnLogin.submit()
