# An explicit wait makes WebDriver wait for a certain condition to occur before proceeding further with execution.
# An explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code.
# The extreme case of this is time.sleep(), which sets the condition to an exact time period to wait.
# There are some convenience methods provided that help you write code that will wait only as long as required.
# WebDriverWait in combination with ExpectedCondition is one way this can be accomplished.

# An implicit wait makes WebDriver poll the DOM for a certain amount of time when trying to locate an element
# or elements if they are not immediately available.
# An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find
# any element (or elements) not immediately available.
# The default setting is 0 (zero). Once set, the implicit wait is set for the life of the WebDriver object.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get(url='http://automationpractice.com/index.php')
# driver.find_element(By.ID, value="search_query_top").send_keys('blouse')
# time.sleep(1)
# driver.find_element(By.ID, value='newsletter-input').send_keys('andr3y92_d@yahoo.com')
# time.sleep(1)
# driver.get(url='https://formy-project.herokuapp.com/form')
# first_name = driver.find_element(By.ID, value='first-name')
# first_name.send_keys('Andrei')
# time.sleep(1)
# driver.get(url='https://formy-project.herokuapp.com/')
# link_text = driver.find_element(By.LINK_TEXT, 'Autocomplete').click()
# time.sleep(1)
# driver.get(url='https://formy-project.herokuapp.com/')
# driver.find_element(By.LINK_TEXT, 'Checkbox').click()
# time.sleep(1)
# driver.get(url='https://formy-project.herokuapp.com/')
# driver.find_element(By.LINK_TEXT, 'Buttons').click()
# time.sleep(1)
# driver.get(url='https://formy-project.herokuapp.com/')
# driver.find_element(By.PARTIAL_LINK_TEXT, 'Enabled').click()
# time.sleep(3)
# driver.get(url='https://formy-project.herokuapp.com/')
# driver.find_element(By.PARTIAL_LINK_TEXT, 'Mouse').click()
# time.sleep(1)
# driver.get(url='https://formy-project.herokuapp.com/')
# driver.find_element(By.PARTIAL_LINK_TEXT, 'Complete').click()
# time.sleep(1)
# driver.get(url='http://www.seleniumframework.com/practiceform/')
# driver.find_element(By.NAME, 'country').send_keys('Romania')
# time.sleep(3)
# driver.get(url='http://www.seleniumframework.com/practiceform/')
# driver.find_element(By.NAME, 'email').send_keys('andr3y92_d@yahoo.com')
# time.sleep(1)
# driver.find_element(By.NAME, value='company').send_keys('IT Factory')
# time.sleep(1)
# driver.get(url='https://formy-project.herokuapp.com/form')
# driver.find_element(By.TAG_NAME, 'select').send_keys(0)
# time.sleep(2)
# driver.get(url='https://formy-project.herokuapp.com/form')
# # driver.find_element(By.TAG_NAME, 'input').send_keys('Andrei-Gabriel')
# input_list = driver.find_elements(By.TAG_NAME, 'input')
# input_list[0].send_keys('Andrei-Gabriel')
# time.sleep(1)
# input_list[1].send_keys('Dumitrascu')
# time.sleep(2)
# driver.get(url='http://www.seleniumframework.com/practiceform/')
# button_list = driver.find_elements(By.TAG_NAME, 'button')
# button_list[0].click()
# time.sleep(1)
# button_list[1].click()
# time.sleep(1)
# driver.get(url='https://formy-project.herokuapp.com/form')
# form_control_list = driver.find_elements(By.CLASS_NAME, 'form-control')
# form_control_list[0].send_keys('A-G')
# form_control_list[1].send_keys('D')
# form_control_list[2].send_keys('qa tester')
# time.sleep(2)
# driver.get(url='https://formy-project.herokuapp.com/form')
# selectors by CSS ID
# driver.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys('Mar')
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, 'select#select-menu').send_keys(2)
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, 'input#datepicker').send_keys('09/07/2022')
# time.sleep(2)
# # selectors by CSS Class -only first if multiple matches
# driver.get(url='https://formy-project.herokuapp.com/form')
# driver.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('ia')
# time.sleep(2)
# driver.get(url='http://automationpractice.com/index.php')
# driver.find_element(By.CSS_SELECTOR, 'input.search_query').send_keys('clothes')
# time.sleep(2)
# # selectors by CSS atribut=valoare
# driver.get(url='https://formy-project.herokuapp.com/form')
# driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter last name"]').send_keys('Dum')
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter your job title"]').send_keys('qa automation engineer')
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, 'input[value="radio-button-2"]').click()
# time.sleep(2)
# # selectors by CSS atribut=valoare partiala + parinte -->copil
# driver.get(url='https://formy-project.herokuapp.com/form')
# driver.find_element(By.CSS_SELECTOR, 'div input[placeholder*="last name"]').send_keys('Dumitrascu')
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, 'div input[value="checkbox-1"]').click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, 'div input[placeholder="mm/dd/yyyy"]').send_keys('09/07.2022')
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, 'div a[role="button"]').click()
# time.sleep(2)
# selectors by XPATH atribut=valoare
# driver.get(url='https://formy-project.herokuapp.com/form')
# driver.find_element(By.XPATH, '//input[@id="first-name"]').send_keys('A')
# time.sleep(1)
# driver.find_element(By.XPATH, '//input[@id="radio-button-2"]').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//input[@value="checkbox-1"]').click()
# time.sleep(1)
# # selectors by XPATH * toate elementele care respecta regula
# driver.get(url='https://formy-project.herokuapp.com/form')
# driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('Andrei')
# time.sleep(1)
# driver.find_element(By.XPATH, '//*[@id="select-menu"]').send_keys(2)
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@value="radio-button-3"]').click()
# time.sleep(2)
# driver.get(url='https://formy-project.herokuapp.com/form')
# driver.find_element(By.XPATH, '//*[@value="radio-button-3"]').click()
# time.sleep(1)
#  selectors by XPATH navigare in jos - trecem prin toate elementele
# driver.get(url='https://formy-project.herokuapp.com/form')
# driver.find_element(By.XPATH, '//div/div/input[@id="first-name"]').send_keys('Gabriel')
# time.sleep(1)
# # selectors by XPATH navigare in jos - skip tags - cautam oriunde sub form un input care sa respecte regula
# driver.get(url='https://formy-project.herokuapp.com/form')
# driver.find_element(By.XPATH, '//form//input[@id="first-name"]').send_keys('ei')
# time.sleep(1)
# selectors by XPATH - selectare elemente din lista - indexul incepe de la 1
# driver.get(url='https://formy-project.herokuapp.com/form')
# driver.find_element(By.XPATH, '(//input[@class="form-control"])[2]').send_keys('Dumitrascu')
# time.sleep(1)
# driver.find_element(By.XPATH, '(//input[@type="radio"])[1]').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '(//input[@aria-label="checkbox"])[1]').click()
# time.sleep(1)
# selectors by XPATH - OR primul gasit dintre variante
# driver.get(url='https://formy-project.herokuapp.com/form')
# s = driver.find_element(By.XPATH, '//input[@id="last-name1"] | //input[@id="last-name2"] | //input[@id="last-name"]')
# # # stergem valorile din input
# # s.clear()
# # time.sleep(1)
# s.send_keys('Dumitrascu')
# time.sleep(1)
# t = driver.find_element(By.XPATH, '//input[@id="checkbox-1"] | //input[@id="checkbox-2"] | //input[@id="checkbox-3"]')
# t.click()
# time.sleep(2)
# selectors by XPATH - in functie de textul partial + luam textul de pe el cu proprietatea text
# driver.get(url='https://formy-project.herokuapp.com/form')
# partial_text = driver.find_element(By.XPATH, '//a[contains(text(),"Sub")]').text
# print(partial_text)
# select_option = driver.find_element(By.XPATH, '//select/option[contains(text(),"Select")]').text
# print(select_option)
# # selectors by XPATH - in functie de textul vizibil
# driver.get(url='https://the-internet.herokuapp.com/')
# text_selector1 = driver.find_element(By.XPATH, '//a[text()="A/B Testing"]')
# text_selector1.click()
# time.sleep(2)
# driver.get(url='https://the-internet.herokuapp.com/')
# text_selector2 = driver.find_element(By.XPATH, '//a[text()="Broken Images"]')
# text_selector2.click()
# time.sleep(2)
# driver.get(url='https://the-internet.herokuapp.com/')
# text_selector3 = driver.find_element(By.XPATH, '//a[text()="Drag and Drop"]')
# text_selector3.click()
# time.sleep(2)
# driver.get(url='https://the-internet.herokuapp.com/')
# partial_text = driver.find_element(By.XPATH, '//a[contains(text(), "Context")]')
# partial_text.click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//a[text()="Submit"]').click()
# time.sleep(2)
# driver.get(url='https://formy-project.herokuapp.com/form')
# element_by_parent = driver.find_elements(By.XPATH, '//*[@type="text"]//parent::div')
# print(f"The text inside the element is: {element_by_parent[0].text}")
# time.sleep(2)
# driver.get(url='https://formy-project.herokuapp.com/form')
# element_by_sibling = driver.find_element(By.XPATH, '//*[@type="text"]//parent::div/following-sibling::div')
# print(f"The text inside the element is: {element_by_sibling.text}")
# time.sleep(2)
# //label[text()="First name"]/parent::strong/folowing-sibling::input/preceding-sibling::strong
driver.get(url='https://formy-project.herokuapp.com/form')
t = driver.find_element(By.XPATH, '//input/preceding-sibling::strong').text
print(t)
s = driver.find_element(By.XPATH, '//label[text()="First name"]/parent::strong').text
print(s)
# b = driver.find_element(By.XPATH, '//label[text()="Highest level of education"]').text
# print(b)
# driver.find_element(By.XPATH, '//input[@id="radio-button-2"]/parent::div').click()
# time.sleep(1)
# XPATH - axis navigation
'''
x y axis navigation
cu parent in sus
cu /elem_tipe - ajungem la elementul copil
cu //elem_type - cauta prin toti descendentii
cu parent::elem_type in sus
cu folowing-sibling::elem_type -urmatorul frate de la acelasi nivel
cu preceding-sibling::elem_type - fratele anterior de la acelasi nivel
//label[text()="First name"]/parent::strong/folowing-sibling::input/preceding-sibling::strong
'''
# cu ajutorul unei functii cand avem foarte multe elemente de acelasi tip
# si vrem sa parametrizam selectorul
# driver.get(url='https://formy-project.herokuapp.com/form')
#
# def formy_input(placeholder_text, input_value):
#     input = driver.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]')
#     input.clear()
#     input.send_keys(input_value)
#
# formy_input(placeholder_text='Enter first name', input_value='Andrei-Gabriel')
# time.sleep(1)
# formy_input(placeholder_text='Enter last name', input_value='Dumitrascu')
# time.sleep(1)
# formy_input(placeholder_text='Enter your job title', input_value='QA Automation Engineer')
# time.sleep(1)
driver.get(url='http://www.seleniumframework.com/practiceform/')
def formy_practice_input(placeholder, input_value):
    input = driver.find_element(By.XPATH, f'//input[@placeholder="{placeholder}"]')
    input.clear()
    input.send_keys(input_value)
formy_practice_input(placeholder='E-mail *', input_value='andr3y92_d@yahoo.com')
time.sleep(1)