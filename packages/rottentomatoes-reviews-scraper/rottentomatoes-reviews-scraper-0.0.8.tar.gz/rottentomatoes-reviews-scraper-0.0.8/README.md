# Rotten Tomatoes Scraper

A Python package to scrape movie data from Rotten Tomatoes, including titles and reviews.

ロッテントマトから映画のレビューをスクレイピングするPythonパッケージです。

## Features / 特徴

- Retrieve the following fields and save them to a CSV file
  - Title
  - Release Date
  - Reviewer
  - Review Date
  - Rating
  - Review Text

- 以下のフィールドを取得しCSVファイルに保存する
  - タイトル
  - 公開日
  - レビュアー
  - レビュー日時
  - 評価
  - レビューテキスト

## Installation / インストール

To install the package, use pip:

パッケージをインストールするには、pipを使用します：

```sh
pip install rottentomatoes-reviews-scraper
```

## Usage / 使い方

After installing the package, you can use the command line interface to scrape data. Here is an example of how to use the package from the terminal:

パッケージをインストールした後、コマンドラインインターフェースを使用してデータをスクレイピングできます。

Set the number of movies to retrieve and the number of reviews to retrieve

取得する映画数と取得するレビュー数を設定します。

```sh
rottentomatoes-reviews-scraper --count_title 20 --count_review 20
```

This command will first scrape 20 movie titles and then scrape 20 reviews for each of those movies.

このコマンドは、最初に20の映画タイトルをスクレイピングし、その後各映画の20のレビューをスクレイピングします。

## Command Line Arguments / コマンドライン引数

- `--count_title`: Number of movie titles to scrape
- `--count_review`: Number of reviews to scrape per movie

- `--count_title`: スクレイピングする映画タイトルの数
- `--count_review`: 各映画ごとにスクレイピングするレビューの数

## Example / 例

Here is an example of how to run the scraper:

スクレイパーを実行する例を以下に示します：

```sh
rottentomatoes-reviews-scraper --count_title 20 --count_review 20
```