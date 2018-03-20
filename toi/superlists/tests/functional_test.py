from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#browser = webdriver.Chrome()
browser = webdriver.Firefox()
browser.get('http://localhost:9000')

assert 'Django' in browser.title
