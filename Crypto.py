import cryptocompare

print("BTC=BitCoin LTC=LiteCoin ZEC=ZCash Press ENTER to see current prices")
input()
prices = cryptocompare.get_price(['BTC','LTC','ZEC'],['EUR','USD'])
print(prices)
