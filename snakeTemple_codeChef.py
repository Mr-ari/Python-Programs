def is_odd(num):
    if num % 2 == 0:
        return False 
    else :
        return True
def check_incresing_decresing_by_1(array):
    for i in range (1,int (len(array)/2)+1):
	if array[i-1]==i:
	    pass 
        else:
            return False
    j = i+1
    while i < len (array):
	if array[j] == j:
            pass
	else:
            return False
    return True
						
test_cases = int (input())

for test in range (test_cases):

    length = int (input())
    sec_line_input = input()
    array  = sec_line_input.split' ')

    if is_odd(length) and check_incresing_decresing_by_1(array):
	print ('yes')
    else:
	print('no')

