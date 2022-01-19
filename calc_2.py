values = ('24', "32", "18", "71")
print("use BOADMAS to solve the question. ")
print(str("SOLVE (24*32+71/18)"))

print("possible actions include; \n mult(*), \n add(+),\n div(/):")
action=(str(input("enter first action to be executed: ")))
if action== "*":
    numb1= print(int(input("enter first value to be multiplied: ")))
    numb2= print(int(input("enter second value to be multiplied: ")))
    print(numb1*numb2)

elif action != "*":
    print("not the first action!\n Try again! ")
else:
    print('proceed')
action2=(str(input("enter next action: ")))

if numb1 == "24":
    numb2 = print(int(input("enter the second value: ")))
    