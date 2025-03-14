# Prompt the user to enter a Power Level to check if it's a Magical Potion
n = float(input("Enter a Power Level to check if the potion is a Magical Potion: "))

# Calculate the cube root of the entered number by raising it to the power of 1/3
powerLevel = n ** (1/3)

# Round the result of the cube root to the nearest integer
roundedPotion = round(powerLevel)

# Check if the cube of the rounded number equals the original number 'n'
if roundedPotion ** 3 == n:
    # If it matches, print "YES", indicating the power level is a perfect cube
    print("YES")
else:
    # If it doesn't match, print "NO", indicating it's not a perfect cube
    print("NO")