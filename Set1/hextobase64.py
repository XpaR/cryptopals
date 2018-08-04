import binascii
import base64

def hextobase64(raw_hex):
	return base64.b64encode(raw_hex.decode('hex'))