
## if and else ##
# if -> else -> elif. Show bug if elif is replaced by if
today = "Monday"
people = 5
coffees_needed = 0

if today == "Monday":
    coffees_needed = people*2
elif today == "Saturday" or today == "Sunday":
    # no one's at work on the weekend
    coffees_needed = 0
else:
    coffees_needed = people*1



## while ##
# as is -> convert to while True. Show need to update condition var

coffees_made = 0
while coffees_made < coffees_needed:
    print("Make another coffee")
    coffees_made += 1

print("Finished making coffees")
