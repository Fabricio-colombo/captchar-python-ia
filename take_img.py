from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time

def take_img():
    try:
        url = 'https://www.portaldoconsignado.org.br/cipCaptchaImg?0.6342887347984043'
        
        chrome_options = Options()
        chrome_options.add_argument('--headless')

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)

        img_folder = "img"
        if not os.path.exists(img_folder):
            os.makedirs(img_folder)

    except Exception as e:
        print(e)   

    try:
        num = 0
        while True:
            driver.save_screenshot(os.path.join(img_folder, f'captchar{num}.png'))
            num += 1
            #time.sleep(2)
            driver.refresh()
    except Exception as e:
        print(e)
        
    finally:
        driver.quit()
take_img()
