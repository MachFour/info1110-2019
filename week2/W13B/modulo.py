import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

remainder = n % m

#print("after dividing", n, "by", m, "the remainder is", remainder)

print("After dividing {} by {}, the remainder is {}".format(n, m, remainder))
