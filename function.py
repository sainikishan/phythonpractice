def calculate_gmean(a, b):
    gmean = ((a * b) ** 0.5)
    return gmean
a=9
b=8
if(a > b):
    print("First number is greather:")
else:
    print("Both numbers must be positive.")
calculate_gmean(a, b)
print(calculate_gmean(a, b))

