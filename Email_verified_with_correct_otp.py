import random

import time

start_time=time.time()

otp=random.randrange(1000,10000)


print("your otp is ",otp)

num=int(input("enter otp :"))

end_time=time.time()


result_time=format(end_time-start_time)


if float(result_time)>=10:
    
    print("otp session expired")
    
elif num==otp:
    
    print("email verified successfully")
    
else:
    
    print("otp does not matched try again ")

    for x in range(1,4):

        a=int(input("enter otp:"))

        if a==otp:
            
            print("email verified successfully")
            
            break

        else:
            
            print("wrong otp,going for sleep")
        
            for z in range(1,6):
                
                print(z,end=' ')
                
                time.sleep(1)
                
                print()

