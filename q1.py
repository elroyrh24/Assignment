digits = input("Enter the four digit number: ")
total = int(digits[0]) + int(digits[1]) + int(digits[2]) + int(digits[3])
print(f"""
total: {total}
reverse: {digits[::-1]}
"""
)