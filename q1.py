digits = input("Enter the four digit number: ")
total = 0
reverse =''
for number in digits:
    total = total + int(number)
for number_flip in reversed(digits):
    reverse = reverse + number_flip
reverse = (reverse)
print(f"""
total: {total}
reverse: {reverse}
"""
)