# x = input("What's x? ")
# y = input("What's y? ")
# print (int(x)+int(y))

# x = int(input("What's x?"))
# y = int(input("What's y?"))
# print (x + y)

# x = float(input("What's x? "))
# y = float(input("What's y? "))
# z = round(x + y)

# print(f"{z:,}")

# x = float(input("What's x? "))
# y = float(input("What's y? "))
# z = x/y

# print(f"{z:.2f}")

def main():
    x = int(input("What's x? "))
    print("X squared is ", square(x))

def square(n):
    return pow(n,2)

main()