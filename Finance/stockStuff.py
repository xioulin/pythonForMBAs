from yahoofinancials import YahooFinancials

tickers= ["GM","F","RIVN","TSLA","HMC"]

yahoo_financials= YahooFinancials(tickers)
balance_sht_data_qt= yahoo_financials.get_financial_stmts('quarterly','balance')
print(balance_sht_data_qt.values())