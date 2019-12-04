# -*- coding: utf-8 -*-
"""
Web Scraping using Selenium
"""

from selenium import webdriver

# Open firefox browser
browser = webdriver.Firefox()

# Simple CLick on webpage
browser.get('http://inventwithpython.com') # tell browser to go to webpage
linkElem = browser.find_element_by_link_text('Read Online for Free')
type(linkElem)
linkElem.click() # follows the "Read It Online" link

# Fill in a gmail login form
browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
# enter email
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('12345@email.com')

# click on next button
nextbutton = browser.find_element_by_id('identifierNext')
nextbutton.click()

passwElem = browser.find_element_by_name('password')
passwElem.send_keys('pasword12345')

# click on next button
nextbutton = browser.find_element_by_id('passwordNext')
nextbutton.click()


