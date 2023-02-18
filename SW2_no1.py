def five():
    distance = float(input("What is the distance in feet?"))
    speed = float(input("what is the speed in miles per hour?"))

    seconds = distance / speed * 1.46667

    answer = f'the distance is {distance} feet and the speed is {speed} miles per hour, so the aswer is {seconds} seconds.'
    print(answer)

five()