import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3455468498&f_AL=true&f_E=1%2C2&f_TPR=r604800&f_WT=2"
           "&geoId=105072130&keywords=Python&location=Polska&sortBy=R")

login_btn = driver.find_element(By.XPATH, "/html/body/div[3]/header/nav/div/a[2]")
login_btn.click()

email_input = driver.find_element(By.ID, "username")
email_input.send_keys("****")

pswd_input = driver.find_element(By.ID, "password")
pswd_input.send_keys("****")

log_btn = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
log_btn.click()
time.sleep(10)

job_ad = driver.find_element(By.CSS_SELECTOR, ".scaffold-layout__list a")
job_ad.click()
apply_btn = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card span")
apply_btn.click()

driver.quit()
