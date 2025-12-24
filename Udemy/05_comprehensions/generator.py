daily_sales = [5, 10, 12, 7, 3, 6, 8]

total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups)