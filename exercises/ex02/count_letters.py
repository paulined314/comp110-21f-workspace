"""Counting letters in a string."""

__author__ = "730390549"


letter: str = input("What letter do you want to seach for?: ")
word: str = input("Enter a word: ")

wordcount: int = 0
letter_count: int = 0

while wordcount < len(word):
    if word[wordcount] == letter:
        letter_count = letter_count + 1
    wordcount = wordcount + 1
print(letter_count)