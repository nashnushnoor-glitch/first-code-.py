#Input data converted to an integer
information=input("Enter the number of seconds for the course :\n")
transformation=int( information )

#Calculation process
hours=transformation//3600
minout=(transformation%3600)//60
secounds=transformation%60

#Calculation process
print("hours:" +"(" +str(hours) +")" + "  minout:" +"("+ str(minout) +")"+ " secounds: " +"(" +str(secounds )+")" 
