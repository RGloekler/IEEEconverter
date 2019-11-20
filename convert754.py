if __name__ == "__main__":
    exponent = 0

    number = input('What is the value? ')
    value = float(number)
    bitnum = input('How many bits after the radix point? ')
    bits = float(bitnum)

    #calcluates the fractional portion of the representation
    while value > 2:
        value = value/2          #divide by 2 until less than 2 greater than 1.
        exponent = exponent + 1
    fraction = value -1

    #prints the binary value of the fraction--------------------------
    print('The fractional portion is ' + str(fraction))
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

    print()
    print('The fraction is ' + str(countfrac) + ' bits long')
