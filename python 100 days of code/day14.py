#match case statement
x=int(input("enter a number:"))
print("The number that you have entered:",x)
match x:
    case 0:
        print("the number is zero.")
    case 100:
        print("The number is equals to hundred.")
    case _ if x!=50:
        print(x ,"is not equals to 50.")
    case _ if x!=30:
        print(x,"is not equals to 30")
    case _:
        print(x)