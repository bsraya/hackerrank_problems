"""
Find out if a string has:
1. alphanumeric characters
2. alphabetical characters
3. any digits l
4. owercase characters
5. uppercase characters
`eval()` compute any expressions in strings
`any()` function returns True if any element of an iterable is True. If not, any() returns False.
"""

string = 'qA2'

# dumb way
if(len(string) == 0):
    print(False)
else:
    print (any(c.isalnum() for char in string))
    print (any(c.isalpha() for char in string))
    print (any(c.isdigit() for char in string))
    print (any(c.islower() for char in string))
    print (any(c.isupper() for char in string))

# shorter way
funcs = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']
for func in funcs:
    print(any(eval('char.' + func + '()') for char in string))