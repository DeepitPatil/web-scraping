from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import os
import shutil
import time

minDiff = input("Enter Minimum Difficulty : ")
maxDiff = input("Enter Maximum Difficulty : ")
num_probs = int(input("Enter number of problems(<=100) : "))

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome("/Users/deepitpatil/chromedriver", options=chrome_options)
driver.get("https://codeforces.com/problemset")
min_in = WebDriverWait(driver, 10).until(lambda d: d.find_element_by_name("minDifficulty"))
max_in = driver.find_element_by_name("maxDifficulty")
min_in.clear()
max_in.clear()
min_in.send_keys(minDiff)
max_in.send_keys(maxDiff)
apply = driver.find_element_by_xpath("//input[@value='Apply']")
apply.click()

links = WebDriverWait(driver, 10).until(lambda d: d.find_elements_by_tag_name("td"))
t = [x.text for x in links]
txt = [x for x in t if (len(x) == 5 or (len(x)==6 and (x[5]=="1" or x[5]=="2")) and x[1]!="x" and x[4]!="0")]
txt = txt[:num_probs]

if os.path.exists("CodeForces/"+str(minDiff)+"-"+str(maxDiff)):
    shutil.rmtree("CodeForces/"+str(minDiff)+"-"+str(maxDiff))
os.mkdir("CodeForces/"+str(minDiff)+"-"+str(maxDiff))

for pr in txt:
    problemset = pr[:4]
    label = pr[4:]
    driver.get("https://codeforces.com/problemset/problem/"+problemset+"/"+label)
    l = WebDriverWait(driver, 10).until(lambda d: d.find_element_by_class_name("title"))
    os.mkdir("CodeForces/"+str(minDiff)+"-"+str(maxDiff)+"/"+pr)
    prob = driver.find_element_by_class_name("problemindexholder")
    driver.set_window_size(1920, prob.size["height"]+1000)
    prob.screenshot("CodeForces/"+str(minDiff)+"-"+str(maxDiff)+"/"+str(pr)+"/problem.png")
    inputs = driver.find_elements_by_class_name("input")
    count = 0
    for i in inputs :
        count += 1
        f = open("CodeForces/"+str(minDiff)+"-"+str(maxDiff)+"/"+str(pr)+"/input"+str(count)+".txt", "w+")
        f.write(i.text[11:])
        f.close()
    outputs = driver.find_elements_by_class_name("output")
    count = 0
    for i in outputs :
        count += 1
        f = open("CodeForces/"+str(minDiff)+"-"+str(maxDiff)+"/"+str(pr)+"/output"+str(count)+".txt", "w+")
        f.write(i.text[12:])
        f.close()
driver.quit()