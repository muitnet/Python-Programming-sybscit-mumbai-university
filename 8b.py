try:
    num=int(input("Enter the number: "))
    re=100/num
except(ValueError,ZeroDivisionError):
    print("something is wrong")
else:
    print("result is:",re)