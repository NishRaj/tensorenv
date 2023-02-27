import re

text_to_search = '''
abcdefghijklmnopqrstuv
ABCDEFGHIJKLMNOPQRSTUVW
@@^^---^^&&!!!
91-9980936945
SUNDAY
MONDAY
TUESDAY
JANUARY
FEBRUARY
123-123-1980
274-034-1984
065-091-2012
nishank nishanknishanknishank
cat
bat
sat
pat
nat

# pattern based on raw string
#pattern = re.compile(r'DAY')
Mr. Ajay Yadav
Mr Sateyndra Kuntal
Mr. Pramod Shankar Gupta
Mr. Kumar Abhishek
Mrs. Neha
Mr Anand Mukul Pandey
'''

pattern_1 = re.compile(r'\d\d\d[-]\d\d\d[-]\d\d\d\d')
# [] character set always matches only one character and not a sequence of characters.
# [-.] will either match - or . but not a combibation of -.

pattern_2 = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
# - if used with digits and alphabets inside character set, it defines a range
pattern_3 = re.compile(r'[1-3][4-6][7-9]-\d\d\d-\d\d\d\d')
# ^ is called Caret. If used in the character set, it negates the characters inside the chanacter set
# all three letter words which ends with at but does not start with b
pattern_4 = re.compile(r'[^b]at')

# Use quantifiers to repeat the pattern.
pattern_5 = re.compile(r'\d{3}-\d{3}-\d{3}')

# Use ? to make the matching character optional
pattern_6 = re.compile(r'Mr\.?\s[A-Z]')
# Use () to define group of patterns
pattern_7 = re.compile(r'M(r|rs|s)\.?\s\w*')
matches = re.finditer(pattern_7, text_to_search)

for match in matches:
     # prints the group of patterns. It throws index error if group is not present.
     print(match.group())

with open("data.txt", 'r') as f:
    contents = f.read()
    matches = re.finditer(pattern_5, contents)
    for match in matches:
        pass