# receive kilometers to drive from user

kmdrive = float(input("How many kilometers do you have to drive: "))

# receive liters-per-kilometer usage of the car from user

ltrperkm = float(input("What is the liters-per-kilometer usage of the car: "))

# receive price per liter of fuel from user

priceltr = float(input("What is the price of fuel per liter: "))

# calculate the cost of the trip
# calculate the amount of liters required for the trip

litersreq = kmdrive * ltrperkm

# caluclate the price of fuel

price = litersreq * priceltr

# display cost to user

print(f"The total cost of the trip is ${price}")