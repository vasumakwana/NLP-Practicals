from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.flipkart.com/")
driver.maximize_window()
try:
    popup = driver.find_element_by_css_selector("._3wFoIb.row")
    if popup.is_displayed():
        cross = driver.find_element_by_css_selector("._2KpZ6l._2doB4z")
        cross.click()
except Exception as e:
    print(e)

search = driver.find_element_by_name("q")
search.clear()
search.send_keys("Samsung Galaxy S21")
search.send_keys(Keys.RETURN)

file = open('flipkart1.txt', 'w', encoding='utf-8')

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_2kHMtA"))
    )
    main.click()
    p = driver.current_window_handle
    chwd = driver.window_handles

    for w in chwd:
        if (w != p):
            driver.switch_to.window(w)

    reviewall = driver.find_element_by_css_selector("._3UAT2v._16PBlm")
    reviewall.click()

    time.sleep(3)
    i,isExist,data = 1,True,""

    while(isExist):
        reviewdata = driver.find_elements_by_class_name("t-ZTKy")
        readmore = driver.find_elements_by_class_name("_1BWGvX")
        for p in readmore:
            p.click()

        print("------------------------------------------------------------------------------")

        for col in reviewdata:
            file.write("\n------------------------------------------------------------------------------\n" +
                       "Customer " + str(i) + "\n" + col.text +
                       "\n------------------------------------------------------------------------------\n")

            print("Customer ",i)
            print(col.text)
            print("\n------------------------------------------------------------------------------")
            i += 1

        try:
            next = driver.find_element_by_xpath("//span[text()='Next']")
            driver.execute_script("arguments[0].click();",next)
            time.sleep(3)
        except:
            print('next not found')
            isExist = False
    file.close()
except Exception as e:
    print(e)

