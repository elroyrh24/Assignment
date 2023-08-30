stringOne, stringTwo = input("Enter the sample string: ").split(", ", 2)
stringOne, stringTwo = stringOne.strip(), stringTwo.strip()
print(f"expected result: {stringTwo[:3] + stringOne[3:]} {stringOne[:3] + stringTwo[3:]}")
