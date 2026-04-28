import random
def d_r():
    print("========WELCOME TO DICE-ROLL GAME========")
    u_count = 0
    c_count = 0
    i=1
    while i <=3:
     u_c = int(input("ENTER THE NO. OF YOUR CHOICE :" ))
     no_generator = random.randint(1,6)
     if u_c == no_generator :
            print(f'''your number match | you win 
                    user choice : {u_c}
                    computer choice : {no_generator}''')
            u_count +=1
     else:
            print(f'''you loose
                  user choice : {u_c}
                  computer choice : {no_generator}''' )
            c_count +=1
     i+=1
 
    if u_count == c_count:
         print("GAME DRW")
    elif u_count > c_count:
         print(f"YOU WIN , SCORE IS : {u_count}")  
    elif c_count > u_count: 
         print(f"COMPUTER WIN , SCORE IS : {c_count}")
          