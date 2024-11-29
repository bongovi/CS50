# name = input("WHat's your name?")
# name = name.strip().title()
# first,last = name.split(" ")
# print(f"Hello, {last}")


def main():
    name = input("What's your name? ")
    hello(name)
    hello()

def hello(to="BonGovi"):
    print(f"Hello, {to}")

main()

