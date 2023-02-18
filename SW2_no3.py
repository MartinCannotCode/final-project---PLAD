total_stock = 750
stock_price = 35.00
sellingPrice = 31.15

def seven():
    n = float(input("Numbers of shares that were sold:  "))
    if n > 750:
        print("the numbers are exceeding the total shares which is only 750 shares")
    else:
        stock = n * stock_price
        totalReceived = n * sellingPrice
        lostAmount = n * 3.75
        print("the total amount paid for the stock is ", stock)
        print("the total amount received from selling the stock is ", totalReceived)
        print("the total amount of money she lost is ", lostAmount)

seven()