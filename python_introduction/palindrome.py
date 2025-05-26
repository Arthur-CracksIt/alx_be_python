word = input("Enter a word: ").lower() #this converts the input to lowercase for case-insensitive
if word == word[::-1]: #this reverses the string and checks if it's the same as the original
    print("The word is a palindrome")

else:
    print("The word is not a palindrome")

#ternary operator version
message = "The word is a palindrome" if word ==word[::-1] else "The word is not a palindrome"
print(message)
if 0 < len(message) < 15:
    print("The message is short")

