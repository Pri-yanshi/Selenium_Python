import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


console_err_list=[]
option= Options()
option.set_capability("goog:loggingPrefs",{"browser":"ALL","performance":"ALL"})     #Console log
  #Network call -performance

driver = webdriver.Chrome(options=option)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#Console log call
# time.sleep(5)
# logs = driver.get_log("browser")
# for log in logs:
#     if log["level"] == "SEVERE":
#         console_err_list.append(log["message"])
# print(console_err_list)

#Network calls
time.sleep(5)
logs = driver.get_log("performance")
for log in logs:
    # if log["level"] == "SEVERE":
    #     console_err_list.append(log["message"])
    print(log)
