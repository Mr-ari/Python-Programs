"""A name can have at most three parts: first name, middle name and last name. It will have at least one part. The last name is always present. The rules of formatting a name are very simple:

    Only the first letter of each part of the name should be capital.
    All the parts of the name except the last part should be represented by only two characters. The first character should be the first letter of the part and should be capitalized. The second character should be ".".
"""


test = int(input())

for i in range(0,test):

    string= input()
    output=""
    split_name= string.split()
    if len(split_name) ==1 :
        output=output+split_name[0][0].upper()
        for i in range(1,len(split_name[0])):
            output=output + split_name[0][i].lower()

    else:
        for i in range(0,len(split_name)):
            if i==len(split_name)-1:
                output=output+split_name[len(split_name)-1][0].upper()
                for j in range(1,len(split_name[0])):
                    output=output + split_name[0][j].lower()
                

            else:
                output = output+split_name[i][0].upper()+". "
                

    print(output)


    
        
        
    

    
        

    
