
# Returns empty string if length if strings length isn't the same.
def xor_strings(data1, data2):
    if len(data1) != len(data2):
        return "";
        
    s = ""
    
    for i in xrange(len(data1)):
        s += chr(ord(data1[i]) ^ ord(data2[i]))
        
    return s