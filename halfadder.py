def halfAdder(a,b):
    sum = a^b      # a xor b  
    carry = a&b    # a and b 

    print("Sum", sum)
    print("carry", carry)

a = 1
b = 2
halfAdder(a,b)
