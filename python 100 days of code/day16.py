k=int(input("your number is:"))
print("your number is:",k)

match k:
    
    case 0:
        print("the number is zero.")
    case 25:
        print("it is a silver jubilee.")
    case 50:
        print("it is a golden jubilee")
    case 75:
        print("it is a platinum jubilee")
    case 100:
        print("it is a century.")
    case _:
        print("it is my wedding anniversary.")