coins = int(input())

beer_bought = coins // 28
bottle = beer_bought

while bottle >= 3:
    beer_trade = bottle // 3
    beer_bought += beer_trade
    bottle = beer_trade + bottle % 3

print(beer_bought)