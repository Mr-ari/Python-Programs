

def find_letter(word,letter):
    find=0
    for ch in word:
        if letter == ch:
            find=find+1

    print ("No of",letter,"present in the word is",find)


    


word=input("Enter the word:")
letter = input ("Enter the letter you want to find out :")

find_letter(word,letter)

            
            
