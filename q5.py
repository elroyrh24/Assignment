textOne = input("Enter the first text: ")
textTwo = input("Enter the second text: ")
tOneMid = int(len(textOne) / 2)
print(f"expected result: {textOne[:tOneMid]}{textTwo}{textOne[tOneMid:]}")