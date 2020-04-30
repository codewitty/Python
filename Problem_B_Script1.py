# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# Unit B Take-Home 

# First Script - Working with Strings

# String Type Tests
string1 = input('Enter a string\n')
print("IsUpper Test: " , string1.isupper())
print("IsDigit Test: " , string1.isdigit())
print("IsAlpha Test: " , string1.isalpha())

# Escape Characters within a string
variable1 = "Type, type, type away.\nCompile. Run. Hip hip hooray!\nNo error today!"
print(variable1)
quote = "And now for something completely different"

# Slicing a string
print(quote[:6])
print(quote[-4:])
print(quote[14:16])
print(quote[::2])
print(quote[::-1])

# Using string operators + and *
pattern1 = ".~*'"
pattern2 = pattern1 + pattern1[::-1]

print(pattern2 * 5)

'''
Execution results:

Enter a string
ABC123
IsUpper Test:  True
IsDigit Test:  False
IsAlpha Test:  False
Type, type, type away.
Compile. Run. Hip hip hooray!
No error today!
And no
rent
me
Adnwfrsmtigcmltl ifrn
tnereffid yletelpmoc gnihtemos rof won dnA
.~*''*~..~*''*~..~*''*~..~*''*~..~*''*~.

'''
