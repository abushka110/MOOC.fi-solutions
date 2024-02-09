def palindromes(word):
    if word != word[::-1]:
        return False
    else:
        return True
    
def main():
    wordx = input("Please type in a palindrome: ")
    while palindromes(wordx) == False:
        print("that wasn't a palindrome")
        wordx = input("Please type in a palindrome: ")
    print(f"{wordx} is a palindrome!")

main()