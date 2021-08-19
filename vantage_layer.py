from pandas.core.frame import DataFrame
import requests
import pandas as pd

with open('alpha.txt') as f:
    API_KEY = f.readline()

# ------ Stock Series ---------
# TODO: Make this return in workable format
def daily(symbol, size="compact"):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}&outputsize={size}"
    r = requests.get(url)
    return r.json()

# ------ Fundamentals ----------

# Grab overview of company:
def overview(symbol) -> DataFrame:
    url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={API_KEY}"
    r = requests.get(url)
    return r.json()

# Grab Earnings:
def earnings(symbol) -> DataFrame:
    url = f"https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol}&apikey={API_KEY}"
    r = requests.get(url)
    data = r.json()
    annuals = pd.json_normalize(
        data,
        record_path = ['annualReports'],
    )
    quarterlies = pd.json_normalize(
        data,
        record_path=['quarterlyReports'],
    )
    return annuals, quarterlies

# Grab Income Statement
def income(symbol) -> DataFrame:
    url = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={API_KEY}"
    r = requests.get(url)
    data = r.json()
    annuals = pd.json_normalize(
        data,
        record_path = ['annualReports'],
    )
    quarterlies = pd.json_normalize(
        data,
        record_path=['quarterlyReports'],
    )
    return annuals, quarterlies

# Grab Balance Sheet
def balance(symbol) -> DataFrame:
    url = f"https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={API_KEY}"
    r = requests.get(url)
    data = r.json()
    annuals = pd.json_normalize(
        data,
        record_path = ['annualReports'],
    )
    quarterlies = pd.json_normalize(
        data,
        record_path=['quarterlyReports'],
    )
    return annuals, quarterlies

# Grab Cash Flow
def cash(symbol) -> DataFrame:
    url = f"https://www.alphavantage.co/query?function=CASH_FLOW&symbol={symbol}&apikey={API_KEY}"
    r = requests.get(url)
    data = r.json()
    annuals = pd.json_normalize(
        data,
        record_path = ['annualReports'],
    )
    quarterlies = pd.json_normalize(
        data,
        record_path=['quarterlyReports'],
    )
    return annuals, quarterlies