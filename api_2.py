#!/usr/bin/env python3
import cgi
import json
import requests

# FRED APIキー（取得したものを設定）
FRED_API_KEY = "39cd550cc72fd1be7c6fd8b02e2fb98c"

# 投資対象のFREDコード
FRED_SERIES = {
    "dow": "DJIA",  # ダウ平均
    "sp500": "SP500",  # S&P 500
    "nasdaq": "NASDAQCOM",  # ナスダック
    "nikkei": "NIKKEI225",  # 日経平均
    "gold": "GOLDPMGBD228NLBM",  # ゴールド
    "ust10y": "DGS10",  # 米国10年債利回り
    "usdjpy": "DEXJPUS",  # ドル円為替
    "bitcoin": "CBBTCUSD"  # ビットコイン
}

# 期間のパラメータ設定
PERIOD_MAPPING = {
    "3m": "90",  # 3ヶ月
    "6m": "180",  # 6ヶ月
    "1y": "365",  # 1年
    "3y": "1095"  # 3年
}

# CGIパラメータ取得
print("Content-Type: application/json")
print()

form = cgi.FieldStorage()
period = form.getvalue("period", "3m")

# APIクエリ期間の取得
days = PERIOD_MAPPING.get(period, "90")

# 各投資対象のデータ取得
def get_fred_data(series_id):
    url = f"https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "observation_start": "2024-01-01"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json().get("observations", [])
        # '.' ではない値だけを処理
        return [(obs["date"], float(obs["value"])) for obs in data if "value" in obs and obs["value"] != "."]
    else:
        return []


# データ取得＆加工
data = []
for name, series_id in FRED_SERIES.items():
    observations = get_fred_data(series_id)
    if observations:
        base_value = observations[0][1]  # 初日を基準値とする
        values = [{"date": obs[0], "change": (obs[1] - base_value) / base_value * 100} for obs in observations]
        data.append({"name": name, "values": values})

# JSONレスポンスを出力
print(json.dumps(data))
#!/usr/bin/env python3
import cgi
import json
import requests

# FRED APIキー（取得したものを設定）
FRED_API_KEY = "39cd550cc72fd1be7c6fd8b02e2fb98c"

# 投資対象のFREDコード
FRED_SERIES = {
    "dow": "DJIA",  # ダウ平均
    "sp500": "SP500",  # S&P 500
    "nasdaq": "NASDAQCOM",  # ナスダック
    "nikkei": "NIKKEI225",  # 日経平均
    "gold": "GOLDPMGBD228NLBM",  # ゴールド
    "ust10y": "DGS10",  # 米国10年債利回り
    "usdjpy": "DEXJPUS",  # ドル円為替
    "bitcoin": "CBBTCUSD"  # ビットコイン
}

# 期間のパラメータ設定
PERIOD_MAPPING = {
    "3m": "90",  # 3ヶ月
    "6m": "180",  # 6ヶ月
    "1y": "365",  # 1年
    "3y": "1095"  # 3年
}

# CGIパラメータ取得
print("Content-Type: application/json")
print()

form = cgi.FieldStorage()
period = form.getvalue("period", "3m")

# APIクエリ期間の取得
days = PERIOD_MAPPING.get(period, "90")

# 各投資対象のデータ取得
def get_fred_data(series_id):
    url = f"https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "observation_start": "2024-01-01"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json().get("observations", [])
        # '.' ではない値だけを処理
        return [(obs["date"], float(obs["value"])) for obs in data if "value" in obs and obs["value"] != "."]
    else:
        return []


# データ取得＆加工
data = []
for name, series_id in FRED_SERIES.items():
    observations = get_fred_data(series_id)
    if observations:
        base_value = observations[0][1]  # 初日を基準値とする
        values = [{"date": obs[0], "change": (obs[1] - base_value) / base_value * 100} for obs in observations]
        data.append({"name": name, "values": values})

# JSONレスポンスを出力
print(json.dumps(data))
