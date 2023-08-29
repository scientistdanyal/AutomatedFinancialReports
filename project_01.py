from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def download_file(index):
    try:
        file_download =  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,f"//table/tbody/tr[{index}]/td[6]/button")))
        file_download.click()
         
        
        down = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[2]/div/div/div[2]/table/tbody/tr/td[2]/a")))
        down.click()
                
        
        close_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[1]/button")))
        close_button.click()

    except:
        print(f"Error for index {i}")



chrome_options = Options()
chrome_options.add_experimental_option("prefs",{"download.default_directory":"D:\downloadfiles"})

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://financials.psx.com.pk/")
time.sleep(2)

for i in range(1, 493):
    download_file(i)


driver.quit()
