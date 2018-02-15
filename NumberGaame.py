

import random
beg=0
end = 100
mid = 50
print ("Choose any number between 1-100")
entry = input ("Done ? are you ready to play ? ").upper()
if entry == "YES" or entry == 'Y':
    while True:
        mid = int ((beg+end)/2)
        print ("Is your choosen number is",mid,"?")
        ans = input().upper()
        if ans == "YES" or ans == 'Y':
            print("hurrah! we got this")
            break
        else :
            rand= random.choice([1,2])
            if rand==1:
                print ("Is your choosen number in between",mid,"-",end,"?")
                ans = input().upper()
                if ans == "YES" or ans == 'Y':
                    beg = mid
                else:
                    end=mid
            elif rand==2:
                print ("Is your choosen number in between",beg,"-",mid,"?")
                ans = input().upper()
                if ans == "YES" or ans == 'Y':
                    end= mid
                else:
                    beg = mid
            
        
    

    print("Thank you !")









