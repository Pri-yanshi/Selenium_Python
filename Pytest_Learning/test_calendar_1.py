import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# def test_set_calendar(calendar):
#     driver,value =calendar
#     month_d=value[0]
#     year_s = value[1]
#     day_s=value[2]
#
#     driver.find_element(By.ID,"datepicker").click()
#     curr_month = driver.find_element(By.CSS_SELECTOR,".ui-datepicker-month").text
#     curr_year = driver.find_element(By.CSS_SELECTOR,".ui-datepicker-year").text
#     print(curr_year,curr_month)
#     while curr_month !=month_d and curr_year !=year_s:
#         driver.find_element(By.CSS_SELECTOR,"a[class*='datepicker-prev']").click()
#         curr_month = driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-month").text
#         curr_year = driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-year").text
#     driver.find_element(By.XPATH,"//td[@data-handler='selectDay']/a[text()='23']").click()



def test_calendar2(calendar):
    driver,value =calendar
    driver.get("https://www.path2usa.com/travel-companion/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.execute_script("window.scrollBy(0,1500);")
    # wait.until(EC.element_located_to_be_selected((By.CSS_SELECTOR,'#form-field-travel_comp_date')))
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR,'#form-field-travel_comp_date').click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div[class*='flatpickr-calendar']")))
    curr_m= driver.find_element(By.CSS_SELECTOR,".cur-month").text
    curr_y = driver.find_element(By.CSS_SELECTOR,".numInput.cur-year").text
    print(curr_m,curr_y)
    # while curr_y != 2027:
    #     driver.find_element(By.CLASS_NAME,"arrowUp").click()
    #     curr_y = driver.find_element(By.CSS_SELECTOR, "input[class*='cur-year']").text
    # print(curr_y)
    # while curr_m != 'November':
    #     driver.find_element(By.CSS_SELECTOR,".flatpickr-next-month").click()
    #     curr_m = driver.find_element(By.CSS_SELECTOR, ".cur-month").text
    # driver.find_element(By.XPATH,"//span[@aria-label='November 16, 2027']").click()


