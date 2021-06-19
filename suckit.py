import json
tickers = None
with open('crypto symbols', 'r') as f:
	tickers = json.load(f)

tickers_formatted = [ticker for ticker in tickers if 'name' in ticker and ticker['type_is_crypto'] == 1]
print(tickers_formatted)

with open('cryptos1.json', 'w') as f:
	json.dump(tickers_formatted, f)
