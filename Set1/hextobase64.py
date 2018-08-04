import binascii
import base64

def hextobase64(raw_hex):
	return base64.b64encode(binascii.unhexlify(raw_hex))