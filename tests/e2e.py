# setting up chrome browser on a desired page
from selenium import webdriver
from time import sleep
import sys

from selenium.webdriver.common.by import By
score = 0;
def test_scores_service(url):
    driver = webdriver.Chrome()
    # opening chrome browser on a desired page
    driver.get(url)
    # # Getting browser current page URL
    print("url: " + driver.current_url)
    sleep(5)
    scoreElement = driver.find_element(By.XPATH, "//div[@id='score']")
    score = int(scoreElement.text)
    print("scoreElement is: ",score)
    driver.refresh()
    # sleep(2)
    driver.close()
    if 1<=score<=1000:
        return True
    else:
        return False

def main_function():

    result = test_scores_service("http://127.0.0.1:5000")
    if(result == False):
        return -1
    else:
        return 0