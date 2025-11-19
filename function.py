age =int(input("enter your age"))
if(age<12):
    print("The tikets is free ")
    
elif(age>=12 and age<=60):
    user=input("Do you have membership: yes/no")
    if (user=='yes'):
        print("ticket rate is 150")
    else:
        print("ticket rate is 200")
else:
    print("the total rate is 100")
        
            
    