def string(l):
    string = ''
    string += "'["
    
    i = 0
    while i < len(l):
        string_val = l[i]

        if i == len(l)-1:
            format_str = "{}"
        else:
            format_str = "{}, "
        
        # Check for str types
        if type(l[i]) == str:
            string_val = "'" + string_val + "'"

        string += format_str.format(string_val)

        i+=1

    string += "]'"
    
    return string


print(string([1,2,3,4,5]))
print(string(['a','b','c']))
print(string([True]))
