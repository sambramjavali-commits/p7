import sys

def palindrome(string):
    if string == string[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

if __name__ == "__main__":

    string = input("Enter a string:")

    result = palindrome(string)
    print(result)