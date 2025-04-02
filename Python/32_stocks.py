stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at_day_x(x):
    return stock_prices[x-1]

def max_price(a,b):
    maximum = 0
    for i in range(a,b+1):
        maximum = max(maximum, price_at_day_x(i))
    return maximum

def min_price(a,b):
    minimum = price_at_day_x(a)
    for i in range(a,b+1):
        minimum = min(minimum, price_at_day_x(i))
    return minimum

print(stock_prices[3])
print(max_price(1,4))
print(min_price(1,4))