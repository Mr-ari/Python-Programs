#ROT13 is a weak form of encryption that involves “rotating” each letter in a word
#by 13 places. To rotate a letter means to shift it through the alphabet, wrapping around to the
#beginning if necessary, so ’A’ shifted by 3 is ’D’ and ’Z’ shifted by 1 is ’A’.
#Write a function called rotate_word that takes a string and an integer as parameters, and that
#returns a new string that contains the letters from the original string “rotated” by the given amount.
#For example, “cheer” rotated by 7 is “jolly” and “melon” rotated by -10 is “cubed”.
#You might want to use the built-in functions ord, which converts a character to a numeric code,
#and chr, which converts numeric codes to characters.




#function definition
def rotate_word(string,num):
    m_string="abcdefghijklmnopqrstuvwxyz"
    new_string=""
    for ch in string:

        position=m_string.find(ch)
        position=position+num
        new_string= new_string+ m_string[position]

        

    return new_string



#function body 

string=input("Enter the string: ")
num= int (input ("Enter the number of shifting: "))

print("After rotating the string will be",rotate_word(string,num))







        
        
                
