import datetime

class UrlMaker:
    """
    取得したタイトルURLからレビューURLを作成するクラス
    """

    def make_url(self, url):
        """
        タイトルURLからレビューURLを作成するメソッド
        """
        return url + "/reviews?type=user"

    def make_audience_url(self, titles_df):
        """
        タイトル情報を含むDataFrameからレビューURLのリストを作成するメソッド
        """
        audience_url = []
        for i in range(len(titles_df)):
            url = titles_df["title_url"][i]
            audience_url.append(self.make_url(url))
        return audience_url


def make_title_name(titles_df):
    """
    DataFrameからタイトル名のリストを作成する関数
    """
    title_names = []
    for i in range(len(titles_df)):
        title = titles_df["title"][i]
        title_names.append(title)
    return title_names

def convert_date(date_str):
    """
    日付文字列を変換する関数
    """
    date_obj = datetime.datetime.strptime(date_str, "%b %d, %Y")
    return date_obj.strftime("%Y-%m-%d")
