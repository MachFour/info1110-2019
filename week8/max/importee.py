import random

message = "I am Importee and this is my message!"
omg = "!@#$%^&*()-=_+"

def do_something():
    print(omg, omg[-1::-1], sep="""""", end="""

""") # list reverse, sep is empty string, end is two newlines!

    r = random.random() # random float between 0 and 1
    a, b = r.as_integer_ratio() # approximate as p/q, where p, q are integers
    ans = a ^ b # bitwise xor

    print("Importee: I did something and the answer was {:#04x}.".format(ans))

def say_hi_main():
    print("Importee: ooh, I am being run as a script!")
    print('''Let's do something :D''') # triple quotes are useful!
    print()

def say_hi_import():
    print("Importee: I am being imported! Yay!")
    print('I won\'t do anything yet...') # notice the escaped quote
    print()

if __name__ == "__main__":
    say_hi_main()
    do_something()
else:
    say_hi_import()

