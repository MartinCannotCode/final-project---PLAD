def two():
    print("Calculating the amount spent on the garden display.")
    print("How much is the cost of the soil?")
    soil = int(input())
    print(" How much is the flower seeds?")
    seeds = int(input())
    print("Lastly, how much is the fence?")
    fence = int(input())
    total = soil + seeds + fence
    print("And total amount spent is", total)

two()