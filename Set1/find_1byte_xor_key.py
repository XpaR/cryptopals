
import string
from collections import Counter

# Returns empty string if something failed.

def decrypt(xored_text):
    for item in xrange(1, 256):
        s = ""
        for index in xrange(len(xored_text)):
            s += chr(ord(xored_text[index])^item)
        
        if all(c in string.printable for c in s) == True: # if string is only printables.
            byte_count = collections.Counter(s)
            common = byte_count.most_common(3)
            if common[0][0] == ' ' and (common[1][0] in 'aeiou' or common[2][0] in 'aeiou'):
                return s
    return ""