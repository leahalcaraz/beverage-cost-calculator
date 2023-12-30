# Test1 Date:September 29, 2023, ID: 301279925  Author: Leah  Alcaraz

firstName, lastName = input("Enter your first name and last name:").split()
sNumber = input("Enter your student number:")
fDrinkName, fUnitPrice, fQuantity = input("Enter the first drink name, unit price and quantity:").split()
sDrinkName, sUnitPrice, sQuantity = input("Enter the second drink name, unit price and quantity:").split()
print("\b")

print("First Name:", "%10s" % firstName.upper())
print("Last Name:", "%14s" % lastName.lower())
print("Student No:", "%15s" % sNumber)

fUnitPrice = float(fUnitPrice)
fQuantity = int(fQuantity)
sUnitPrice = float(sUnitPrice)
sQuantity = int(sQuantity)

fTotalCost = fUnitPrice * fQuantity
sTotalCost = sUnitPrice * sQuantity

print("=" * (40 + 3))
print("%-10s" % "Item", "%10s" % "UnitPrice", "%10s" % "Quantity", "%10s" % "Total")
print("." * (40 + 3))
print("%-10s" % fDrinkName, "%10.2f" % fUnitPrice, "%10d" % fQuantity, "%10.2f" % fTotalCost)
print("%-10s" % sDrinkName, "%10.2f" % sUnitPrice, "%10d" % sQuantity, "%10.2f" % sTotalCost)
print("=" * (40 + 3))
