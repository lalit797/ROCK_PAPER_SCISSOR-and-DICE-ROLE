import random
def r_p_s():
 u_count = 0
 c_count= 0
 l=["rock","paper","scissor"]
 print("==========WELCOME TO ROCK-PAPER-SCISSOR GAME========")

 u_c = int(input('''
                 PRESS 1. START
                 PRESS 2. END| EXIT'''))
 if u_c == 1:
        for i in range (1,6):
            u_in = int(input('''
            prees 1. rock
            press 2. scissor
            press 3. paper ''' ))
            if u_in == 1:
                u_c = "rock"
            elif u_in ==2:
                u_c = "scissor"
            elif u_in ==3:
                u_c = "paper"
            else:
                print("invalid input")
            C_c = random.choice(l)    
            if u_c== C_c:
             print("game draw")
            elif (u_c=="rock" and C_c =="scissor") or (u_c=="paper" and C_c =="rock") or (u_c == "scissor" and C_c == "paper"):
                print("YOU WIN ")
                u_count+=1
                print("your score is",u_count)
            elif(C_c=="rock" and u_c =="scissor")or (C_c=="paper" and u_c =="rock") or (C_c == "scissor" and u_c == "paper"):
                print("Computer wins")
                c_count+=1
                print("computer score is ",c_count)

        if  u_count> c_count:
            print(f"user wins score is :{u_count} ")
        elif u_count<c_count:
            print(f"computer wins score is : {c_count}")
        elif u_count == c_count:
            print(f'''
                  game draw computer score is :{c_count}
                  your score is : {u_count}''')    
