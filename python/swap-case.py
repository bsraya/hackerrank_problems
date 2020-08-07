string = "HackerRank.com presents \"Pythonist 2\"."

print(''.join(letter.lower() if letter.isupper() else letter.upper() for letter in string))