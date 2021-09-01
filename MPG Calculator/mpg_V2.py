# Gather odometer reading from previous receipt
oldMiles = float(input("How many miles at previous receipt? "))
# Gather odometer reading at current receipt
miles = float(input("How many miles at this receipt? "))
# Calculate difference
milesTravelled = miles - oldMiles

# Output difference between odometer readings
print()
print('The difference in miles is', milesTravelled)
print()

# Gather amount filled in liters
litersFilled = float(input("How many liters were filled? "))
# Convert to gallons
gallons = float(litersFilled * 0.21997)

# Output conversion of liters to gallons
print(round(litersFilled, 2), 'liters are', round(gallons, 1), 'UK gallons')
print()

# Calculate mpg
mpg = milesTravelled / gallons

# Output mpg calculation
print('Your car has achieved', round(mpg, 1), 'mpg since your last refill')
