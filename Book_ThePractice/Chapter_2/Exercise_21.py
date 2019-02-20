# Arrenge of numbers
string = str();
for i in range(1,10):
    string += str(i);
    num = int(string) * 8 + i; 
    print string, "* 8 +",i," =", num;


string_2 = str();
for i in range(1,10):
    string_2 += str(i);
    num = int(string_2) * 9 + i+1; 
    print string_2, "* 9 +",i+1," =", num;

string_3 = str();
for i in range(9,1,-1):
    string_3 += str(i);
    num = int(string_3) * 9 + i-2;
    print string_3, "* 9 +",i-2," =", num;

string_4 = str();
for i in range(1,10):
    string_4 = i*str(1);
    num = int(string_4)*int(string_4);
    print string_4, "*",string_4," =", num;
    
