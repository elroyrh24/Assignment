stringOne, stringTwo = input("Enter the sample string: ").split(", ", 2)
newStrOne = stringTwo[:3] + stringOne[3:]
newStrTwo = stringOne[:3] + stringTwo[3:]
print(f"expected result: {newStrOne} {newStrTwo}")
