# 🚀 Selenium WebDriver in Python – Step-by-Step Guide with Commands

## ✅ Step 1: Install Dependencies

```bash
pip install selenium
```

Install browser driver (optional, but recommended):

```bash
pip install webdriver-manager
```

---

## ✅ Step 2: Setup and Initialization

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Maximize window and set implicit wait
driver.maximize_window()
driver.implicitly_wait(10)
```

---

## ✅ Step 3: Open a Web Page

```python
driver.get("https://example.com")
```

---

## ✅ Step 4: Locate Elements

```python
from selenium.webdriver.common.by import By

# Find elements using different locators
driver.find_element(By.ID, "element_id")
driver.find_element(By.NAME, "element_name")
driver.find_element(By.CLASS_NAME, "class_name")
driver.find_element(By.TAG_NAME, "input")
driver.find_element(By.CSS_SELECTOR, ".my-class input[name='q']")
driver.find_element(By.XPATH, "//input[@name='q']")
```

---

## ✅ Step 5: Interact with Elements

```python
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium WebDriver")
search_box.clear()

submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

# Read text or attributes
text = search_box.text
value = search_box.get_attribute("value")
```

---

## ✅ Step 6: Wait for Elements

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)

# Wait for an element to be visible
element = wait.until(EC.visibility_of_element_located((By.ID, "result")))
```

---

## ✅ Step 7: Handle Alerts and Frames

### Handle Alert

```python
alert = driver.switch_to.alert
alert.accept()
```

### Switch to Frame

```python
driver.switch_to.frame("frame_name")
driver.switch_to.default_content()
```

---

## ✅ Step 8: Navigation

```python
driver.get("https://site.com/page1")
driver.back()
driver.forward()
driver.refresh()
```

---

## ✅ Step 9: Take Screenshot

```python
driver.save_screenshot("screenshot.png")
```

---

## ✅ Step 10: Close Browser

```python
driver.close()  # Close current tab
driver.quit()   # Quit entire browser
```

---

## ✅ Best Practices

- Use `WebDriverWait` instead of `time.sleep()` for stable automation.
- Use `webdriver-manager` to auto-manage browser drivers.
- Organize automation using **Page Object Model (POM)**.
- Separate test logic from configuration and page definitions.

---

## 📌 Summary Table

| Task              | Command Example |
|-------------------|-----------------|
| Open Page         | `driver.get(url)` |
| Find Element      | `driver.find_element(By.ID, "id")` |
| Click Element     | `element.click()` |
| Enter Text        | `element.send_keys("text")` |
| Clear Input       | `element.clear()` |
| Get Text          | `element.text` |
| Get Attribute     | `element.get_attribute("attr")` |
| Explicit Wait     | `WebDriverWait(...).until(...)` |
| Screenshot        | `driver.save_screenshot("file.png")` |
| Close Browser     | `driver.quit()` |

---