# main.py

import argparse
from webdriver_manger_driver import webdriver_manager
from titles_scraper import TitlesScraper
from reviews_scraper import ReviewsScraper
from csv_handler import CSVHandler
from maker import UrlMaker

def scrape_titles(csv_title_filename, count_title, fail_counter):
    """
    映画のタイトル情報を取得し、CSVファイルに保存する関数

    :param csv_title_filename: タイトル情報を保存するCSVファイルの名前
    :param count_title: スクレイピングするタイトルの個数
    :param fail_counter: 失敗カウンター
    """
    driver = webdriver_manager()
    URL = "https://www.rottentomatoes.com/browse/movies_at_home/sort:popular"
    scraper = TitlesScraper(driver, URL, fail_counter, csv_title_filename, count_title)
    scraper.scrape_titles()
    driver.quit()

def scrape_reviews(csv_title_filename, count_review, csv_review_filename, fail_counter):
    """
    映画のレビュー情報を取得し、CSVファイルに保存する関数

    :param csv_title_filename: タイトル情報を含むCSVファイルの名前
    :param count_review: スクレイピングするレビューの個数
    :param csv_review_filename: レビュー情報を保存するCSVファイルの名前
    :param fail_counter: 失敗カウンター
    """
    driver = webdriver_manager()
    titles_df = CSVHandler.read_csv(csv_title_filename)
    url_maker = UrlMaker()
    for _, row in titles_df.iterrows():
        title_url = row["title_url"]
        title_name = row["title"]
        open_date = row["open_date"]
        audience_url = url_maker.make_url(title_url)
        scraper = ReviewsScraper(driver, audience_url, title_name, open_date, fail_counter, count_review, csv_review_filename)
        scraper.scrape_reviews()
    driver.quit()

def main():
    parser = argparse.ArgumentParser(description="Scrape Rotten Tomatoes movie data.")
    parser.add_argument("--count_title", type=int, default=20, help="Number of titles to scrape.")
    parser.add_argument("--count_review", type=int, default=3, help="Number of reviews to scrape per title.")
    args = parser.parse_args()

    fail_counter = {"main": 0, "get_inf": 0, "get_inf_for": 0}
    
    csv_title_filename = "./titles.csv"
    scrape_titles(csv_title_filename, args.count_title, fail_counter)

    csv_review_filename = "./reviews.csv"
    scrape_reviews(csv_title_filename, args.count_review, csv_review_filename, fail_counter)

if __name__ == "__main__":
    main()
