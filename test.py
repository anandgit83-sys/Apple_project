import re
test_string = '123abcedsabc567abcttgabc'

pattern = re.compile(r"abc")
matches = pattern.finditer(test_string)

for match in matches:
    print(match)