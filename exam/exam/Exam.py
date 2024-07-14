#1. 8kyu Age Range Compatibility Equation

def dating_range(age):
    if age <= 14:
        min_age = int(age - 0.10 * age)
        max_age = int(age +0.10 * age)
        
    else:
            min_age = int(age / 2 ) +7
            max_age = (age -7) * 2
            
    return {min_age} - {max_age}

def smaller(arr):
    result = []
    for i in range(len(arr)):
      count = 0
    for j in range(i + 1, len(arr)):
            
            if arr[j] < arr[i]:
                count += 1
            result.append(count)
    return result

#7kyu

#1.Simple Fun #352: Reagent Formula
def is_valid_formula(formula):
    formula_set = set(formula)
    
    if 1 in formula_set and 2 in formula_set:
        return False
    
    if 3 in formula_set and 4 in formula_set:
        return False
    
    if (5 in formula_set) != (6 in formula_set):
        return False
    
    if 7 not in formula_set and 8 not in formula_set:
        return False
    
    return True

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

#3. Anagram Detection







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

#5
#1.kyu Unique In Order

def luck_check(ticket):
    # Ensure the input is a non-empty string representing a decimal number
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










        

