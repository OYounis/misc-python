START = 1
END   = 100

for i in range(START, END):
    out = ""
    if i % 3 == 0: out = out + "Fizz"
    if i % 5 == 0: out = out + "Buzz"
    if out == "": out = i

    print (out)