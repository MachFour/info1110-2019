def swap(x, y):
    tmp = x
    x = y
    y = tmp

    return (x,y) # Tuple of x,y

# Function will take a list containing 2 values, and swap their positions
def swap_lst(lst):
    if len(lst) < 2:
        print("Did not provide list with 2 values")
        return
    
    tmp = lst[0]
    lst[0] = lst[1]
    lst[1] = tmp

a = 3
b = 5

# print("Before swap: a:{}, b:{}".format(a,b))
# a,b = swap(a,b)
# print("After swap: a:{}, b:{}".format(a,b))

new_list = [1,9]
print(new_list) # [1,9]
swap_lst(new_list)
print(new_list) # [9,1]
