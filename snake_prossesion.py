#A PROGRAME TO CHECK WHETHER THE PROSSESION IS VALID OR INVALID
#H MEANS HEAD AND T MEANS TAIL
#EXAMPLE HTHT - VALID , HTTH- VALID , HHH-INVALID,.....HT..HT
...
def Word_check(word):
    if word == 'H':
        return 1
    elif word == 'T':
        return 0
    else:
        return 3



test=int(input ("Enter the number of test cases: "))

while test:

    string_inp=input("Enter the string: ")

    string="0"
    
    for ch in string_inp:
        
        if ch != '.':
            string=string+ch

    no=0    
    i=1
    while i< len(string):

        if Word_check(string[i])==1:
            
            if Word_check(string[i+1])==0:
                i=i+2

            else:
                no=no+1
                break
                

        elif Word_check(string[i])==0:
            
            if Word_check(string[i+1])==1:
                i=i+2

            else:
                no=no+1
                break
                

        else:
            no=no+1
            break 
            
                
                
    if no==0:
        print("Valid")

    else:
        print("Invalid")
                
    

    test = test-1




    
         
