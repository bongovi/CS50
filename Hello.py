name = input("WHat's your name?")
name = name.strip().title()
first,last = name.split(" ")
print(f"Hello, {last}")