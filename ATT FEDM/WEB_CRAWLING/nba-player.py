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


options  = Options();
options.add_experimental_option("detach", True);

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options);

driver.get('https://www.nba.com/players');
driver.maximize_window();
# print("maximized")

# time.sleep(2)

soup = BeautifulSoup(driver.page_source, "html.parser");
maxpage = driver.find_element(By.CLASS_NAME, "Pagination_totalPages__jLWZ1").text;
maxpage = int(re.sub(r'\D', '', maxpage))
currpage = 1
player_row2 = []

time.sleep(3)
driver.find_element(By.ID,"onetrust-accept-btn-handler").click();
time.sleep(5)


while currpage <= maxpage: ##track page num
    time.sleep(5)
    listing = driver.find_elements(By.CLASS_NAME, "ListingCell-AllInfo ListingUnit"); #get rows

    for x in player_row:  
        player_row2.append(x.text); #append texted rows
    # print("text converted")

    nextbtn = driver.find_element(By.CLASS_NAME,"Pagination_button__sqGoH").click(); #nexpage
    actions = ActionChains(driver);
    actions.click(nextbtn);
    actions.perform();
    currpage = currpage + 1
    # print("next pageee!", currpage)




print(player_row2)


# player = []
# team = []
# number = []
# position = []
# height = []
# weight = []
# last_attended = []
# country = []



# print(player_row)


