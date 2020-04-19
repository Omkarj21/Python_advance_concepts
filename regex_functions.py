import re
a = "123abc"
a1 = "987pqrs"

# match = Find something at the beginning of the string and return a match object else None, Does only beginning of string.
print("Match : ", re.match("[a-z]",a)) # None
print("Match : ", re.match("[0-9]",a1)) # <re.Match object; span=(0, 1), match='9'>

# If matched pattern found anywhere in string then it returns match object else None, scans through whole string.
print("Search : ", re.search("[a-z]",a)) # <re.Match object; span=(3, 4), match='a'>

# If matched pattern found in string then it returns all the matches string in a LIST, else Empty LIST.
print("Findall : ", re.findall("[a-z]",a)) # Findall :  ['a', 'b', 'c']

# finditer = If matched pattern found in string then it returns position i.e. starting index and ending index of matched pattern,
print("Finditer : ", re.finditer("[a-z]",a)) # Finditer : <callable_iterator object at 0x0000013E85EB6BB0>

# sub = This is nothing but Substitute/Replace.
print("Substitute : ", re.sub("[a-z]",'abc',a1)) # Substitute : 987abcabcabcabc, here abc is 4 times bcoz p,q,r,s this finds these 4 characters.

# subn = This returns a tuple of 2 items containing the new string and the number of substitutions made.
print("Substitute_Count : ", re.subn("[a-z]",'abc',a1)) # Substitute : ('987abcabcabcabc', 4), here abc is 4 times bcoz p,q,r,s this finds these 4 characters.

# split = splits the string where there is a match and returns a list of strings where the splits have occurred.
print("Split : ", re.split('\d',a1)) # Split : ['', '', '', 'pqrs']
# split with maxsplit : You can pass maxsplit argument to the re.split() method. It's the maximum number of splits that will occur.
print("Split_maxsplit : ", re.split('\d',a1,1)) # Split : ['', '', '', 'pqrs']