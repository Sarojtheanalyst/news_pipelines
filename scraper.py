import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from config import BAJAR_URL, NEPALI_URL


class NewsScraper:
    def __init__(self):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=options)
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # BAJAR KO CHIRFAR
    def scrape_bajar(self):
        news_list = []

        self.driver.get(BAJAR_URL)
        time.sleep(5)

        for i in range(1, 6):
            try:
                url = self.driver.find_element(
                    By.XPATH,
                    f"/html/body/div[1]/section/div/div[2]/div[{i}]/article/a[2]"
                ).get_attribute("href")

                self.driver.get(url)
                time.sleep(2)

                title = self.driver.title
                news = self.driver.find_element(
                    By.XPATH,
                    "/html/body/div[1]/div[1]/div/div[1]/main/div/div[1]/article/div"
                ).text

                news_list.append({
                    "title": title,
                    "news": news,
                    "source": "Bajar ko Chirfar",
                    "timestamp": self.timestamp
                })

            except:
                continue

        return news_list

   
    # NEPALI PAISA

    def scrape_nepali_paisa(self):
        news_list = []

        self.driver.get(NEPALI_URL)
        time.sleep(5)

        urls = []

        for i in range(1, 5):
            try:
                url = self.driver.find_element(
                    By.XPATH,
                    f"/html/body/section[1]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[2]/div[{i}]/div/a"
                ).get_attribute("href")
                urls.append(url)
            except:
                continue

        for url in urls:
            try:
                self.driver.get(url)
                time.sleep(2)

                title = self.driver.title
                news = self.driver.find_element(By.ID, "newsBody").text

                news_list.append({
                    "title": title,
                    "news": news,
                    "source": "Nepali Paisa",
                    "timestamp": self.timestamp
                })

            except:
                continue

        return news_list

    def close(self):
        self.driver.quit()