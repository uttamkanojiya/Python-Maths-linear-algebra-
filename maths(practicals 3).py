#practical 3a
#vector product
import numpy as np
while(True):
    print("Enter choose for opeartion 1.vector product,2.dot product,3.exit")
    choose=(int)(input("Enter your choose:"))
    if choose==1:
        u=np.array([3,4,5])
        print(u)
        v=np.array([5,6,7])
        print(v)
        a=int(input("value of a:"))
        b=int(input("value of b:"))
        c=a*u+b*v
        print("au+bv vector product is:",c)
        print()
#dot product
    elif choose==2:
        t=np.array([5,3,1])
        print(t)
        r=np.array([7,8,9])
        print(r)
        alpha=(int)(input("value of alpha:"))
        beta=(int)(input("value of beta;"))
        d=np.dot(alpha,beta)
        print("Dot product is :",d)
    elif choose==3:
        print("The program is ended")
        exit()
    else:
        print("You have entered wrong input value enter again")
    
