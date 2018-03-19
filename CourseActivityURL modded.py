#! python3

#given a student overview url, this will find the
#url of all of their course activity score reports. 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import shelve, os, time
import random
os.chdir('C:\\Programs')
browser = webdriver.Chrome('C:\\Program Files (x86)\\Python36-32\\chromedriver-Windows')
browser.get('http://apexvs.com')
time.sleep(3) #for loading time
login = browser.find_element_by_name('ctl00$ContentPlaceHolder1$loginUsernameTextBox')
login.send_keys('login')
passwd= browser.find_element_by_name('ctl00$ContentPlaceHolder1$passwordTextBox')
passwd.send_keys('pass')
passwd.submit()
time.sleep(3) #for loading time
def gtdLoop(url):
    os.chdir('C:\\Programs')
    shelfFile = shelve.open('classes')
    linklist = []
    browser.get(url) #commenting out completed class thing 
##    try:
##        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageContainer"]/div/div[4]/div[1]/div/div/a')))
##        filterlink = browser.find_element_by_xpath('//*[@id="pageContainer"]/div/div[4]/div[1]/div/div/a')
##        if filterlink.text == 'FILTER':
##            filterlink.click()
##            element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageContainer"]/div/div[4]/div[1]/div/ol/li[2]/a')))
##            active = browser.find_element_by_xpath('//*[@id="pageContainer"]/div/div[4]/div[1]/div/ol/li[2]/a')
##            time.sleep(1)
##            active.click()
##    except Exception as err:
##        print('there was an error: #nofilter') #this is a joke.
##    try:
##        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageContainer"]/div/div[4]/div[1]/div/div/a')))
##        filterlink = browser.find_element_by_xpath('//*[@id="pageContainer"]/div/div[4]/div[1]/div/div/a')
##        if filterlink.text == 'Reset password':
##            element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageContainer"]/div/div[5]/div[1]/div/div/a')))
##            filterlink2 = browser.find_element_by_xpath('//*[@id="pageContainer"]/div/div[5]/div[1]/div/div/a')
##            filterlink2.click()
##            element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageContainer"]/div/div[5]/div[1]/div/ol/li[2]/a')))
##            active = browser.find_element_by_xpath('//*[@id="pageContainer"]/div/div[5]/div[1]/div/ol/li[2]/a')
##            time.sleep(2)
##            active.click()
##
##    except Exception as err:
##        print('there was an error: %s' % (err))

 

    try:
        element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.gtd.listCell'))
            )
        links = browser.find_elements_by_css_selector('.gtd.listCell')
        for x in links:
            x.click()
            handles = browser.window_handles
            popup = browser.window_handles[1]
            browser.switch_to_window(popup)
            linklist.append(browser.current_url)
            main=browser.window_handles[0]
            browser.switch_to_window(main)
            time.sleep(2)
    except Exception as err:
        print('there was an error: %s' % (err))
    cleanlist=[]
    for x in linklist:
        if x not in cleanlist:
            cleanlist.append(x)
    shelfFile[url] = cleanlist
    shelfFile.close()
##def cleanup(url):
##    os.chdir('C:\\Programs')
##    shelfFile = shelve.open('classes')
##    values= shelfFile[url]
##    
##    clean = []
##    for x in values:
##        if x not in clean:
##            clean.append(x)
##    shelfFile[url]=clean
##    shelfFile.close()
        
        


    
shelfFile2 = shelve.open('url')
values = list(shelfFile2.values())
random.shuffle(values)
print(values)

for value in values:
    gtdLoop(value)
##keys= list(shelfFile2.keys())
##for key in keys:
##    cleanup(key)
shelfFile2.close()    
