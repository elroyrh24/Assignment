digits = input("Enter the four digit number: ")
total = int(digits[::])
reverse =''
for number in digits:
    total = total + int(number)
print(f"""
total: {total}
reverse: {digits[::-1]}
"""
)