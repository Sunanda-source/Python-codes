e,n,w,s=map(int,input().split())
x=e-w
y=n-s
if((x>0)and(y>0)):
    print("North East")
if((x<0) and(y>0)):
    print("North West")
if((y<0)and(x<0)):
    print("South West")
if((y<0)and(x>0)):
    print("South East")
if((x==0)and(y==0)):
    print("Original Point")
if((x>0) and(y==0)):
    print("East")
if((y>0)and(x==0)):
    print("North")
if((x<0)and(y==0)):
    print("South")
if((x==0)and(y<0)):
    print("West")
