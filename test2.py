#!/usr/bin/env python3

import urllib.request

# 必要なヘッダーを追加
print("Content-Type: text/html")
print()  # 空行を出力

url = "https://www.google.com"  # 任意のURLに変更できます
try:
    response = urllib.request.urlopen(url)

    # レスポンスが成功した場合の処理
    if response.status == 200:
        print("<h1>成功！</h1>")
        content = response.read()
        print(f"<p>レスポンスの内容（最初の500文字）:</p>")
        print(f"<p>{content[:500]}</p>")
    else:
        print("<h1>エラー</h1>")
        print(f"<p>ステータスコード: {response.status}</p>")
except Exception as e:
    # エラーが発生した場合
    print("<h1>エラー</h1>")
    print(f"<p>エラーメッセージ: {e}</p>")
