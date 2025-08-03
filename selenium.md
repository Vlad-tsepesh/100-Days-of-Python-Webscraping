# Selenium WebDriver - Most Used Commands (Java)

## 🧱 Setup and Initialization

| Command | Description |
|--------|-------------|
| `WebDriver driver = new ChromeDriver();` | Launches a new Chrome browser instance. |
| `System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");` | Sets the path to the ChromeDriver executable. |
| `driver.manage().window().maximize();` | Maximizes the browser window. |
| `driver.get("https://example.com");` | Opens a website URL. |

---

## 🔍 Finding Elements

| Command | Description |
|--------|-------------|
| `driver.findElement(By.id("id"))` | Finds an element by ID. |
| `driver.findElement(By.name("name"))` | Finds an element by name. |
| `driver.findElement(By.className("class"))` | Finds an element by class name. |
| `driver.findElement(By.cssSelector("css"))` | Finds an element using CSS selector. |
| `driver.findElement(By.xpath("//tag[@attr='value']"))` | Finds an element using XPath. |
| `driver.findElements(By.tagName("tag"))` | Finds multiple elements by tag name. |

---

## ⌨️ Interacting with Elements

| Command | Description |
|--------|-------------|
| `element.click();` | Clicks on the element. |
| `element.sendKeys("text");` | Types text into a textbox. |
| `element.clear();` | Clears the content of a textbox. |
| `element.getText();` | Gets the visible text of an element. |
| `element.getAttribute("value");` | Gets the value of an attribute. |

---

## 🕒 Waiting

| Command | Description |
|--------|-------------|
| `driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));` | Waits implicitly for elements to appear. |
| `WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));` | Creates an explicit wait. |
| `wait.until(ExpectedConditions.visibilityOf(element));` | Waits until element is visible. |

---

## 🧭 Navigation

| Command | Description |
|--------|-------------|
| `driver.navigate().to("https://url.com");` | Navigates to a URL. |
| `driver.navigate().back();` | Navigates back in browser history. |
| `driver.navigate().forward();` | Goes forward in browser history. |
| `driver.navigate().refresh();` | Refreshes the current page. |

---

## 🖼️ Screenshots

| Command | Description |
|--------|-------------|
| `TakesScreenshot ts = (TakesScreenshot) driver;`<br>`File src = ts.getScreenshotAs(OutputType.FILE);` | Takes a screenshot of the current page. |

---

## 📜 Alerts and Frames

| Command | Description |
|--------|-------------|
| `driver.switchTo().alert();` | Switches to an alert. |
| `driver.switchTo().frame("frameName");` | Switches to a frame by name or ID. |
| `driver.switchTo().defaultContent();` | Returns to the main document from a frame. |

---

## 🔚 Cleanup

| Command | Description |
|--------|-------------|
| `driver.close();` | Closes the current browser window. |
| `driver.quit();` | Closes all browser windows and ends session. |

---

## 🧠 Tips

- Always use **explicit waits** for dynamic content.
- Avoid `Thread.sleep()`—prefer `WebDriverWait` for stability.
- Use **Page Object Model (POM)** for better test structure.

