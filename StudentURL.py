#! python3
#Finds the url of all the student homepages in apex
#searches through apex and clicks every single student, then records name/url info.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import shelve, os, time
os.chdir('C:\\Programs')
shelfFile = shelve.open('url')


#login
browser = webdriver.Chrome('C:\\Program Files (x86)\\Python36-32\\chromedriver-Windows')
browser.get('http://apexvs.com')
time.sleep(3) #for loading time
login = browser.find_element_by_name('ctl00$ContentPlaceHolder1$loginUsernameTextBox')
login.send_keys('login')
passwd= browser.find_element_by_name('ctl00$ContentPlaceHolder1$passwordTextBox')
passwd.send_keys('pass')
passwd.submit()
time.sleep(3) #for loading time

#open student link page 1

for x in range(15):
    browser.get('https://www.apexvs.com/lms/#!cm2/Students')
    browser.switch_to_frame(browser.find_element_by_id("cm2ContentFrame"))
    link = browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ViewStudentsControl_studentAccountList_cell_%s_2"]/div/a' % (x))
    link.click()
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageContainer"]/div/div[2]/label')))
    header = browser.find_element_by_xpath('//*[@id="pageContainer"]/div/div[2]/label')
    name = header.text
    url = browser.current_url
    name = name[9:]
    shelfFile[name]=url
    print(name)
    print(url)

#page 2

def arrowcount(z):
    for amount in range(1,z+1):
        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ViewStudentsControl_studentAccountList_footer"]/table/tbody/tr/td[1]/div/a[5]')))
        arrow = browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ViewStudentsControl_studentAccountList_footer"]/table/tbody/tr/td[1]/div/a[5]')
        arrow.click()
        
for y in range(1,21):
    try:
        for x in range(15):
            browser.get('https://www.apexvs.com/lms/#!cm2/Students')
            element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "cm2ContentFrame")))
            browser.switch_to_frame(browser.find_element_by_id("cm2ContentFrame"))
            element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ViewStudentsControl_studentAccountList_footer"]/table/tbody/tr/td[1]/div/a[5]')))
            arrow = browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ViewStudentsControl_studentAccountList_footer"]/table/tbody/tr/td[1]/div/a[5]')
            arrowcount(y)
            link = browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ViewStudentsControl_studentAccountList_cell_%s_2"]/div/a' % (x+(15*y)))
            link.click()
            element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageContainer"]/div/div[2]/label')))
            header = browser.find_element_by_xpath('//*[@id="pageContainer"]/div/div[2]/label')
            name = header.text
            url = browser.current_url
            name = name[9:]
            shelfFile[name]=url
            print(name)
            print(url)
    except Exception as err:
            print('An exception happened: ' + str(err))
shelfFile.close()
