def fullAdder(a,b,cin):
    sum = (a^b)^cin     
    carry = (a&b)|(cin&(a^b)) 

    return sum,carry


def rippleAdder(a,b):
    carry = 0 
    result = ""
    

    for i in range(3,-1,-1):    
        aBit = int(a[i])
        bBit = int(b[i])
        sum , carry = fullAdder(aBit, bBit,carry)
        result = str(sum) + result 

        
    overflow = carry

    if overflow:
        result = '1'+ result

    return result, overflow



ain = input("Enter 4 bit binary number:")
bin = input("Enter 4 bit binary number:")

sum , overflow = rippleAdder(ain,bin)
print(f"Sum in binary : {sum}")
print(f"Sum in decimal: {int(sum, 2)}")
print("Overflow occured!" if overflow else"No overflow")
