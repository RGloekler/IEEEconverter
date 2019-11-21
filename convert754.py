# Ryan Gloekler, ECE 251
# 11/19/2019
# I wrote this code in order to finish problem 4 on the homework
# without making human error. Then I decided to make it a full
# converter. In its current state, the program takes in a decimal
# number (+-) and converts it to it's binary IEEE 754 single-precision
# format. It can be easily modified to do double precision.

def calc_sign(value):   #if value is zero, sign bit is zero
    if value >= 0:
        return str(0)
    else: return str(1)


def calc_exp(value):          # calculate the value of the int portion as float
    exponent = 0
    bias = 127
    if value < 1:
        value = value * -1

    while value > 2:
        value = value/2       # divide by 2 until less than 2 greater than 1.
        exponent = exponent + 1
    fraction = value -1

    intpart = exponent + bias
    # print formatted as a binary number
    print('The exponent part is: ' + format(intpart, 'b'))


def calc_fraction(value, bits):
    #calcluates the fractional portion of the representation----------
    if value < 0:
        value = value*-1
        
    while value > 2:
        value = value/2        # divide by 2 until less than 2 greater than 1.
    fraction = value - 1
    #prints the binary value of the fraction--------------------------
    print('The fractional portion is ' + str(fraction))
    print('In binary, this is fraction is: ')
    countfrac = 0
    while fraction !=1:
        if countfrac == bits:
            break
        fraction = fraction*2
        if fraction > 1:
            fraction = fraction-1
            print(1, end='')
        elif fraction < 1:
            print(0, end='')
        else: print(1, end='')
        countfrac = countfrac +1
        #if countfrac % 4 == 0:  # separate every four bits on new lines for
            #print()             # readability, commented out after testing
    print()


if __name__ == "__main__":
        value = float(input('What is the value? '))
        bits = 23  #change this value for other formats
        print('The sign bit is: ' + calc_sign(value))
        calc_exp(value)
        calc_fraction(value, bits)
