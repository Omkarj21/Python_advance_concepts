# There are Total 10 Special Sequences.
# \A, \b, \B, \d, \D, \s, \S, \w, \W, \Z

import re

string = 'Omkar is -2, Prasad +1, Sagar will be 3035, Vina be "91" '
string1 = 'Omkar is , Prasad , Sagar will be , Vina be Omk'

pattern0 = '\AOm' # This will return word/charactes if it present at START, i.e. on 0th Index in Complete string (Whole Sentence) else returns blank
pattern1 = '\d+' # This will return digits as present in Complete string (Whole Sentence)
pattern2 = '\D+' # This will return words as present in Complete string (Whole Sentence)
pattern11 = '\d' # This will return single digits ['2', '1', '3', '0', '3', '5', '9', '1']
pattern22 = '\D' # This will return single characters ['O', 'm', 'k', 'a', 'r', ' ', 'i', 's', ' ', '-', ',', ' ', 'P', 'r', 'a', 's', 'a', 'd', ' ', '+', ',', ' ', 'S', 'a', 'g', 'a', 'r', ' ', 'w', 'i', 'l', 'l', ' ', 'b', 'e', ' ', ',', ' ', 'V', 'i', 'n', 'a', ' ', 'b', 'e', ' ', '"', '"', ' ']
pattern3 = r'\bOmk' # Omk start of the word = ['Omk', 'Omk'] present in Complete string (Whole Sentence)
pattern33 = r'kar\b' # kar end of the word = ['kar'] present in Complete string (Whole Sentence)
pattern4 = '\Baga' # This is same as pattern44, ['aga'] present in middle of word.
pattern44 = 'aga\B' # This is same as pattern4, ['aga'] present in middle of word.
pattern5 = '\s' # This will return only white spaces.
pattern6 = '\S' # This will remove white spaces and will return single characters.
pattern66 = '\S+' # This will remove white spaces and will return each word.
pattern7 = '\w+' # This will return full characters/numbers skips special characters
pattern77 = '\w' # This will return single characters/numbers skips special characters
pattern8 = '\W' # This will return special characters and skips alphanumerics i.e. characters and numbers
pattern9 = 'Omk\Z' # This will return word if it is same as last word in whole string.

result0 = re.findall(pattern0, string)
result1 = re.findall(pattern1, string)
result2 = re.findall(pattern2, string)
result7 = re.findall(pattern7, string)
result8 = re.findall(pattern8, string)
print("Output of \A+ : ", result0)  # With \AOm => ['Om']
print("Output of \d+ : ", result1)  # With \d+ => ['2', '1', '3035', '91']
print("Output of \D+ : ", result2)  # With \D+ => ['Omkar is -', ', Prasad +', ', Sagar will be ', ', Vina be "', '" ']
print("Output of \w+ : ", result7)  # With \w+ => ['Omkar', 'is', '2', 'Prasad', '1', 'Sagar', 'will', 'be', '3035', 'Vina', 'be', '91']
print("Output of \W : ", result8)  # With \W => [' ', ' ', '-', ',', ' ', ' ', '+', ',', ' ', ' ', ' ', ' ', ',', ' ', ' ', ' ', '"', '"', ' ']

result3 = re.findall(pattern3, string1)
result4 = re.findall(pattern4, string1)
result5 = re.findall(pattern5, string1)
result6 = re.findall(pattern6, string1)
result9 = re.findall(pattern9, string1)
print(r"Output of \bOmk : ", result3)  # With \bOmk  => ['Omk', 'Omk']
print("Output of \Baga : ", result4)  # With \Baga => ['aga']
print("Output of \s : ", result5,len(result5))  # With \s => [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] 11 => This returns white spaces
print("Output of \S : ", result6)  # With \S => This will remove white spaces and return single string : ['O', 'm', 'k', 'a', 'r', 'i', 's', ',', 'P', 'r', 'a', 's', 'a', 'd', ',', 'S', 'a', 'g', 'a', 'r', 'w', 'i', 'l', 'l', 'b', 'e', ',', 'V', 'i', 'n', 'a', 'b', 'e', 'O', 'm', 'k']
print("Output of Omk\Z : ", result9)  # With \Z => ['Omk'], This will return word if it is same as last word in whole string.
# ---------------------------------------------------------------------------------------------
