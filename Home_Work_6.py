result = []

def divider(a, b):
    if a < b:
        raise ValueError("a must be greater than or equal to b")
    if b > 100:
        raise IndexError("b must be less than or equal to 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ValueError, IndexError, TypeError, ZeroDivisionError) as e:
        print(f"Error with key {key}: {e}")

print(result)
