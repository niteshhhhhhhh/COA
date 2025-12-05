def fullAdder(a,b,cin):
    sum = a^b^cin     
    carry = (a&b)|(cin&(a^b)) 

    print("Sum", sum)
    print("carry", carry)

a = 1
b = 1
cin = 1
fullAdder(a,b,cin)
