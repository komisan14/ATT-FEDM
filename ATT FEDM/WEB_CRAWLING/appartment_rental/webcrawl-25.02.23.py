from selenium import webdriver;
from bs4 import BeautifulSoup;
from selenium.webdriver.chrome.service import Service;
from selenium.webdriver.common.by import By;
from selenium.webdriver.chrome.options import Options;
from selenium.webdriver.common.action_chains import ActionChains;
from webdriver_manager.chrome import ChromeDriverManager;
import time;
import pandas as pd;
import re;

# *open window

options  = Options();
options.add_experimental_option("detach", True);
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options);

driver.get('https://www.lamudi.com.ph/apartment/rent/'); # *link to open
driver.maximize_window(); # *maximize the window

# * data to get : 
# *title, location, price, key-info : bedroom, bath, floor area, agent


# ! step 1 : get max page and curr page


soup = BeautifulSoup(driver.page_source, "html.parser");
page = driver.find_element(By.CLASS_NAME, "nav-box-center").find_element(By.TAG_NAME ,'select');

curr_page = page.get_attribute('data-pagination-current');
max_page = page.get_attribute('data-pagination-end');

print(curr_page, max_page)


while curr_page <= max_page: ##track page num
    time.sleep(5)
    
   