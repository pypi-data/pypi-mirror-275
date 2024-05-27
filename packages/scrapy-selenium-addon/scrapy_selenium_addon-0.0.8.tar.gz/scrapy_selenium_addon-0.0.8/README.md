# Scrapy with Selenium

The Scrapy middleware to handle JavaScript pages using Selenium.

## Installation
```
$ pip install git+https://github.com/sakarimov/scrapy-selenium-addon
```
You should use **Python>=3.6**.
You will also need one of the Selenium [compatible browsers](https://selenium-python.readthedocs.io/installation.html#drivers).

## Configuration
1. Add the browser to use and the arguments to pass to the executable to the Scrapy settings:
```python
SELENIUM_DRIVER_NAME = "firefox"
SELENIUM_DRIVER_ARGUMENTS=["-headless"]  # "--headless' if using Chrome instead of Firefox
```

In order to use a remote Selenium driver, specify `SELENIUM_COMMAND_EXECUTOR`:
```python
SELENIUM_COMMAND_EXECUTOR = "http://localhost:4444/wd/hub"
```

2. Add the `SeleniumMiddleware` to the downloader middlewares:

```python
DOWNLOADER_MIDDLEWARES = {
"scrapy_selenium.SeleniumMiddleware": 543
}
```

## Usage
Use the `scrapy_selenium.SeleniumRequest` instead of the Scrapy built-in `Request` like below:
```python
from scrapy_selenium import SeleniumRequest

yield SeleniumRequest(url=url, callback=self.parse_result)
```
The request will be handled by Selenium, and the request will have an additional `meta` key, named `driver` containing the Selenium driver with the request processed.
```python
def parse_result(self, response):
    print(response.request.meta["driver"].title)
```
For more information about the available driver methods and attributes, refer to the [Selenium with Python documentation](https://selenium-python.readthedocs.io/api.html#webdriver-api).

The `selector` response attribute works as usual (but contains the HTML processed by the Selenium driver).
```python
def parse_result(self, response):
    print(response.selector.xpath("//title/@text"))
```

### Additional arguments
The `scrapy_selenium.SeleniumRequest` accepts 4 additional arguments:

#### `wait_time`/`wait_until`

When used, Selenium will perform an [Explicit wait](http://selenium-python.readthedocs.io/waits.html#explicit-waits) before returning the response to the spider.
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

yield SeleniumRequest(
    url=url,
    callback=self.parse_result,
    wait_time=10,
    wait_until=EC.element_to_be_clickable((By.ID, "someid"))
)
```

#### `screenshot`
When used, Selenium will take a screenshot of the page, and the binary data of the .png captured will be added to the response `meta`:
```python
yield SeleniumRequest(
    url=url,
    callback=self.parse_result,
    screenshot=True
)

def parse_result(self, response):
    with open("image.png", "wb") as image_file:
        image_file.write(response.meta["screenshot"])
```

#### `script`
When used, Selenium will execute custom JavaScript code.
```python
yield SeleniumRequest(
    url=url,
    callback=self.parse_result,
    script="window.scrollTo(0, document.body.scrollHeight);"
)
```
