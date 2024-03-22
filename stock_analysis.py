#Stonks

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]
                #1      2       3       4       5   6       7       8       9   10      11      12  13      14      15      16  17      18      19     20

def price_at(x):
    return stock_prices[x - 1]

def max_price(a,b):
    mx_stock = 0
    for x in range(a, b + 1):
        mx_stock = max(mx_stock, price_at(x))
    return mx_stock

def min_price(a,b):
    mn_stock = price_at(a)
    for x in range(a, b + 1):
        mn_stock = min(mn_stock, price_at(x))
    return mn_stock

print (price_at(3))

print (max_price(1,16))

print (min_price(1,16))