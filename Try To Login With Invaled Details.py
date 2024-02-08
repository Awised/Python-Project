#This Project Will TRY to login with an IVALID Details To >> Linkedin Website

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import FunctionProject
import POM1
import POM2


#driver = webdriver.Chrome("C:\\Drivers\\chromedriver.exe")
#try:
driver = webdriver.Chrome()
driver.get(POM1.Website)

time.sleep(5)
#except:

#try:
driver.maximize_window()
time.sleep(5)
FunctionProject.InsertEmail(driver, POM1.UserNameFieldByID,POM1.IncorrectUserName)

# #except:
# UserNameField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'session_key')))
# UserNameField.clear()
# time.sleep(5)
# #try:
# UserNameField.send_keys('awis4business@gmail.com')
time.sleep(5)
#except:

#try:
password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,POM1.PasswordFieldByID)))
password.send_keys(POM1.IncorrectPassword)
time.sleep(5)
#except:

#try:
login_Button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')))
login_Button.click()
time.sleep(5)
#except:
if POM1.IncorrectUserContent in str(driver.page_source):
  FunctionProject.writeToLog ('InvalidUserName.Log','User Name Found-PASS')

    #print("User Name Found-PASS")
else:
    FunctionProject.writeToLog ('InvalidUserNmae.Log','User Name not Found-FAIL')


    #print("User Name Not Found - test PASS")
driver.get_screenshot_as_file("Linkedin home page.png")

driver.quit()




