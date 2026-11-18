from p7 import palindrome

def test_palindrome():
    assert palindrome("madam") == "Palindrome"

def test_palindrome2():
    assert palindrome("level") == "Palindrome"

def test_palindrome3():
    assert palindrome("hello") == "Not Palindrome"