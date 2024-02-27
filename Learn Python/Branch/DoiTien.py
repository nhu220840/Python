money = int(input())

minimum_dollars = 0

minimum_dollars += money // 100 
minimum_dollars += (money % 100) // 20
minimum_dollars += (money % 20) // 10
minimum_dollars += (money % 10) // 5
minimum_dollars += (money % 5) 

print(minimum_dollars)