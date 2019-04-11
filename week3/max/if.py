
day = "Monday"
#day = "Saturday"
coffees_needed = 0
people = 5

if day == "Monday":
    coffees_needed = people * 2
elif day == "Saturday" or day == "Sunday":
    coffees_needed = 0
else:
    coffees_needed = people * 1

print("{} coffees needed".format(coffees_needed))

coffees_made = 0
while True:
    if not (coffees_made < coffees_needed):
        break
    print("Made 1 coffee")
    coffees_made += 1

print("Finished making coffee!")



