import math

def measure_time (length,velocity):
    return (length / velocity)

test = int (input())

for testing in range (test):

    inp = input()
    inputs = inp.split(' ')

    len_th_stair = math.sqrt(2) * int (inputs[0])
    len_th_elevator = 2 * int(inputs[0])

    if measure_time (len_th_stair,int (inputs[1])) > measure_time (len_th_elevator,int (inputs[2])):
        print("Elevator")
    else:
        print ("Stairs")
