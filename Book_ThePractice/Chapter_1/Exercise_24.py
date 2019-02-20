# Write a program that accept one interger n and computes the value of n + n*n + n*n*n + n*n*n*n

# 1. input the integer
# 2. Estimate n, n*n ... n*n*n*n
# 3. Add them
num_str = raw_input("Type a non-negative integer: ");
num = int(num_str);

i = 1;
product = 1;
addition = 0;


while i < 5:
    product *= num;
    print "product", product;
    addition += product;
    i += 1; 

print "The magin number is: ", addition;

