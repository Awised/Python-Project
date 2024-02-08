#This Project Will Have a Login With a Valid Details To >> Linkedin Website
 #in the end , this project will open my private website and close it after 5 secunds
#please NOTICE all my  projects will work under  "POM1 + FunctionProject "

#Test PASS


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import POM1
import FunctionProject


#driver = webdriver.Chrome("C:\\Drivers\\chromedriver.exe")
#try:
driver = webdriver.Chrome()
driver.get(POM1.Website)

time.sleep(5)
#except:

#try:
driver.maximize_window()
time.sleep(5)
#except:
FunctionProject.InsertEmail(driver, POM1.UserNameFieldByID,POM1.CorrectUserName)
# UserNameField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'session_key')))
# UserNameField.clear()
# time.sleep(5)
# #try:
# UserNameField.send_keys('awised.ca380@gmail.com')
time.sleep(5)
#except:

#try:
FunctionProject.InsertPassword (driver,POM1.PasswordFieldByID ,POM1.Password)
# password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,'session_password')))
# password.send_keys('awis4business')
time.sleep(5)
#except:

#try:
login_Button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,POM1.LogInButtonByXPATH)))
login_Button.click()
time.sleep(5)
#except:
if POM1.SuccessfulContent in str(driver.page_source):
 FunctionProject.writeToLog ('ValidDetails.Log','User Name Found-PASS')

   #print("User Name Found-PASS")
else:
    FunctionProject.writeToLog ('ValidDetails.Log','User Name not Found-FAIL')
    #print("User Name Not Found - test PASS")
driver.get_screenshot_as_file("Linkedin home page.png")

driver.quit()






