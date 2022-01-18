numb1=(int (input("enter your first number: ")))
numb2=(int(input("enter your second number: ")))

action=str(input("choose action: Add(a), sub(s), mult(m), div(d) "))
if action == "a":
    print(numb1 + numb2)
elif action == "s":
    print(numb1 - numb2)
elif action == "m":
    print(numb1 * numb2)
elif action == "d":
    print(numb1 / numb2)
else:
    print("invalid!")
    print("try again,\n.")