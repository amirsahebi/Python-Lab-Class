def binary_operations(num1, num2):
    binary_num1 = bin(num1)
    binary_num2 = bin(num2)

    sum_result = num1 + num2
    difference_result = num1 - num2
    multiplication_result = num1 * num2

    if num2 != 0:
        division_result = num1 / num2
        modulo_result = num1 % num2
    else:
        division_result = "Undefined (Division by zero)"
        modulo_result = "Undefined (Division by zero)"

    binary_sum = bin(sum_result)
    binary_difference = bin(difference_result)
    binary_multiplication = bin(multiplication_result)
    binary_division = bin(int(division_result)) if division_result != "Undefined (Division by zero)" else division_result
    binary_modulo = bin(int(modulo_result)) if modulo_result != "Undefined (Division by zero)" else modulo_result

    bitwise_and = num1 & num2
    bitwise_or = num1 | num2
    bitwise_xor = num1 ^ num2

    return (binary_num1, binary_num2, binary_sum, binary_difference, binary_multiplication,
            binary_division, binary_modulo, bitwise_and, bitwise_or, bitwise_xor)


def octal_operations(num1, num2):
    octal_num1 = oct(num1)
    octal_num2 = oct(num2)

    sum_result = num1 + num2
    difference_result = num1 - num2
    multiplication_result = num1 * num2

    if num2 != 0:
        division_result = num1 / num2
        modulo_result = num1 % num2
    else:
        division_result = "Undefined (Division by zero)"
        modulo_result = "Undefined (Division by zero)"

    octal_sum = oct(sum_result)
    octal_difference = oct(difference_result)
    octal_multiplication = oct(multiplication_result)
    octal_division = oct(int(division_result)) if division_result != "Undefined (Division by zero)" else division_result
    octal_modulo = oct(int(modulo_result)) if modulo_result != "Undefined (Division by zero)" else modulo_result

    return (octal_num1, octal_num2, octal_sum, octal_difference, octal_multiplication,
            octal_division, octal_modulo)


def logical_operations(num1, num2):
    logical_and = num1 and num2
    logical_or = num1 or num2
    bitwise_and = num1 & num2
    bitwise_or = num1 | num2
    bitwise_xor = num1 ^ num2

    return (logical_and, logical_or, bitwise_and, bitwise_or, bitwise_xor)



num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Binary operations for first part of question 
print("\nBinary Operations:")
binary_results = binary_operations(num1, num2)
print("Binary Representation of num1:", binary_results[0])
print("Binary Representation of num2:", binary_results[1])
print("Sum:", binary_results[2])
print("Difference:", binary_results[3])
print("Multiplication:", binary_results[4])
print("Division:", binary_results[5])
print("Modulo:", binary_results[6])

# Octal operations for second part of question
print("\nOctal Operations:")
octal_results = octal_operations(num1, num2)
print("Octal Representation of num1:", octal_results[0])
print("Octal Representation of num2:", octal_results[1])
print("Sum:", octal_results[2])
print("Difference:", octal_results[3])
print("Multiplication:", octal_results[4])
print("Division:", octal_results[5])
print("Modulo:", octal_results[6])

# Logical operations for third part of question
print("\nLogical Operations:")
logical_results = logical_operations(num1, num2)
print("Logical AND:", logical_results[0])
print("Logical OR:", logical_results[1])
print("Bitwise AND:", logical_results[2])
print("Bitwise OR:", logical_results[3])
print("Bitwise XOR:", logical_results[4])


