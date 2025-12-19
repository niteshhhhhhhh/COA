
def full_adder(a, b, c):
    sum_bit = (a ^ b) ^ c
    carry_out = (a & b) | (b & c) | (a & c)
    return sum_bit, carry_out


def adder_4bit(binary1, binary2):
    result = ""
    carry = 0

    for i in range(3, -1, -1):
        a = int(binary1[i])
        b = int(binary2[i])
        sum_bit, carry = full_adder(a, b, carry)
        result = str(sum_bit) + result

    return result, carry


def twos_complement(binary):
    # 1's complement
    ones_comp = ''.join('1' if bit == '0' else '0' for bit in binary)

    # Add 1
    result, _ = adder_4bit(ones_comp, "0001")
    return result


# -------- Main Program --------
print("\n4-Bit Binary Subtraction using 2's Complement Method")
print("=" * 55)

# Input (as strings)
a = input("Enter first 4-bit binary number (A): ")
b = input("Enter second 4-bit binary number (B): ")

b_2s = twos_complement(b)
print(f"2's complement of B (B'+1): {b_2s}")

final_sum, carry = adder_4bit(a, b_2s)

print(f"Final Sum (A + B'+1): {final_sum}")

if carry:
    print("Result is Positive (No Borrow)")
else:
    print("Result is Negative (Borrow occurred)")
