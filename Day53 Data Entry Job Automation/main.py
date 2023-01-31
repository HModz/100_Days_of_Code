import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

form_url = "https://forms.gle/@********"
zillow_url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.58833922338867%2C%22east%22%3A-122.27831877661133%2C%22south%22%3A37.73891907720936%2C%22north%22%3A37.81164594432895%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept_Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(zillow_url, headers=headers)
website = response.text

soup = BeautifulSoup(website, "html.parser")

links = soup.select("#grid-search-results li a")
all_links = []

for link in links:
    href = link["href"]
    if "http" not in href:
        href = f"https://www.zillow.com{href}"
        all_links.append(href)
    else:
        all_links.append(href)

address_elements = soup.select("#grid-search-results li a address")
all_addresses = [address.get_text().split(" | ")[-1] for address in address_elements]

price_elements = soup.select("#grid-search-results .property-card-data div span")
all_prices = [price.get_text().split("+")[0] for price in price_elements]

driver = webdriver.Chrome()

for n in range(len(all_links)):
    driver.get(form_url)

    time.sleep(2)
    address = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()




