print('spam eggs'); # single quotes
print('doesn\'t'); # use / to escape the single quotes
print("doesn't"); # or use double quotes

print("thank\nyou"); # \n is special character
print(r"thank\nyou"); # r is raw string

print("""
    using
    triple
    quotes
"""); # triple quotes make string literals can span multiple lines

print(3*"good"+" job"); # string concatination
print("py" "thon");

word="Python"
print(word[0]); # strings can be indexed
print(word[:2]);
print(word[4:])
print(len(word));
