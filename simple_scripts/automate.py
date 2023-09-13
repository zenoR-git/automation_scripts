import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#initializing gecko webdriver
browser = webdriver.Firefox()

# added an implicit waiting time of 3 seconds
browser.implicitly_wait(3)

# same as typing  the url addressbar of browser
browser.get('https://internshala.com/')

#replace email and password with your password
email = ""
password = ""

#finding and clicking on the login button of internshala page
ele1 = browser.find_element(By.CSS_SELECTOR,"button[data-target=\"#login-modal\"]")
ele1.click()

#selecting email and password fields to enter email and password
ele2 = browser.find_element(By.ID,"modal_email")
ele3 = browser.find_element(By.ID,"modal_password")
ele2.clear()
ele2.send_keys(email)
ele3.clear()
ele3.send_keys(password)

#pressing enter will send the data and log us in if the data is correct
ele3.send_keys(Keys.RETURN)

#sleep for 4 seconds so that we can see if we logged in successfully or not
time.sleep(4)

#close the browser
browser.close()