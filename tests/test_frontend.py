from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://localhost:5500/frontend/index.html")

time.sleep(3)

title = driver.title
assert title == "Carlos Villa's Resume", f"Title does not match. Found: {title}"
print("Title matches successfully.")

counter_element = driver.find_element(By.ID, "counter")
assert counter_element is not None, "Counter element not found."
print("Counter element found successfully.")

print("Test passed successfully!")

driver.quit()