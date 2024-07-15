import random

cpu = 0
usr = 0

while (1):
    # prints title
    print("Rock Paper Scissors")
    print("cpu " + str(cpu) + " | usr " + str(usr))
    
    # User Plays
    userin = ""
    usrchoice = 0
    print("User chooses ", end="")
    input(userin)
    userin = userin.upper()
    if (userin == "rock"):
        userchoice = 0
    elif (userin == "paper"):
        userchoice = 1
    elif (userin == "scissor"):
        userchoice = 2
    
    # Computer Plays
    cpurand = random.randint(0, 2)
    if (cpurand == 0):
        print('Computer choose rock')
    elif (cpurand == 1):
        print('Computer choose paper')
    elif (cpurand == 2):
        print ('Computer choose scissors')
        
    # Scoring
    condition = 0 # 0 is draw 1 is user win 2 is cpu win
    if (usrchoice == cpurand):
        condition = 0
        print('Draw')
    if ((userchoice == 0 && cpurand == 2) || (userchoice = 1 && cpurand == 0) || (userchoice))
        
