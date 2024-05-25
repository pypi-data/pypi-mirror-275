# titles_scraper.py

import time
import pprint
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from click_button import ButtonClicker
from csv_handler import CSVHandler
from maker import convert_date

class TitlesScraper:
    def __init__(self, driver, URL, fail_counter, csv_title_filename, count_title):
        """
        TitlesScraperクラスのコンストラクタ

        :param driver: SeleniumのWebDriverオブジェクト
        :param URL: タイトルをスクレイプする対象のURL
        :param fail_counter: 失敗カウンター
        :param csv_title_filename: タイトル情報を保存するCSVファイルの名前
        :param count_title: スクレイピングするタイトルの個数
        """
        self.driver = driver
        self.URL = URL
        self.fail_counter = fail_counter
        self.csv_title_filename = csv_title_filename
        self.count_title = count_title

    def scrape_titles(self):
        """
        タイトル情報をスクレイプするメソッド
        """
        title_columns = ["title", "open_date", "title_url"]
        csv_handler = CSVHandler(title_columns)
        self.driver.get(self.URL)
        time.sleep(1)
        button_clicker = ButtonClicker(self.driver)
        
        scraped_titles = 0
        while scraped_titles < self.count_title:
            button_clicker.click_title_actions()
            time.sleep(2)
            scraped_titles = self._get_title_info(csv_handler, scraped_titles)
        
        csv_handler.save_to_csv(self.csv_title_filename)
        print(self.fail_counter)

    def _get_title_info(self, csv_handler, scraped_titles):
        """
        タイトル情報を取得するメソッド
        """
        try:
            all_titles = self.driver.find_elements(By.CSS_SELECTOR, "a[data-qa='discovery-media-list-item-caption']")
            for title_element in all_titles:
                if scraped_titles >= self.count_title:
                    break
                title_dic = self._extract_title_info(title_element)
                csv_handler.add_info(title_dic)
                pprint.pprint(title_dic)
                scraped_titles += 1
        except NoSuchElementException:
            self.fail_counter["get_inf"] += 1
        
        return scraped_titles

    def _extract_title_info(self, title_element):
        """
        タイトル情報を抽出するメソッド

        :param title_element: タイトル情報を含むWebElement
        :return: タイトル情報の辞書
        """
        title_dic = {"title": None, "open_date": None, "title_url": None}
        try:
            title_text_element = title_element.find_element(By.CSS_SELECTOR, "span[data-qa='discovery-media-list-item-title']")
            title_dic["title"] = title_text_element.text.strip()

            open_date_element = title_element.find_element(By.CSS_SELECTOR, "span[data-qa='discovery-media-list-item-start-date']")
            open_date_text = open_date_element.text.strip()
            if open_date_text.startswith("Opened "):
                open_date_text = open_date_text.replace("Opened ", "")
            elif open_date_text.startswith("Streaming "):
                open_date_text = open_date_text.replace("Streaming ", "")
            title_dic["open_date"] = convert_date(open_date_text)

            title_dic["title_url"] = title_element.get_attribute("href")
        except NoSuchElementException:
            pass

        return title_dic
