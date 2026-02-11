from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

import time

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@type='search']").send_keys('ber')
expected = ['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actual = []
#time.sleep(2) # Implicit wait would not work for find_elements(Plural) , if we did not use timeSleep then selenium proceed with empty List[]
# wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='products']/div")))
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div") #list[]
for result in results:
   result.find_element(By.XPATH,"div/button").click()  # results contain chain process(parent to child)
   actual.append(result.find_element(By.CSS_SELECTOR,'.product-name').text)
print(actual)
if actual == expected:
    print("PASS")
assert actual == expected, 'appended to actual list'
# I got StaleElementReferenceException: Don’t store WebElement for long time,Because page refreshes or updates DOM,Stored element becomes invalid (stale).
# results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
# carts = driver.find_elements(By.XPATH,"//button[@type='button'][normalize-space()='ADD TO CART']")
# for i in range(len(results)):  #range(len(results))
#     print(i)
#     carts[i].click()


driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//div[@class='action-block']/button").click()

promo= wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".promoCode")))
promo.send_keys("rahulshettyacademy")

# driver.find_element(By.XPATH,'//input[@class="promoCode"]').send_keys("rahulshettyacademy") #instead of "input[class='promoCode']" use promoCode or input.promoCode
driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.promoInfo')))
# print(driver.find_element(By.CSS_SELECTOR,'.promoInfo').text)
#driver.close()


# #sum validation
prices = driver.find_elements(By.CSS_SELECTOR,"tbody tr td:nth-child(5)")

s = 0
for price in prices:
    s=s+int(price.find_element(By.CSS_SELECTOR,'.amount').text)
print(s)
tAmt = float(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert s == tAmt
DAmt=float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
if tAmt > DAmt:
    print('pass')
# assert tAmt > DAmt, f"{DAmt} should be less than {tAmt}"
