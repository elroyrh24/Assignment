textOne = input("Enter the first text: ")
textTwo = input("Enter the second text: ")
resultText = textOne[0] + textTwo[0] + textOne[int(len(textOne)/2)] + textTwo[int(len(textTwo)/2)] + textOne[-1] + textTwo[-1]
print(f"expected result: {textOne[0] + textTwo[0] + textOne[int(len(textOne)/2)] + textTwo[int(len(textTwo)/2)] + textOne[-1] + textTwo[-1]}")