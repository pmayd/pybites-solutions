def sum_numbers(numbers=None):
    if numbers is not None:
        return sum(numbers)
        
    return sum(range(101))