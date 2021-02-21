from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import os
import shutil

problemset = input("Enter contest number : ")
labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome("/Users/deepitpatil/chromedriver", options=chrome_options)
error_msg = "The requested URL was not found on this server."
if os.path.exists("CodeForces/"+problemset):
    shutil.rmtree("CodeForces/"+problemset)
os.mkdir("CodeForces/"+problemset)

for label in labels :
    driver.get("https://codeforces.com/problemset/problem/"+problemset+"/"+label)
    l = WebDriverWait(driver, 10).until(lambda d: d.find_element_by_class_name("title"))
    if (error_msg in driver.page_source) or (l.text[0] != label):
        driver.quit()
        break
    os.mkdir("CodeForces/"+problemset+"/"+label)
    prob = driver.find_element_by_class_name("problemindexholder")
    driver.set_window_size(1920, prob.size["height"]+1000)
    prob.screenshot("CodeForces/"+problemset+"/"+label+"/problem.png")
    inputs = driver.find_elements_by_class_name("input")
    count = 0
    for i in inputs :
        count += 1
        f = open("CodeForces/"+problemset+"/"+label+"/input"+str(count)+".txt", "w+")
        f.write(i.text[11:])
        f.close()
    outputs = driver.find_elements_by_class_name("output")
    count = 0
    for i in outputs :
        count += 1
        f = open("CodeForces/"+problemset+"/"+label+"/output"+str(count)+".txt", "w+")
        f.write(i.text[12:])
        f.close()