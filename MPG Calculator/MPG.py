# Gather input for miles driven since last trip reset
miles_travelled = float(input("How many miles have you travelled since your last trip reset? "))
# Gather how many liters filled
liters_filled = float(input("How many liters did you fill the tank with? "))
# Convert liters into gallons
gallons = float(liters_filled) * 0.21997
print(round(liters_filled, 2),"liters are ", round(gallons, 1), "UK gallons")

mpg = miles_travelled / gallons

print("Your car has achieved ", round(mpg, 1), "mpg since your last refill")