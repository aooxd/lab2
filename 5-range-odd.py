def odd_numbers_in_range(start, end):
    if end < start:
        return []
    
    result = []
    for i in range(start, end + 1):
        if i % 2 != 0:
            result.append(i)
    return result 
