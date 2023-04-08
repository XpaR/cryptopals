import requests
import math
from collections import Counter
SITE_TO_GET_FREQUENCY = "http://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt"


MAX_ASCII_CHARS = 127

FREQUENCY_TABLE = []

first_time = True


# You should call this function once, before running decrypt_1byte_xor
def init_frequencies():
    global FREQUENCY_TABLE
    site_text = requests.get(SITE_TO_GET_FREQUENCY).text.encode('ascii')
    FREQUENCY_TABLE = dict(Counter(site_text))



def is_ascii(s):
    return all(ord(c) >= 0x20 and ord(c) <= 0x7F for c in s)
    

    
def decrypt_1byte_xor(xored_text):
    best_freq_index = (0, 0.0) # this holds the number iteration with biggest frequency
    total_freq = 0.0
    current_decrypted = ""
    
    for i in xrange(0, MAX_ASCII_CHARS + 1):
        current_decrypted = ""
        current_freq = 1.0
        
        
        for j in xrange(len(xored_text)):
            current_decrypted += chr(ord(xored_text[j]) ^ i)
            try:
                current_freq += math.log(FREQUENCY_TABLE[current_decrypted[j]])
            except:
                continue
            
        if current_freq > total_freq:
            total_freq = current_freq
            best_freq_index = (i,total_freq)
            
    # The return value is a tuple of the index which the best match was at, and how trusty its frequency was
    return best_freq_index
    
    
    
    