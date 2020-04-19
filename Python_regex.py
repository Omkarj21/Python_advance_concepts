import re
print(range(10))

pattern1 = '^a...s$'
test_string_1 = 'abyss'  # For this Search successful
test_string_2 = 'Alias'  # For this Search unsuccessful
# result = re.match(pattern, test_string_2) # None
result = re.match(pattern1, test_string_1)  # <re.Match object; span=(0, 5), match='abyss'>
print("Result of re.match :", result)
if result:
    print("Search successful.")
else:
    print("Search unsuccessful.")

# -----------------------------------------------------------------------------------------------------------------------
strg1 = """The letters on the perimeter tell you which column, row, or diagonal each letter must be placed and
		the next letter must be placed in a square adjacent to the previous letter. Our formulation works,
		but it is displays messy output. Our professor recommended we do a summation for each letter (1=A, 2=B...)
		and display it in a single matrix similar to how the grid is displayed on the website. I've attached what we
		have so far, but we continue to get an error"""
pattern2 = re.compile(r'the')
result = re.search(pattern2, strg1)  # <re.Match object; span=(0, 5), match='abyss'>
print("Result of re.match :", result)
if result:
    print("Search successful.")
else:
    print("Search unsuccessful.")
#------------------------------------------------------------------------------------------------------------------------
# finditer =>
import re
s1 = """This is Blue Berries which is awesome, 
        This is also Blue Berries which is awesome"""
pattern = 'Blue Berries'
for match in re.finditer(pattern, s1):
    s = match.start()
    e = match.end()
    print ('String match "%s" at %d:%d' % (s1[s:e], s, e))
