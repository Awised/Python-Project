from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import NewPom
import POM1
#POM = 1
#Valid Details
def InsertEmail (drive,EmailName, Mail):
    UserNameField = WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.NAME, EmailName)))
    UserNameField.clear()
    time.sleep(5)
    UserNameField.send_keys(Mail)



#POM = 2
#Invalid Password
def InsertPassword (drive,PasswordName , Password):
     PassW = WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.NAME,PasswordName)))
     PassW.clear()
     PassW.send_keys(Password)
     time.sleep(3)


from datetime import datetime


 def writeToLog (LogFile,textToWrite):
    f = open ('LogFile','a')
    timeStamp = str(datetime.datetime.now())
    f.write (timeStamp+""+ textToWrite + '\n')
    f.close()
























