# Verify if a number is a perfect squared:


#Is a perfect squared?
def IsSquared(num_in):
    square = True;
    i = 1;
    while(i < num_in):
        if(num_in == i*i):
            square = False;           
            # Print out if it is a perfect squared
            print num_in, " is a perfect squared ";
        i += 1;
    return square;


a = True;
while a:
    # Prompt a user for a number
    num = int(raw_input("Type a non-negative integer: "));
    a = IsSquared(num);
    
    

