import random as r
def number(j):
    while True :
        try:
            number = int(input(f"{j}"))
            break
        except ValueError:
            print ("please enter a number")
    return number
def difficulty():#to set the difficulty 
    print ("for easy , medium , hard difficulty \n type  easy medium hard ")
    diff = input ("")
    if diff.strip() in "easy":
        while True :
            range_f =int ( input ("enter range in between 20 to 30 "))
            if range_f <= 30 and range_f >= 20:
                return range_f,diff
            else :
                print ("enter a number between the given range ")
    elif diff.strip() == "medium":
        while True :
            range_f =int ( input ("enter range in between 100 to 200 "))
            if range_f <= 200 and range_f >= 100:
                return range_f,diff
            else :
                print ("enter a number between the given range ")
    elif diff.strip() in "hard":
        while True :
            range_f =int ( input ("enter range in between 500 to 1000 "))
            if range_f <= 1000 and range_f >= 500:
                return range_f,diff
            else :
                print ("enter a number between the given range ")
def setting(top,diff,r_numb,guss):
    while True :
        print (" if want to see difficuty enter (d/D)\n if you want to see the current difficulty then enter (c/C)\n if want to start game enter esc")
        ch=input (":")
        
        global top_of_range,diff_m,r_number,guess
        if ch =="d":
            
            
            top_of_range,diff = difficulty()
            r_number = r.randint(0,top)
            guess=0
            
        
        
        if ch =="c":
            print (diff)
            
            r_number = r.randint(0,top)
            guess=0
         
        if ch == "esc" :
            
            guess=0
            r_numb = r.randint(0,top)
            return top,diff,r_numb
    
guess = 0

top_of_range,diff_m = difficulty()
r_number = r.randint(0,top_of_range)

while True :
     g_number= number("enter the guess number:")
     if g_number == r_number :
         print ("you got it ")
         print (f"number of try it takes you {guess}")
         print ("you want to play another game (y/n)\n if want to change setting then enter (S/s)")
         n_round = input (":")
         if n_round in ["y","Y"]:
             r_number = r.randint(0,top_of_range)
             guess=0
             continue
         if n_round in ["s","S"]:

             setting(top_of_range,diff_m,r_number,guess) 
             
         else :
             break
     if g_number > r_number :
         print ("guess is greater than the random number ")
         
     elif g_number < r_number :
         print ("guess is less than the random number ")
     guess += 1
     
         
         
        

