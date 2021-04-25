from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
import time,os

webdriver = "/home/phuyalb/Desktop/chromedriver"

driver = Chrome(webdriver)
# hello

URL = 'https://www.chegg.com/auth?action=login&redirect=https%3A%2F%2Fwww.chegg.com%2Fhomework-help%2Fresearch-al-khorezmi-also-al-khwarizmi-man-whose-name-word-a-chapter-1.1-problem-1e-solution-9780132316811-exc'

driver.get(URL)

email_signin = driver.find_element_by_id('emailForSignIn')
email_signin.click()
email_signin.send_keys("dasdasd34rdadad@hotmail.com")

pass_signin = driver.find_element_by_id('passwordForSignIn')
pass_signin.click()
pass_signin.send_keys("Chegg2021")

login_button = driver.find_element_by_name('login')
login_button.click()

time.sleep(3)

open_list = driver.find_element_by_id('toc-button')
open_list.click()

time.sleep(3)


def export_to_file(i):
    file = open('file%s.html'%i,'w')
    section = driver.find_element_by_xpath('/html/body/div[3]/div[5]/div[2]/div[2]/div/div[5]/div[2]/section/section/div/section[1]')
    html = section.get_attribute('innerHTML')
    file.write(html)
    file.close()
    print(i,html)



for i in range(1,56):
    select_chapters = driver.find_element_by_xpath("/html/body/div[3]/div[5]/div[2]/div[2]/div/div[5]/div[2]/section/nav/ol/li[%s]" % str(i))
    select_chapters.click()
    for sub_ch in range(1,15):
        try:
            select_sub_ch = driver.find_element_by_xpath("/html/body/div[3]/div[5]/div[2]/div[2]/div/div[5]/div[2]/section/nav/ol/li[%s]/ol/li[%s]" % (str(i),str(sub_ch)))
            select_sub_ch.click()
            file_name =str(i)+":"+str(sub_ch)
            print(file_name)
            time.sleep(3)
            export_to_file(file_name)
            time.sleep(3)
        except:
            break
            time.sleep(3)
    time.sleep(3)
