import time
import requests
import selenium.webdriver.common.devtools.v112.runtime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

web = 'https://www.bezrealitky.com/'
driver.get(web)

try:
    # wait up to 10 seconds for the pop-up to appear
    popup = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "CybotCookiebotDialog")))

    # close the pop-up by clicking the close button
    close_button = popup.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[4]/div[1]/div[2]/button[4]')
    close_button.click()

except selenium.webdriver.common.devtools.v112.runtime.ExceptionDetails:
    print("No pop-up appeared")

finally:

    driver.implicitly_wait(5)
    # To check if : I WANT - is set to Rent,  --------------------------------------------------------------------------
    I_want_dropbox = driver.find_element(by=By.XPATH,
                                         value='//*[@id="__next"]/main/section[1]/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/button')
    I_want_dropbox.click()
    I_want_drop = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/section[1]/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/button/span[2]')
    if I_want_drop.text == 'I’m selling':
        driver.find_element(by=By.XPATH, value='//*[@id="PRONAJEM"]').click()
    else:
        pass
    # To check if : I LOOK FOR - Flat,----------------------------------------------------------------------------------
    driver.implicitly_wait(5)
    I_look_for_dropbox = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/section[1]/div/div/div[2]/div[1]/div/div/div[1]/div/div[2]/button')
    I_look_for_dropbox.click()
    I_look_for_drop = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/section[1]/div/div/div[2]/div[1]/div/div/div[1]/div/div[2]/button/span[2]')
    if I_look_for_drop.text != 'Flat':
        driver.find_element(by=By.XPATH, value='//*[@id="BYT"]').click()
    else:
        pass

# Fill Where do I want to look for flat:
where_element_input = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/section[1]/div/div/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/label/input')
where_element_input.send_keys('Vinohrady, Praha, okres Hlavní město Praha, Hlavní město Praha, Praha, Česko')
where_element_second_input = driver.find_element(by=By.XPATH, value='//*[@id="react-autowhatever-1--item-0"]/button/span[2]/span')
where_element_second_input.click()


# Fill For how much will rent go (The amount of money in CZK)
for_element = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/section[1]/div/div/div[2]/div[1]/div/div/div[1]/div/div[4]/button').click()
for_element_input = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/section[1]/div/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div/div/div[2]/input')
for_element_input.send_keys(27000)
for_element_input.send_keys(Keys.RETURN)
# Submitting the search
driver.find_element(by=By.XPATH,value='// *[ @ id = "__next"] / main / section[1] / div / div / div[2] / div[1] / div / div / div[2] / a').click()

# wait for the search results to load
search_results = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.PropertyCard_propertyCardContent__yVdlW")))

# get all the property card elements
property_cards = driver.find_elements(By.CSS_SELECTOR, "div.PropertyCard_propertyCardContent__yVdlW")

print(property_cards)
# iterate over each property card element and extract the data
try:
    for card in property_cards:
        # extract the data from the card element
        link = card.find_element(By.CSS_SELECTOR, "h2.PropertyCard_propertyCardHeadline__y3bhA > a").get_attribute('href')
        size = card.find_element(by=By.CLASS_NAME, value='FeaturesList_featuresList__W4KSP').text
        price = int(card.find_element(by=By.CLASS_NAME, value='PropertyPrice_propertyPriceAmount___dwT2').text.strip('CZK ').replace(',', '')) + int(card.find_element(by=By.CLASS_NAME, value='PropertyPrice_propertyPriceAdditional__gMCQs').text.strip('+ CZK ').replace(',', ''))
        print(f'Link:{link}\nPrice:{price}\nSize:{size.strip()}')
except ValueError:
    pass

finally:
    pass


