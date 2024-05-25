from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class ButtonClicker:
    """
    ウェブページのボタンをクリックするクラス
    """
    def __init__(self, driver):
        self.driver = driver

    def click_button(self, class_name):
        """
        指定されたクラス名のボタンをクリックするメソッド
        """
        try:
            btn = self.driver.find_element(By.CLASS_NAME, class_name)
            btn.click()
        except NoSuchElementException:
            print("クリック失敗")
            pass

    def click_title_actions(self):
        """タイトルアクションボタンをクリックするメソッド"""
        self.click_button("discovery__actions")

    def click_review_actions(self):
        """レビューアクションボタンをクリックするメソッド"""
        self.click_button("load-more-container")
