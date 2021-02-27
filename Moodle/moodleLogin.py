from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import getpass

username = input("username : ")
password = getpass.getpass("password : ", stream=None)

driver = webdriver.Chrome("/Users/deepitpatil/chromedriver")
driver.get("https://moodle.iitd.ac.in/login/index.php")

username_input = WebDriverWait(driver, 10).until(lambda d: d.find_element_by_id("username"))
username_input.clear()
username_input.send_keys(username)

password_input = driver.find_element_by_id("password")
password_input.clear()
password_input.send_keys(password)

login = driver.find_element_by_id("login")
captcha = str(login.text).splitlines()[-2].split()

captcha_answer = ""
if captcha[1] != "enter" :
    a = int(captcha[2])
    b = int(captcha[4])
    solve = {"add" : a+b, "subtract" : a-b}
    captcha_answer = solve[captcha[1]]
else :
    a = int(captcha[4])
    b = int(captcha[6])    
    solve = {"first" : a, "second" : b}
    captcha_answer = solve[captcha[2]]

captcha_input = driver.find_element_by_id("valuepkg3")
captcha_input.clear()
captcha_input.send_keys(captcha_answer)

loginbtn = driver.find_element_by_id("loginbtn")
loginbtn.click()