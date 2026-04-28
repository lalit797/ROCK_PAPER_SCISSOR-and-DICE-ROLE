from rockpaperscisor import r_p_s
from diceroll import d_r
print("==========WELCOME TO MY GAME SIMULATION==========")
def main():
 while True:
    user_choice  = int(input('''
          press 1. to play rock-paper-scissor
          press 2. to dice role '''))
    if user_choice == 1:
        r_p_s()
    elif user_choice == 2:
        d_r()
    else:
        print("SAHI NUMBER DAAL YAAR, KAAM DIMAG HAI KYA !!!!")    

main()