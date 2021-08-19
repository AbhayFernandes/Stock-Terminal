import pandas as pd
import pickle
from vantage_layer import *
from pathlib import Path

root = Path(".")
universe_path = root / "universe"
class Stock():
    def __init__(self, ticker):
        self.meta = overview(ticker)
        self.ticker = ticker

        self.earn_a, self.earn_q = earnings(ticker)
        self.income_a, self.income_q = income(ticker)
        self.balance_a, self.balance_q = balance(ticker)
        self.cash_a, self.cash_q = cash(ticker)

        self.generate_big_dfs()

    
    def generate_big_dfs(self):
        self.df_a = self.earn_a.merge(right=self.income_a, on="fiscalDateEnding")
        self.df_a = self.df_a.merge(right=self.balance_a, on="fiscalDateEnding")
        self.df_a = self.df_a.merge(right=self.cash_a, on="fiscalDateEnding")

        self.df_q = self.earn_q.merge(right=self.income_q, on="fiscalDateEnding")
        self.df_q = self.df_q.merge(right=self.balance_q, on="fiscalDateEnding")
        self.df_q = self.df_q.merge(right=self.cash_q, on="fiscalDateEnding")
    
    def add(self):
        path = universe_path / f"{self.ticker}.pickle"
        with open(path, 'wb') as f:
            pickle.dump(self, f)