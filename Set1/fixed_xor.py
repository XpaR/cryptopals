
# Returns empty string if length if strings length isn't the same.
def xor_strings(data1, data2):
	if len(data1) != len(data2):
		return "";
		
	data1 = data1.decode('hex')
	data2 = data2.decode('hex')
		
	return "".join([chr(ord(data1[i])^ord(data2[i])) for i in xrange(len(data1))])