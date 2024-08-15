from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import paths as p
import time

import pandas as pd
headers=['JOB TITLE','COORPORATION','LOCATION','LINK']
jobs_list=[]

def get_job_list(job_key):
    browser_options=Options()
    browser_options.add_argument("--headless")
    browser_options.add_argument("--no-sandbox")
    browser_options.add_argument("--disable-dev-shm-usage")
    service=Service(p.driver_path)
    driver=webdriver.Chrome(service=service,options=browser_options)
    driver.get(p.get_url(job_key))
    
    
    
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    scroll_pause_time = 2  # Time to wait between scrolls
    
    while True:
    # Scroll down to the bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
        time.sleep(scroll_pause_time)

    # Calculate new scroll height and compare with the last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
    
    # Break the loop if no more content is loaded
        if new_height == last_height:
            break

        last_height = new_height
        
        
    wait = WebDriverWait(driver, 240)
    job_cards_list=wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/section[2]/ul")))
    
    job_cards=job_cards_list.find_elements(By.TAG_NAME,'li')
    
    for card in job_cards:
        title=card.find_element(By.CLASS_NAME,"base-search-card__title").text
        coorporation=card.find_element(By.CLASS_NAME,"base-search-card__subtitle").text
        location=card.find_element(By.CLASS_NAME,"job-search-card__location").text
        link=card.find_element(By.CLASS_NAME,'base-card__full-link').text
        
        
        jobs_list.append({
            'JOB TITLE' : title,
            'COORPORATION':coorporation,
            'LOCATION':location,
            'LINK':link
        })
    df=pd.DataFrame(jobs_list,columns=headers)
    print(df)
    return df
    
        
        
    




