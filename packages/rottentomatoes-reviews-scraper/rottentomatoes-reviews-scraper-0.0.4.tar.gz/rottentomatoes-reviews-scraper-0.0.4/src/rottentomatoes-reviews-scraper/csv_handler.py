# csv_handler.py: CSVファイルを操作するためのクラスを定義するモジュール

import pandas as pd
import os

class CSVHandler:
    def __init__(self, columns):
        """
        CSVHandlerクラスのコンストラクタ。
        新しいDataFrameを指定された列で初期化します。

        :param columns: DataFrameの列名のリスト
        """
        self.df = pd.DataFrame(columns=columns)
    
    def add_info(self, add_dict):
        """
        辞書形式のデータをDataFrameに追加するメソッド。

        :param add_dict: 追加するデータの辞書
        """
        self.df = pd.concat([self.df, pd.DataFrame([add_dict])], ignore_index=True)

    def save_file(self, file_name):
        """
        DataFrameをCSVファイルに保存するメソッド。

        :param file_name: 保存するファイルのパス
        """
        if not os.path.exists(file_name):
            self.df.to_csv(file_name, index=False)
        else:
            self.df.to_csv(file_name, mode="a", header=False, index=False)

    def save_to_csv(self, csv_title):
        """
        DataFrameを指定されたタイトルでCSVファイルに保存するメソッド。

        :param csv_title: 保存するCSVファイルの名前
        """
        file_path = os.path.join(csv_title)
        self.save_file(file_path)

    @staticmethod
    def read_csv(file_name):
        """
        CSVファイルを読み込んでDataFrameを返す静的メソッド。

        :param file_name: 読み込むCSVファイルのパス
        :return: 読み込んだデータを含むDataFrame
        """
        return pd.read_csv(file_name)