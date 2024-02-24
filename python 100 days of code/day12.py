num=int(input("enter a valid number:"))
print("The number you have entered.",num)

if(num>0):
    print("The number is positive.")
    if(num==18):
            print("Your are an adult.")
    else:
        print("Your are not an adult.")
    
elif(num==0):
    print("The number is equals to zero.")   
        
else:
    print("The number is negative.")
print("yay!")

