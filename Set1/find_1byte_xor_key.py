
import string
import collections

# Returns empty string if something failed.

# Change logic to first do most common check and only then check if one out of the three most common is space.

def decrypt_1byte_new(xored_text): # Still a WIP, fix to find the string in next challenge
    s = ""
    byte_count = collections.Counter(xored_text)
    common = byte_count.most_common(3)
    
    for i in xrange(len(common)):
        diff = (ord(common[i][0]) ^ ord(' '))
        s = "".join([chr(ord(x)^diff) for x in xored_text])
        if chr(ord(common[0][0])^diff) == ' ' and (chr(ord(common[1][0])^diff).lower() in 'aeiou' or chr(ord(common[2][0])^diff).lower() in 'aeiou'):
            return s
    
    return ""
            

def decrypt_1byte_old(xored_text):
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