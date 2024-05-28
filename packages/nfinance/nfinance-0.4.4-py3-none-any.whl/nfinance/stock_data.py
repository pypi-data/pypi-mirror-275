
from datetime import datetime
import requests
import pandas as pd

class StockDataDownloader:
    def __init__(self, ticker, start_date, end_date, interval='day'):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval
        self.base_url = self.set_base_url()

    def set_base_url(self):
        if self.ticker.isdigit() and len(self.ticker) == 6:
            return "https://api.stock.naver.com/chart/domestic/item/"
        else:
            return "https://api.stock.naver.com/chart/foreign/item/"

    def download(self):
        start_datetime = datetime.strptime(self.start_date, '%Y-%m-%d')
        end_datetime = datetime.strptime(self.end_date, '%Y-%m-%d')
        start_str = start_datetime.strftime('%Y%m%d') + "0000"
        end_str = end_datetime.strftime('%Y%m%d') + "2359"

        url = f"{self.base_url}{self.ticker}/{self.interval}?startDateTime={start_str}&endDateTime={end_str}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return self.parse_data(data)
        else:
            raise Exception(f"Failed to fetch data: {response.status_code}")

    @staticmethod
    def parse_data(data):
        df = pd.DataFrame(data)
        df['localDate'] = pd.to_datetime(df['localDate'])
        df.set_index('localDate', inplace=True)

        columns = {
            'closePrice': 'Close',
            'openPrice': 'Open',
            'highPrice': 'High',
            'lowPrice': 'Low',
            'accumulatedTradingVolume': 'Volume'
        }

        # Check if 'foreignRetentionRate' is in the data
        if 'foreignRetentionRate' in df.columns:
            columns['foreignRetentionRate'] = 'ForeignHold'

        df.rename(columns=columns, inplace=True)

        # Convert relevant columns to numeric
        numeric_columns = ['Close', 'Open', 'High', 'Low', 'Volume']
        if 'ForeignHold' in df.columns:
            numeric_columns.append('ForeignHold')

        df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)

        return df
