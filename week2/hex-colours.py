
#colour = int(input("Enter a color:"), 16)

# red is 255, green is 0, blue is 255
#colour = 0xff11ef
#           rrggbb
colour = 0b111111110001000111101111
#          rrrrrrrrggggggggbbbbbbbb

# each hex digit is 4 binary digits, so
# to select the last two hex digits, we
# should use 2*4 binary digits
#blue =  colour & 0b000000000000000011111111
#green = colour & 0b000000001111111100000000
blue = (colour &  0x0000ff) >> 0
green = (colour & 0x00ff00) >> 8
red = (colour & 0xff0000) >> 16

print("colour is {:#08x}".format(colour))
print()
print("blue is {:#04x}".format(blue))
print("green is {:#04x}".format(green))
print("red is {:#04x}".format(red))


