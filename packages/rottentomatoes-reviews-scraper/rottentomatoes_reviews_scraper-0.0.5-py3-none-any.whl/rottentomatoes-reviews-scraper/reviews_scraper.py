# reviews_scraper.py

import time
import pprint
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from click_button import ButtonClicker
from csv_handler import CSVHandler
from maker import convert_date

class ReviewsScraper:
    def __init__(self, driver, URL, title_name, open_date, fail_counter, count_review, csv_review_filename):
        """
        ReviewsScraperクラスのコンストラクタ

        :param driver: SeleniumのWebDriverオブジェクト
        :param URL: レビューをスクレイプする対象のURL
        :param title_name: 映画のタイトル名
        :param open_date: 映画の公開日
        :param fail_counter: 失敗カウンター
        :param count_review: スクレイピングするレビューの個数
        :param csv_review_filename: レビュー情報を保存するCSVファイルの名前
        """
        self.driver = driver
        self.URL = URL
        self.title = title_name
        self.open_date = open_date
        self.fail_counter = fail_counter
        self.count_review = count_review
        self.csv_review_filename = csv_review_filename

    def scrape_reviews(self):
        """
        レビューをスクレイプするメソッド
        """
        review_columns = ["title", "open_date", "reviewer", "review_date", "evaluation", "review"]
        csv_handler = CSVHandler(review_columns)
        self.driver.get(self.URL)
        time.sleep(1)
        button_clicker = ButtonClicker(self.driver)
        
        scraped_reviews = 0
        while scraped_reviews < self.count_review:
            button_clicker.click_review_actions()
            time.sleep(2)
            scraped_reviews = self._get_reviews_info(csv_handler, scraped_reviews)
        
        csv_handler.save_to_csv(self.csv_review_filename)
        print(self.fail_counter)

    def _get_reviews_info(self, csv_handler, scraped_reviews):
        """
        レビュー情報を取得するメソッド
        """
        try:
            all_reviews = self.driver.find_elements(By.CSS_SELECTOR, ".audience-review-row")
            for review_element in all_reviews:
                if scraped_reviews >= self.count_review:
                    break
                review_dic = self._extract_review_info(review_element)
                csv_handler.add_info(review_dic)
                pprint.pprint(review_dic)
                scraped_reviews += 1
        except NoSuchElementException:
            self.fail_counter["get_inf"] += 1
        
        return scraped_reviews

    def _extract_review_info(self, review_element):
        """
        レビュー情報を抽出するメソッド

        :param review_element: レビュー情報を含むWebElement
        :return: レビュー情報の辞書
        """
        review_dic = {
            "reviewer": self._get_reviewer(review_element),
            "review_date": None,
            "evaluation": None,
            "review": None,
            "title": self.title,
            "open_date": self.open_date
        }
        review_dic["review"], review_dic["review_date"], review_dic["evaluation"] = self._get_review_info(review_element)
        return review_dic

    def _get_reviewer(self, review_element):
        """
        レビュアー名を取得するメソッド

        :param review_element: レビュー情報を含むWebElement
        :return: レビュアー名
        """
        try:
            reviewer_element = review_element.find_element(By.CSS_SELECTOR, ".audience-reviews__name")
            return reviewer_element.text.strip()
        except NoSuchElementException:
            return "Anonymous"

    def _get_review_info(self, review_element):
        """
        レビュー情報を取得するメソッド

        :param review_element: レビュー情報を含むWebElement
        :return: レビューのテキスト、日付、評価
        """
        try:
            review_text_element = review_element.find_element(By.CSS_SELECTOR, ".audience-reviews__review.js-review-text")
            review_text = review_text_element.text.strip()

            date_element = review_element.find_element(By.CLASS_NAME, "audience-reviews__duration")
            date = convert_date(date_element.text.strip())

            score_elements = review_element.find_elements(By.CSS_SELECTOR, ".star-display__filled, .star-display__half")
            score = sum(1 if "star-display__filled" in e.get_attribute("class") else 0.5 for e in score_elements)

            return review_text, date, score
        except NoSuchElementException:
            return None, None, None
