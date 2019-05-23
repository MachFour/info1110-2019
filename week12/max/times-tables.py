
def times_tables(n):
    # this will be a list of lists
    table = []
    i = 1
    while i <= n:
        new_row = []
        j = 1
        while j <= n:
            new_row.append(i*j)
            j += 1
        table.append(new_row)
        i += 1
    return table

def print_table(table):
    for row in table:
        for number in row:
            print("{:3d} ".format(number), end='')
        print()
    print()

t = times_tables(10)
print_table(t)
