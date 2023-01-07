'''
Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app

Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome_page = webdriver.Chrome()
# chrome_page.get("https://www.phptravels.net/")
# chrome_page.maximize_window()
# time.sleep(3)

# # ID
# chrome_page.find_element(By.ID, "ACCOUNT").click()
# time.sleep(3)
#
# #LinkText
# chrome_page.find_element(By.LINK_TEXT, "Customer Login").click()
# time.sleep(3)
#
# #NAME
# chrome_page.find_element(By.NAME, "email").send_keys('carmen_giol@yahoo.com')
# time.sleep(3)
#
# chrome_page.find_element(By.NAME, "password").send_keys('SuperSecretPassword!')
# time.sleep(3)
#
# #LinkText
# chrome_page.find_element(By.LINK_TEXT, "Hotels").click()
# time.sleep(3)
#
# # ID
# chrome_page.find_element(By.ID, "submit").click()
# time.sleep(3)
#
# #LinkText
# chrome_page.find_element(By.LINK_TEXT, "Tours").click()
# time.sleep(3)
#
# chrome_page.find_element(By.LINK_TEXT, "Transfers").click()
# time.sleep(3)
#
# chrome_page.find_element(By.LINK_TEXT, "Blog").click()
# time.sleep(3)
#
# chrome_page.find_element(By.LINK_TEXT, "Offers").click()
# time.sleep(3)
#
# chrome_page.find_element(By.ID, "languages").click()
# time.sleep(3)
#
# chrome_page.find_element(By.ID, "currency").click()
# time.sleep(3)

# # ID
# chrome_page.find_element(By.ID, "ACCOUNT").click()
# time.sleep(3)
#
# #LinkText
# chrome_page.find_element(By.LINK_TEXT, "Customer Login").click()
# time.sleep(2)
#
# # CSS By Tag, class and attribute
# chrome_page.find_element(By.CSS_SELECTOR, "input.form-control[placeholder=Email]").send_keys('carmen@popa.ro')
# time.sleep(2)
#
# chrome_page.find_element(By.CSS_SELECTOR, "input.form-control[placeholder=Password]").send_keys('password')
# time.sleep(2)
#
# # CSS By Tag and attribuite
# chrome_page.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
# time.sleep(2)
# chrome_page.quit()


# chrome_page.get("https://phptravels.net/api/supplier")
# chrome_page.maximize_window()
# time.sleep(2)
#
# # CSS By ID
# chrome_page.find_element(By.CSS_SELECTOR, "a#link-forgot").click()
# time.sleep(2)
#
# #CSS By class
# chrome_page.find_element(By.CSS_SELECTOR, "button.btn-close").click()
# time.sleep(2)
#
# # CSS By attribute=value
# chrome_page.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys('carmen@popa.ro')
# time.sleep(2)
#
# chrome_page.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys('Pass2')
# time.sleep(2)
#
# chrome_page.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
# time.sleep(2)

# XPATH
# chrome_page.find_element(By.XPATH, '//*[@id="currency"]').click()
# time.sleep(2)
#
# # XPATh cu metoda text()
# chrome_page.find_element(By.XPATH, "//a[text()=' EUR']").click()
# time.sleep(2)
#
# chrome_page.find_element(By.XPATH, '//*[@id="languages"]').click()

# chrome_page.find_element(By.ID, "ACCOUNT").click()
# time.sleep(2)
# chrome_page.find_element(By.LINK_TEXT, "Customer Login").click()
# time.sleep(2)
# chrome_page.find_element(By.XPATH, "//input[@type='email' and @placeholder='Email']").send_keys('a@a.ro')
# time.sleep(2)

# chrome_page.quit()

# *********************************************************************************************************************

# chrome_page1 = webdriver.Chrome()
# chrome_page1.get("https://www.techlistic.com/p/selenium-practice-form.html")
# chrome_page1.maximize_window()
# time.sleep(3)
#
# chrome_page1.find_element(By.CSS_SELECTOR, 'button#ez-accept-all').click()
# time.sleep(2)
#
# chrome_page1.find_element(By.XPATH, "//input[@name='firstname']").send_keys('Carmen')
# chrome_page1.find_element(By.XPATH, "//input[@name='lastname']").send_keys('Popa')
# chrome_page1.find_element(By.XPATH, "//input[@id='sex-1']").click()
#
# chrome_page1.find_element(By.XPATH, "//input[@id='exp-0']").click()
# chrome_page1.find_element(By.XPATH, "//input[@id='profession-1']").click()
# time.sleep(4)
#
# chrome_page1.quit()

# *********************************************************************************************************************

# chrome_page5 = webdriver.Chrome()
# chrome_page5.get("https://verlin.ro/")
# chrome_page5.maximize_window()
#
# #Class Name, Link Test, Partial Link Test
# chrome_page5.find_element(By.CLASS_NAME, "search-bar__input").send_keys('Vitamina C')
# chrome_page5.find_element(By.CLASS_NAME, "search-bar__submit").click()
# chrome_page5.find_element(By.LINK_TEXT, "Verlin").click()
# chrome_page5.find_element(By.PARTIAL_LINK_TEXT, "Produs in").click()
# time.sleep(2)
# # chrome_page5.find_elements(By.TAG_NAME, "button")[72].click()
# time.sleep(2)
# chrome_page5.quit()

