import itertools
from explicit import waiter, XPATH
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


def open_browser():
    teamnumber = 3751
    PATH = r"D:\python\Space ac\US-cansat\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("http://cansat.info/plot.html")
    driver.find_element_by_id("team").send_keys(teamnumber)
    driver.find_element_by_xpath("/html/body/p[8]/button").click()
    sleep(10000)


if __name__ == "__main__":
    open_browser()
