marks = int(input("Enter the marks: "))

if marks < 40:
    print('fail')
elif marks >= 40 and marks <50:
    print("D")
elif marks >=50 and marks <60:
    print("C")
elif marks >60 and marks <70:
    print("B")
elif marks >70 and marks <=100:
    print("A")
else:
    print("invalid input")

x = 12

if x >= 22:
    print("false")
elif x <= 12:
    print("true")
else:
    print("does not apply!")

