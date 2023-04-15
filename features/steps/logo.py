from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

@given(u'launch chrome browser')
def launchBrowser(context):
    #context.driver=webdriver.Chrome('/Users/mini/Documents/GitHub/pycucumber/drivers/chromedriver')
    context.driver=webdriver.Chrome(service=Service('/path/to/chromedriver'))


@when(u'open Wholesoft Notes home page')
def openHomePage(context):
    context.driver.get('https://notes.wholesoft.net')


@then(u'verify that the logo is present on the page')
def verifyLogo(context):
    status=context.driver.find_element(By.CLASS_NAME,"logo") # fails?
    #status=context.driver.find_element(By.LINK_TEXT,"Login"). # fails?

    assert status is True
    


@then(u'close the browser')
def closeBrowser(context):
    context.driver.close
    #pass
