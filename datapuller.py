# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 10:47:06 2017

@author: bmburk
"""

from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time


folder = "E:/Projects/openDotaData/"
failed = []

browser = webdriver.PhantomJS()
browser.get('https://www.dotabuff.com/heroes/')

#delay = 3
#
#try:
#    WebDriverWait(browser, delay).until(EC.presence_of_element_located(browser.find_element_by_id('IdOfMyElement')))
#    print("Page is ready!")
#except TimeoutException:
#    print("Loading took too much time!")

#username = driver.find_element_by_id("email")
#password = driver.find_element_by_id("password")
#username.send_keys("")
#password.send_keys("")
#driver.find_element_by_name("commit").click()

time.sleep(2)

for currentNum in range(1, 36):
    currentNum = str(currentNum)

    driver.get('https://brookdale.gimlet.us/sites/1511/questions/new?page=' + str(currentNum))      
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    findAlls = [["div", "class", "question"], 
            ["div", "class", "answer"], 
            ["span", "title", "Location"], 
            ["span", "title", "Asked by"], 
            ["span", "title", "Question type"], 
            ["span", "title", "Format"],
            ["span", "title", "Duration"], 
            ["span", "title", "Initials"]]
    
#    <div class='reldate asked-at span-3 last right' style='font-size:0.8em;' title='2017-05-25T18:34:00.000-04:00'>
#2017-05-25 18:34:00 -0400
#</div>
    count = 0
    for i in soup.find_all('div', { "class" : "span-18" }):
#        i = soup.find_all('div', { "class" : "span-18" })[0]
        for j in range(len(findAlls)):
            ttt = i.find_all(findAlls[j][0], {findAlls[j][1]:findAlls[j][2]})
            if len(ttt) > 0:
                responses[j].append(ttt[0].text.strip())
            else:
                responses[j].append("")
                    
        tempL = []
        temp = i.find_all("p", { "id" : "tag_list" })
        if len(temp) > 0:
            currL = temp[0].find_all('a')
            for j in range(len(currL)):
                tempL.append(currL[j].text)
            responses[8].append(",".join(tempL))
        else:
            responses[8].append("")
            
        responses[9].append(soup.find_all('div', { 'class' : 'reldate asked-at span-3 last right'})[count].text)
        count += 1
        


responsesDF = pd.DataFrame(responses).transpose().to_csv("P:\\sr analyst b burk\\20170525 Gimlet\\output.csv")


print('process completed.')
