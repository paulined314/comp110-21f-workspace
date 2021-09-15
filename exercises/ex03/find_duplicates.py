"""Finding duplicate letters in a word."""

__author__ = "730390549"

word: str = input("Enter a word: ")
a = 0
while a < len(word):
    b = 0
    repeat = 0
    letter = word[a]
    if repeat < 2:
        while b < len(word):
            if word[b] == letter:
                repeat = repeat + 1
            b = b + 1
        if repeat > 1:
            print("Found Duplicate: True")
            a = len(word)
        else:
            a = a + 1
            if a >= len(word):
                print("Found Duplicate: False")
            
        
