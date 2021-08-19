import pandas as pd
from vantage_layer import *

class Stock():
    def __init__(self, ticker):
        self.meta = overview(ticker)

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