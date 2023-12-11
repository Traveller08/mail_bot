import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyttsx3
from data import email_objects
from email_body import get_email_body
import pyautogui as pt
from selenium.webdriver.common.keys import Keys

optObj = Options()
optObj.add_argument('--profile-directory=Profile 6')
optObj.add_argument('--user-data-dir=C:\\Users\\ankit\\AppData\\Local\\Google\\Chrome\\User Data\\')

driver = webdriver.Chrome(options=optObj)
print("intialised browser setup...")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://mail.google.com/mail/u/0/#inbox")
print("browser setup done")
#  p_tab =driver.find_elements(By.CSS_SELECTOR,'li.pointer.tab.ga-event-tracker')
try:
    email_file = 'cleaned_emails.txt'
    with open(email_file, 'r') as file:
        cleaned_emails = [line.strip() for line in file]

    for obj in cleaned_emails:
        compose_btn = driver.find_element(By.CSS_SELECTOR,'div.T-I.T-I-KE.L3')
        compose_btn.click()
        
     
        
        # Fill in the recipient's email address
        to_element = driver.find_element(By.CSS_SELECTOR,'input.agP.aFw')
        to_element.send_keys(obj)
        

        # Fill in the subject
        subject_elem = driver.find_element(By.NAME,"subjectbox")
        subject = "Application for SDE (Fresher) Role - Ankit Kumar"
        subject_elem.send_keys(subject)

        # Construct the email body with the company name
      
       
        # Fill in the email body
        email_body_elem = driver.find_element(By.CSS_SELECTOR,"div.Am.Al.editable.LW-avf")
        time.sleep(1)
        email_body_elem.click()
        email_body_elem.click()
        time.sleep(1)
        email_body_elem.send_keys(Keys.CONTROL,'v')
        time.sleep(1)

        # Send the email
        send_btn = driver.find_element(By.CSS_SELECTOR,"div.T-I.J-J5-Ji.aoO.T-I-atl.L3")
        send_btn.click()

        # Wait briefly before sending the next email
        time.sleep(5)

        
except Exception as error:
    print("Error in finding tab....")
    print(error)
finally:
    print("quiting browser...")
    driver.quit()
    
