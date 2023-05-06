import time
import datetime

class TimestampError(Exception): pass
class AdderssError(Exception): pass

def is_mac(var):
	try:
		segments = var.split(':')
		segments = map(lambda x: '*' == x or 1 == len(x.decode('hex')), segments)
		if not False in segments:
			return True

		var = var.replace(':', '')
		binary = var.decode('hex')
		return len(binary) == 6
	except Exception as e:
		return False
	

def is_ip(var):
	try:
		ipv6 = '[' == var[0] and ']' == var[-1] and ':' in var
		if ipv6:
			return True
		nibbles = var.split('.')
		nibbles = map(int, nibbles)
		inrange = map(lambda x: x <= 255 and x >= 0, nibbles)
		return (4 == len(nibbles)) and not (False in inrange)
	except Exception as e:
		return False

def is_lease(var):
	valid_postfix = ('m', 'h', 'd')
	if 'infinite' == var:
		return True
	try:
		endswith = var[-1] in valid_postfix
		number = int(var[:-1])
		return endswith and number
	except Exception as e:
		return False

def is_id(var):
	return var.startswith('id:')

def is_set(var):
	return var.startswith('set:')

def append_comma(s, val, space = False):
	if not val:
		return s
	if not s:
		return val
	if ',' == s[-1]:
		return s + ' ' + val
	elif '=' == s[-1]:
		return s + val
	else:
		return s + ', ' + val

def get_timestamp(val):
	try:
		num = int(val)
		ctime = time.ctime(num)
		ret = datetime.datetime.strptime(ctime, "%a %b %d %H:%M:%S %Y")
	except Exception as e:
		print(e)
		raise TimestampError("'%s' is not a valid timestamp" % (val, ))
	return ret
