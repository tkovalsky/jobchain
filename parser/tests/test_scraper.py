from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/in/satyanadella/")

print(driver.title)
driver.quit()