## 参考したYouTube
https://www.youtube.com/watch?v=V0d_Q3Gq3-Q



# ホテル情報スクレイピングツール

このプロジェクトは、指定されたWebサイトからホテル情報をスクレイピングし、OpenAIのGPT-4を使用してデータを抽出し、結果をExcelとCSVファイルに保存するPythonスクリプトです。

## 機能

- Firecrawlを使用してWebページの内容をスクレイピング
- OpenAI GPT-4を使用してスクレイピングされたコンテンツからホテル情報を抽出
- 抽出されたデータをExcelとCSVファイルに保存

## 必要条件

- Python 3.8以上
- pip（Pythonパッケージマネージャー）

## セットアップ

1. このリポジトリをクローンまたはダウンロードします。

2. プロジェクトディレクトリに移動します：
   ```
   cd ホテル情報スクレイピングツール
   ```

3. 仮想環境を作成し、アクティベートします：
   ```
   python -m venv venv
   source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
   ```

4. 必要なパッケージをインストールします：
   ```
   pip install -r requirements.txt
   ```

5. `.env`ファイルを作成し、必要な環境変数を設定します：
   ```
   FIRECRAWL_API_KEY=あなたのFirecrawlAPIキー
   OPENAI_API_KEY=あなたのOpenAI APIキー
   ```

## 使用方法

スクリプトを実行するには、以下のコマンドを使用します：

```
python main.py
```

スクリプトは指定されたWebページからホテル情報をスクレイピングし、データを抽出して `hotels.xlsx` と `hotels.csv` ファイルに保存します。

## 注意事項

- このスクリプトは教育目的で作成されています。実際の使用にあたっては、対象Webサイトの利用規約を確認してください。
- APIキーは機密情報です。`.env`ファイルをGitにコミットしないよう注意してください。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細については`LICENSE`ファイルを参照してください。


1,217 回視聴  2024/08/08  #webscraping #chatgpt #python
Do you want to scrape data from the internet without identifying HTML components etc.? Scraping data becomes easy with Firecrawl! Even without any knowledge about the HTML structure of a website, you can build a reliable web scraper in a few minutes!

## ⭐️ Links ⭐ 
🔗  Website with hotels to scrape: https://www.python-unlimited.com/webs...
🔗 Download the Python script: https://tomstechacademy.com/web-scrap...
🔗 Firecrawl website: https://www.firecrawl.dev/
