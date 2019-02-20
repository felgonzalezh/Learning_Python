import math;
num = 0;
while(num <= 2):
    num = int(raw_input("Type an integer greater than 2: "));

i = 1;
while (num > 2):
    print str(i)+": "+ str('{0:.3f}'.format(math.sqrt(num)));
    num = math.sqrt(num);
    i += 1;


