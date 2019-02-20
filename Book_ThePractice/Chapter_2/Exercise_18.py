# Sum consetive numbers

# Prompt the user for a number:
num = int(raw_input("Type a non-negative integer: "));
def adding_consecutives(num):
    sum = 0;
    sum_div = 0;
    for i in range(1,num+1):
        sum += i;
        if(sum % i == 0):
            sum_div = sum;
    print "The sum is ", sum_div;
    return sum_div;

sum_total = 0;
for i in range(1,num+1):
    sum_total += adding_consecutives(i);
print "The TOTAL sum is ", sum_total;



