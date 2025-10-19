def power_two(a):
    return a ** 2

def power_three(a):
    return a ** 3

def mean(a, b):
    return (a + b) / 2

def run_calculation():
    results = []
    for i in range(5, 16): 
        m = mean(power_two(i), power_three(i))
        results.append(m)
    return results
