chave_api = 'MAMK7UL4ONZUQ7NS'

!pip  install alpha_vantage

import pandas as pd
from alpha_vantage.fundamentaldata import FundamentalData

import requests

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=BRL&apikey=MAMK7UL4ONZUQ7NS'
r = requests.get(url)
data = r.json()

print(data)

api_key = chave_api

fd = FundamentalData(key = api_key)

ticker = "AAPL"

financials = fd.get_income_statement_annual(symbol = ticker)

type(financials)

financials[0]

balance = fd.get_balance_sheet_annual(symbol = ticker)

balance[0]

cashflow = fd.get_cash_flow_annual(symbol = ticker)

cashflow[0]

function=CURRENCY_EXCHANGE_RATE
