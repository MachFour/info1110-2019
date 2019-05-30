
def do_something():
    num = 1
    odds_mod_17 = []
    evens_squared = []

    while num <= 100:
        if num % 2 == 1:
            odds_mod_17.append(num % 17)
        else:
            evens_squared.append(num*num)
        num += 1

    combined = []

    i = 0
    while i < len(evens_squared) and i < len(odds_mod_17):
        if i % 2 == 0:
            combined.append(odds_mod_17[i])
        else:
            combined.append(evens_squared[i])
        i += 1
    print(combined)

if __name__ == "__main__":
    do_something()
