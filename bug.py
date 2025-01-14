def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
except TypeError:
    #this will not catch the TypeError
    return "Invalid input types"

print(function_with_uncommon_error(10, 0))  # Output: Division by zero
print(function_with_uncommon_error(10, "hello")) # Output: TypeError