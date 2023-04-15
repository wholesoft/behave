from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"""
find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")
"""
def page_has_loaded(driver, sleep_time = 2):
    '''
    Waits for page to completely load by comparing current page hash values.
    '''

    def get_page_hash(driver):
        '''
        Returns html dom hash
        '''
        # can find element by either 'html' tag or by the html 'root' id
        dom = driver.find_element(By.TAG_NAME,'html').get_attribute('innerHTML')
        # dom = driver.find_element_by_id('root').get_attribute('innerHTML')
        dom_hash = hash(dom.encode('utf-8'))
        return dom_hash

    page_hash = 'empty'
    page_hash_new = ''
    
    # comparing old and new page DOM hash together to verify the page is fully loaded
    while page_hash != page_hash_new: 
        page_hash = get_page_hash(driver)
        time.sleep(sleep_time)
        page_hash_new = get_page_hash(driver)
        print('<page_has_loaded> - page not loaded')

    print('<page_has_loaded> - page loaded: {}'.format(driver.current_url))


@given(u'User launches Chrome browser')
def step_impl(context):
    context.driver=webdriver.Chrome(service=Service('/path/to/chromedriver'))
    context.driver.implicitly_wait(5)

@when(u'User Opens Home page')
def step_impl(context):
    context.driver.get('https://notes.wholesoft.net')

@when(u'User clicks on login')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Login").click()

@when(u'User enters the username "{username}"')
def step_impl(context, username):
    context.driver.find_element(By.ID, "username").send_keys(username)

@when(u'User enters the password "{password}"')
def step_impl(context, password):
    context.driver.find_element(By.CLASS_NAME, "p-password-input").send_keys(password)

@when(u'User clicks Login')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, "p-button").click()
    #assert status is True 

@then(u'User successfully fails to log in')
def step_impl(context):
    #status=context.driver.find_element(By.LINK_TEXT,"Login") 
    #assert status is False
    page_has_loaded(context.driver,2)
    print("Title is: %s" % (context.driver.title))
    assert context.driver.title != "My Notes - Wholesoft Notes"
    context.driver.close()
    context.driver.quit()

@then(u'User successfully logs in')
def step_impl(context):
    page_has_loaded(context.driver,2)
    print("Title is: %s" % (context.driver.title))
    assert context.driver.title == "My Notes - Wholesoft Notes"
    context.driver.close()
    context.driver.quit()  
