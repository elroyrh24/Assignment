digits = input("Enter the four digit number: ")

#tambahin digit jadi nomor
total = int(digits[0]) + int(digits[1]) + int(digits[2]) + int(digits[3])

#kasih hasil
print(f"""
total: {total}
reverse: {digits[::-1]}
"""
)