from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
login_element = driver.find_element(By.CSS_SELECTOR, ".form-signin")

login_element.find_element(By.CSS_SELECTOR, ".top").send_keys("Vlad")
login_element.find_element(By.CSS_SELECTOR, ".middle").send_keys("Cris")
login_element.find_element(By.CSS_SELECTOR, ".bottom").send_keys("vlad.cris@gmail.com")
login_element.find_element(By.CSS_SELECTOR, "button").send_keys(Keys.ENTER)

# driver.close()
# driver.quit()