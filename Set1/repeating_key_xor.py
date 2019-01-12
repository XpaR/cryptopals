
KEY = "ICE"


def repeat_xor(text_to_xor, key=KEY):
    s = ""
    index = 0
    for item in xrange(len(text_to_xor)):
        s += chr(ord(text_to_xor[index]) ^ ord(key[item % len(key)]))
        index += 1
    return s
