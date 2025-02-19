def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    return total / len(numeric_numbers) 

#Example
print(calculate_average([1,2,3,4,5]))
print(calculate_average([]))
print(calculate_average([1,2,'a',4,5]))