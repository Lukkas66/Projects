#8kyu

#Age Range Compatibility Equation

def dating_range(age):
    if age <= 14:
        min_age = int(age - 0.10 * age)
        max_age = int(age + 0.10 * age)
    else:
        min_age = int(age / 2 + 7)
        max_age = int((age - 7) * 2)
    
    return f"{min_age}-{max_age}"

#simple Fun #352: Reagent Formula

#7kyu

#2.How many are smaller than me?

def smaller(arr):
    result = []
    for i in range(len(arr)):
        count = 0
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                count += 1
        result.append(count)
    return result

#1. Anagram Detection

def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    
    sorted_test = sorted(test)
    sorted_original = sorted(original)
    
    return sorted_test == sorted_original

#6kyu

#1.Unique In Order

def unique_in_order(sequence):
    result = []
    for i, item in enumerate(sequence):
       if i == 0 or item != sequence[i - 1]:
        result.append(item)
    return result

#2.Sum of nested numbers

def sum_nested_numbers(arr, depth=1):
    total = 0
    for item in arr:
        if isinstance(item, list):
            total += sum_nested_numbers(item, depth + 1)
        else:
            total += item ** depth
    return total

#5kyu

#1.luck check

def luck_check(ticket):
    if not isinstance(ticket, str) or not ticket.isdigit():
        raise ValueError("Input should be a non-empty string representing a decimal number")

    n = len(ticket)
    half_n = n // 2
    
    if n % 2 == 0:
        left_sum = sum(int(digit) for digit in ticket[:half_n])
        right_sum = sum(int(digit) for digit in ticket[half_n:])
    else:
        left_sum = sum(int(digit) for digit in ticket[:half_n])
        right_sum = sum(int(digit) for digit in ticket[half_n+1:])
    
    return left_sum == right_sum

#2.





#პირველი გამოცდა იყო და იმედია სწორედ ავტვირთე ყველფერი.






        

