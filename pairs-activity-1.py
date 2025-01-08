# def name(first,last):
#     print(f'{first.title()}, {last.title()}')

# name("Thayer", "Yang")

# name("Yang", "Thayer")

# name(last="Yang",first="Thayer")

def calulate_time(velocity,distance):
    if velocity > 0:
        time = distance / velocity
        print(f"at {velocity} mph, it will take {time:.2f} hours to travel {distance} miles")
    else:
        print("Error: Velocity is 0 or negative")

calulate_time(distance=350,velocity=80)