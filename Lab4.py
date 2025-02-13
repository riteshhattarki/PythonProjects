# Function 1
def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    sum = 0
    num1 = 0
    num2 = 1
    for i in range(3, n + 1):
        for j in range(i - 2, i - 1):
            sum = num1 + num2
        num1 = num2
        num2 = sum
    return sum

# result = fibonacci(25)
# print(result)

# Function 2
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# result = is_prime(-2)
# print(result)

def print_prime_factors(n):
    final_string = ""
    main_string = str(n) + " " + "=" + " "
    if is_prime(n):
       final_string = final_string + str(n) + " " + "=" + " " + str(n)
       print(final_string)
       return

    else:
        while n != 1:
            if n % 2 == 0:
                main_string += "2" + " " + "*" + " "
                # final_string = final_string + str(n) + " " + "=" + " " + str(2) + " " + "*"
                n = n // 2
            elif n % 3 == 0:
                main_string += "3" + " " + "*" + " "
                # final_string = final_string + str(n) + " " + "=" + " " + str(3) + " " + "*"
                n = n // 3
            elif n % 5 == 0:
                main_string += "5" + " " + "*" + " "
                # final_string = final_string + str(n) + " " + "=" + " " + str(5) + " " + "*"
                n = n // 5
            elif n % 7 == 0:
                main_string += "7" + " " + "*" + " "
                # final_string = final_string + str(n) + " " + "=" + " " + str(7) + " " + "*"
                n = n // 7
            elif n % 11 == 0:
                main_string += "11" + " " + "*" + " "
                # final_string = final_string + str(n) + " " + "=" + " " + str(11) + " " + "*"
                n = n // 11
    modified_string = main_string[0:len(main_string) - 2]
    print(modified_string)

# print_prime_factors(24)


