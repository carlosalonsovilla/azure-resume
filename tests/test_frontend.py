from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.carlosalonsovilla.com")

time.sleep(3)

# Test 1: Check title
title = driver.title
assert title == "Carlos Villa's Resume", f"Title does not match. Found: {title}"
print("Title matches successfully.")

# Test 2: Check if the counter exists
counter_element = driver.find_element(By.ID, "counter")
assert counter_element is not None, "Counter element not found."
print("Counter element found successfully.")

# Test 3: Check if Linkedin link is present and correct
linkedin = driver.find_element(By.CSS_SELECTOR, "a[href='https://www.linkedin.com/in/carlos-villa-63236927b/']")
assert linkedin is not None, "Linkedin link not found."
print("Linkedin list found successfully.")

# Test 4: Check if Github link is present and correct
github = driver.find_element(By.CSS_SELECTOR, "a[href='https://github.com/carlosalonsovilla/azure-resume']")
assert github is not None, "Github link not found."
print("Github link found successfully.")

# Test 5: Check if profile image is present
profile_pic = driver.find_element(By.CSS_SELECTOR, "img[src='images/me.png']")
assert profile_pic is not None, "Profile Picture was not found."
print("Profile image found successfully")


print("Test passed successfully!")

driver.quit()