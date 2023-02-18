def six():
    n = int(input("Enter the number of seconds: "))

    hrs = n // 3600
    min = (n % 3600) // 60
    sec = n % 60

    print(f"{n} seconds is equal to {hrs} hours, {min} minutes, and {sec} seconds.")

six()