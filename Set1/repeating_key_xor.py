
KEY = "ICE"


def repeat_xor(text_to_xor):
    s = ""
    index = 0
    for item in xrange(len(text_to_xor)):
        s += chr(ord(text_to_xor[index]) ^ ord(KEY[item % len(KEY)]))
        index += 1
    print s.encode('hex')
