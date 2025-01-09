def binary_calculator(bin1, bin2, operator):
    
    if not (set(bin1) <= {"0", "1"} and set(bin2) <= {"0", "1"}):   #--------------------------  Makes sure that there are only 1's and 0's, and returns an error message if otherwise
        return "Error"

    decimal1 = 0
    for digit in bin1:  #----------------------------/-----------------------------------------  Converts the first binary number to its decimal equivalent
        decimal1 = decimal1 * 2 + int(digit) #------/

    decimal2 = 0
    for digit in bin2:  #---------------------------/------------------------------------------  Converts the second binary number to its decimal equivalent
        decimal2 = decimal2 * 2 + int(digit) #-----/

    if operator == '+': #-------------------/--------------------------------------------------  Performs addition if the operator is '+'
        result = decimal1 + decimal2 #-----/

    elif operator == '-':   #---------------/--------------------------------------------------  Performs subtraction if the operator is '-'
        result = decimal1 - decimal2 #-----/

    elif operator == '*':   #---------------/--------------------------------------------------  Performs multiplication if the operator is '*'
        result = decimal1 * decimal2 #-----/

    elif operator == '/':   #------------------------------------------------------------------  Performs integer division if the operator is '/'
        if decimal2 == 0:   #------------------/-----------------------------------------------  Returns "NaN" if attempting to divide by zero
            return "NaN" #                    /
        result = decimal1 // decimal2 #------/

    else:   #-----------------/---------------------------------------------------------------   Returns an error message if the operator is invalid
        return "Error" #-----/

    if result < 0 or result > 255:  #-----/----------------------------------------------------  Returns "Overflow" if the result is outside the range 0 to 255
        return "Overflow" #--------------/

    binary_result = f"{result:08b}" #----------------------------------------------------------  Converts the result back to an 8-bit binary string

    return binary_result

if __name__ == "__main__":
    bin1 = input("Enter the first binary number: ").strip() #----------------------------------  Prompts the user for the first binary number
    bin2 = input("Enter the second binary number: ").strip()    #------------------------------  Prompts the user for the second binary number
    operator = input("Enter the operation (+, -, *, /): ").strip()  #--------------------------  Prompts the user for the operation

    result = binary_calculator(bin1, bin2, operator)    #--------------------------------------  Calls the binary calculator function and stores the result
    print(f"Result: {result}")  #--------------------------------------------------------------  Prints the final result to the user