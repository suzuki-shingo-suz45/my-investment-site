import requests
import pandas as pd

API_KEY = "39cd550cc72fd1be7c6fd8b02e2fb98c"  # 取得したAPIキーをここに入れる

# FRED APIのURL（CPIのデータ取得）
CPI_URL = f"https://api.stlouisfed.org/fred/series/observations?series_id=CPIAUCSL&api_key={API_KEY}&file_type=json"

def get_fred_data(url):
    response = requests.get(url)
    data = response.json()
    observations = data["observations"]
    
    # DataFrameに変換
    df = pd.DataFrame(observations)
    df["date"] = pd.to_datetime(df["date"])
    df["value"] = df["value"].astype(float)
    return df

# CPIデータ取得
cpi_data = get_fred_data(CPI_URL)
print(cpi_data.head())  # 取得したデータの最初の5行を表示
