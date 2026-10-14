#Enter data first.
length=input("Enter the length of the room:\n")
width=input("Enter the room display area :\n")
price=input("What is the price per meter?\n")


#Convert to flout
l_1=float (length)
w_2=float (width)
p_3=float (price)


#Accounts
result=( l_1 * w_2 )
result_1=( result * p_3 )


#Convert to str
a=str(result)
b=str(result_1)


#Final value
print(  "Total area  :  "  +  a )
print(  "Final price :  "  +  b )
