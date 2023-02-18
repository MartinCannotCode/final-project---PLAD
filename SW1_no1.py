def one():
    print("How much did the Little League Baseball Team spend to purchase new baseballs last year?")
    price = int(input())
    print("How many did they buy?")
    quantity = int(input())
    total = price*quantity
    print("Then, the total amount spent is ", total)

one()