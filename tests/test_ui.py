from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_add_to_cart():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get('http://localhost:5000')
    driver.find_element_by_xpath('//a[contains(@href, "/add/1")]').click()
    time.sleep(1)
    assert "sepete eklendi" in driver.page_source
    driver.quit()
