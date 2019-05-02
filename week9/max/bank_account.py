
# note the camel case
class BankAccount:
    # class/static variable 'interest_rate' initialised to 2.
    interest_rate = 2 # percent per annum

    # the constructor - run separately for each instance
    # initialises instance variables 'name' and 'balance'
    def __init__(self, name, initial_balance=0):
        self._name = name
        self._balance = initial_balance

    def name(self):
        return self._name

    def balance(self):
        return self._balance


    # controlled access to the balance
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount can't be negative")
        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdraw amount can't be negative")
        self._balance -= amount


    # calculates simple interest
    def interest_per_month(self):
        return self._balance*self.get_interest_rate()/12

    # A concise but complete string representation of an instance
    # It should contain all important information about the instance
    # Used when printing in a list.
    def __repr__(self):
        s = "'{}': ${:.2f} (r={:f}%p.a.)"
        return s.format(self.name, self.balance, BankAccount.rate)

    # A 'readable' string representation of an instance
    # Used when calling print() and str()
    def __str__(self):
        format_string = "Bank account: name '{}', balance: ${:.2f}"
        return format_string.format(self.name, self.balance)


    # These methods operate on the whole class, not any particular instance
    @classmethod
    def update_interest_rate(cls, rate):
        cls.interest_rate = rate

    @classmethod
    # we can use a 'getter' method to create complex behaviour without changing
    # the variables used.
    def get_interest_rate(cls, month):
        if month == 12:
            return cls.interest_rate*1.5 # christmas bonus interest rate
        else:
            return cls.interest_rate # usual interest rate


if __name__ == ":__main__":
    # some sample usage
    a = BankAccount("Nabi", 5000)
    b = BankAccount("Rong", 10000)
    print("Printing individual bank accounts, using __str__:")
    print(a) # same as print(str(a)), str(a) is the same as a.__str__()
    print(b) # same as print(str(b))
    print("Printing a list of bank accounts, using __repr__:")
    print([a, b]) # uses __repr__ instaad

    # getting data

