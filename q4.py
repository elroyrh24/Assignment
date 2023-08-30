textOne = input("Enter the first text: ")
textTwo = input("Enter the second text: ")
firstTwo = textOne[0] + textTwo[0]
middleTwo = textOne[int(len(textOne)/2)] + textTwo[int(len(textTwo)/2)]
lastTwo = textOne[-1] + textTwo[-1]
print(f"expected result: {firstTwo}{middleTwo}{lastTwo}")