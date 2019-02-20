import math;
# This programm finds the roots for a quadratic equation:

print "This program finds the roots for a quadratic equation Ax2 + Bx + C = 0";
a = int(raw_input("Type the parameter A= "));
b = int(raw_input("Type the parameter B= "));
c = int(raw_input("Type the parameter C= "));

root = b*b - 4*a*c;

if(root < 0):
    print "The solution is an imaginary number ";
    root_i = math.sqrt(abs(root))*1j;
    x1 = (-b+root_i)/(2*a);
    x2 = (-b-root_i)/(2*a);
    print "One root: ", '{0:.2f}'.format(x1);
    print "Second root: ", '{0:.2f}'.format(x2);
elif(root == 0):
    x1 = -b/(2*a);
    print "There is only ONE root: ", x1;
else:
    x1 = (-b+math.sqrt(root))/(2*a);
    x2 = (-b-math.sqrt(root))/(2*a);
    print "One root: ", '{0:.2f}'.format(x1);
    print "Second root: ", '{0:.2f}'.format(x2);


    
