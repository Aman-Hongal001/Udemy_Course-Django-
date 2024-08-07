import re

# patterns = ['term1','term2']

# text = 'This is a string with term1, not the other!'

# for pattern in patterns:
#     print("I'm searching for "+pattern)
    
#     if re.search(pattern,text):
#         print("MATCH!")
#     else:
#         print("NO MATCH")

def multi_re_find(patterns,phrase):
    
    for pat in patterns:
        print("Searching for patter {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")
    

# test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dsssss...sddddd'

# test_patterns = ['sd+'] #starting with s and one or more d
# test_patterns = ['sd*'] #starting with s and one or more d
# test_patterns = ['sd{3}'] #starting with s and 3 d
# test_patterns = ['sd{1,3}'] #starting with s and 1 or 3 d


# test_phrase = 'This is a string! But is has punctuation. How can we remove it?'
# test_patterns = ['[^!.?]+'] #it is going to split the phrase when it finds anyone of the mention pattern
# test_patterns = ['[a-z]+'] # will split all the lowercase words
# test_patterns = ['[A-Z]+'] # will split all the uppercase words

test_phrase = 'This is a string with numbers 123231 and symbol #hastag'
test_patterns = [r'\d+'] # to search one or more digits
test_patterns = [r'\D+'] # to search one or more non digits
test_patterns = [r'\s+'] # to search one or more white spaces
test_patterns = [r'\S+'] # to search one or more non-white spaces
test_patterns = [r'\w+'] # to search one or more letter or digits
test_patterns = [r'\W+'] # to search one or more special letters including space
multi_re_find(test_patterns,test_phrase)