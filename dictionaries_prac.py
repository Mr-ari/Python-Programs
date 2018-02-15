def histogram(s):
	h = dict()
	for c in s:
		if c not in h:
			h[c] = 1
		else:
			h[c] += 1

	return h
	
def  LookUpError():
	print ("Error")


def reverse_look_up(h,value):
	for key in h:
		if h[key] == val:
			return key
	raise LookUpError()
	


def invert_dict(h):
	invert = dict()
	for key in h:
		val = h[key]
		if val not in invert:
			invert[val] = [key] 
		else :
			invert[val].append(key)

	return invert
 
def fibonacci(n):
	known = dict()
	known = { 0:0 , 1:1 } 
	if n in known :
		return known[n]
	else:
		res = fibonacci(n-1)+fibonacci(n-2)
		known [n] = res
		return res





#in main

h = histogram("parrot")
print(invert_dict(h))			
print(fibonacci(5))				




