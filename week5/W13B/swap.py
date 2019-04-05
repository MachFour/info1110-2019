# We pass by VALUE
def swap(x,y):
    tmp = x
    x = y
    y = tmp
    return x,y

# We pass by REFERENCE for passing a list
def swap_list(l):
    if len(l) < 2:
        print("Please pass in a list with 2 values")
        return
    
    tmp = l[0]
    l[0] = l[1]
    l[1] = tmp

a = 3
b = 5
l = [1,9]
# print("Before swap, a:{}, b:{}".format(a,b))
#a,b= swap(a,b)
#print("After swap, a:{}, b:{}".format(a,b))
print(l)
swap_list(l)
print(l)

