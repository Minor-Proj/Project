#importing libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# chromedriver path
PATH = "chromedriver.exe"

# initialize driver
def get_content_from_wikipedia(search_key):
    
    driver = webdriver.Chrome(PATH)

    # target website
    driver.get("https://www.wikipedia.org/")

    # find search box
    search = driver.find_element_by_id("searchInput")

    # search keys to get results
    search.send_keys(search_key)

    # pressing enter
    search.send_keys(Keys.RETURN)


    try:
        elem = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, "bodyContent"))
        )
    except:
        driver.quit()

    print(elem.text)
    # driver.quit()



if _name_ == "_main_":
    get_content_from_wikipedia("issac newton")