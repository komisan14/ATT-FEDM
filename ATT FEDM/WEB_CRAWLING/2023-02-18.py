from selenium import webdriver;
from bs4 import BeautifulSoup;
from selenium.webdriver.chrome.service import Service;
from selenium.webdriver.common.by import By;
from selenium.webdriver.chrome.options import Options;
from selenium.webdriver.common.action_chains import ActionChains;
from webdriver_manager.chrome import ChromeDriverManager;
import time;
import pandas as pd;


options  = Options();
options.add_experimental_option("detach", True);

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options);

driver.get('https://www.lazada.com.ph/');
driver.maximize_window();
# print("maximized")

# time.sleep(2)

driver.find_element(By.CLASS_NAME,"search-box__input--O34g").send_keys("louis vuitton bag for women");
driver.find_element(By.CLASS_NAME,"search-box__button--1oH7").click();
soup = BeautifulSoup(driver.page_source, "html.parser");
pages = driver.find_elements(By.CSS_SELECTOR, "ul.ant-pagination > li");
maxpage = int(pages[-2].text);
curpage = 1

time.sleep(2)

products= []

while curpage <= maxpage:
    soup = BeautifulSoup(driver.page_source, 'html.parser');
    for item in soup.find_all('div', class_ = 'Bm3ON'):
        product_name = item.find('div',class_ = 'RfADt').text;
        product_price = item.find('div',class_ = 'aBrP0').text;
        products.append([product_name,product_price]);
    
    time.sleep(2)
    nextbtn = driver.find_element(By.CSS_SELECTOR,".ant-pagination-next > button");
    toAction = driver.find_element(By.CLASS_NAME,"gN1t-");
    curpage = curpage + 1;
    actions = ActionChains(driver);
    actions.move_to_element(toAction).perform();
    time.sleep(6);
    actions = ActionChains(driver);
    actions.click(nextbtn); 
    actions.perform();

# print(products);
time.sleep(3);
df = pd.DataFrame(products,columns=["Product Name", "Product Price"]);
print(df);
df.to_csv("laptops_u20k");
