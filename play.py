from selenium import webdriver #ウェブドライバーにセレニウムを追加
from selenium.webdriver.common.keys import Keys #セレニウムウェブドライバーにサイト上の操作を可能にするcommonとkeyを追加
from selenium.webdriver.common.by import By #セレニウムウェブドライバーにByという位置を指定するツールを追加
from selenium.webdriver.common.service import Service #セレニウムウェブドライバーにseaviceというドライバーの補助的なツールを追加

from webdriver_manager.chrome import ChromeDriverManager #グーグルドライバーを自動で追加できるものをインストール
from selenium.webdriver.support.ui import WebDriverWait #ページがすべて読み込まれるまで待つ、待機用のモジュール
from selenium.webdriver.support import expected_conditions as EC #
from selenium.webdriver.chrome.options import Options

from openpyxl import Workbook
import time
import re
import pandas as pd
import os
import subprocess


url = "https://www.cosme.net/categories/item/800/product/"


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# Chromeオプション設定（必要なら追加）
chrome_options = Options()
chrome_options.add_argument("--headless")  # ヘッドレスモード（画面なしで実行）
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


# ChromeDriverのセットアップ
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


driver.get(url)
time.sleep(5)


data =[]


#商品名セレクタ―指定選択
title_tags = WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#keyword-product-list div.item-head > h3"))
    )

#商品名指定のセレクタ―各情報をテキストにして、titlesに格納
titles = [t.text.strip() for t in title_tags]



#価格のセレクタを選択指定
pricese_tags = WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#keyword-product-list span.price"))
)  
prices = [p.text.strip() for  p in pricese_tags]
 

      

for idx,(titles,prices) in enumerate(zip(titles,prices),start=1):
            print(f"{idx}, 商品名: {titles}, 価格: {prices}")
            data.append({"NO":idx,"商品名":titles,"価格":prices})

    

faile_path = r"C:\Users\USER\Downloads\python練習用記録.xlsx"

      
print(data)


df = pd.DataFrame(data)

df.to_excel(faile_path,sheet_name="商品リスト" ,index=False)
print("Excelファイルに書き込み完了")



faile_path




driver.quit()






