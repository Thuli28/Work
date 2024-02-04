# TODO
# prompt the user for amount of change owed until non-negative value provided
from cs50 import get_float

while True:
    changed_owed = get_float("Change Owed: ")
    if changed_owed >= 0:
        break
# Convert the change owed to cents
changed_owed_cents = round(changed_owed * 100)
# Initialize number of coins tp 0
num_coins = 0
# calculate number of coins needed
while changed_owed_cents > 0:
    if changed_owed_cents >= 25:
        changed_owed_cents -= 25
        num_coins += 1
    elif changed_owed_cents >= 10:
        changed_owed_cents -= 10
        num_coins += 1
    elif changed_owed_cents >= 5:
        changed_owed_cents -= 5
        num_coins += 1
    else:
        changed_owed_cents -= 1
        num_coins += 1
print(num_coins)
