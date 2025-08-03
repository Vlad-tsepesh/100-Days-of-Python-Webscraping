from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# items = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div')
items = driver.find_elements(
    By.CSS_SELECTOR,
    "#content .event-widget ul > li > a"
)

data = {i + 1: {"name": item.text, "link": item.get_attribute("href")} for i, item in enumerate(items)}

print(data)

driver.close()
driver.quit()
