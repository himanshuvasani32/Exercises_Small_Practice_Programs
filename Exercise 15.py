# using list

# password = input("Enter your password: ")
#
# result = []
#
# if len(password) >= 8:
#     result.append(True)
# else:
#     result.append(False)
#
# digit = False
# for i in password:
#     if i.isdigit():
#         digit = True
#
# result.append(True)
#
# upper_case = False
# for i in password:
#     if i.isupper():
#         upper_case = True
#
# result.append(True)
#
#
# if all(result) == True:
#     print("Strong Password!")
# else:
#     print("Weak Password!")


# Dictionary

# password = input("Enter your password: ")
#
# result = {}
#
# if len(password) >= 8:
#     result["length"] = True
# else:
#     result["length"] = False
#
# digit = False
# for i in password:
#     if i.isdigit():
#         digit = True
#
# result["digits"] = digit
#
# upper_case = False
# for i in password:
#     if i.isupper():
#         upper_case = True
#
# result["uppercase"] = upper_case
#
#
# if all(result.values()):
#     print("Strong Password!")
# else:
#     print("Weak Password!")

# Using function

def strength(password):
    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    upper_case = False

    for i in password:
        if i.isdigit():
            digit = True

        if i.isupper():
            upper_case = True

    result["digits"] = digit
    result["uppercase"] = upper_case

    if all(result.values()):
        return "Strong Password!"
    else:
        return "Weak Password!"


print(strength('DBUxbX90lHeJyuyR1IP'))