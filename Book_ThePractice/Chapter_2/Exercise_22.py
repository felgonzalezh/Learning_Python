import math;

num = int(raw_input("Type an non-negative integer: "));

bool = True;
for i in range(2,int(math.sqrt(num))+1):
    if(num % i == 0):
        bool = False;
        continue;

if(bool):
    print num, " is a prime number ";
else:
    print num, " is NOT a prime number ";
    

        
