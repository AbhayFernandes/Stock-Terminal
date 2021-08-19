import requests
import pandas as pd
import json
import csv

with open('alphavantage.txt') as f:
    API_KEY = f.readline()

# ------ Stock Series ---------

def daily(symbol, size="compact", ):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}&outputsize={size}"
    r = requests.get(url)
    return r

# ------ Fundamentals ----------

# Grab overview of company:
def overview(symbol):
    url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={API_KEY}"
    r = requests.get(url)
    return r

# Grab Earnings:
def earnings(symbol):
    url = f"https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol}&apikey={API_KEY}"
    r = requests.get(url)
    return r

# Grab Income Statement
def income(symbol):
    url = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={API_KEY}"
    r = requests.get(url)
    return r

# Grab Balance Sheet
def balance(symbol):
    url = f"https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={API_KEY}"
    r = requests.get(url)
    return r

# Grab Cash Flow
def cash(symbol):
    url = f"https://www.alphavantage.co/query?function=CASH_FLOW&symbol={symbol}&apikey={API_KEY}"
    r = requests.get(url)
    return r