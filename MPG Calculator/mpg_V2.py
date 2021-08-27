oldMiles = float(input("How many miles at last receipt? "))
miles = float(input("How many miles at this receipt? "))
milesTravelled = miles - oldMiles

print()
print('The difference in miles is', milesTravelled)
print()

litersFilled = float(input("How many liters were filled? "))
gallons = float(litersFilled * 0.21997)

print(round(litersFilled, 2), 'liters are', round(gallons, 1), 'UK gallons')
print()

mpg = milesTravelled / gallons

print('Your car has achieved', round(mpg, 1), 'mpg since your last refill')
