stringOne, stringTwo = input("Enter the sample string: ").split(", ", 2)
print(f"expected result: {stringTwo[:3] + stringOne[3:]} {stringOne[:3] + stringTwo[3:]}")
