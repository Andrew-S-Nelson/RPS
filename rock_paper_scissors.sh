usr=0
cpu=0
while [ 0 -eq 0 ]
do
    echo -------------------
    echo rock paper scissors
    echo "usr $usr | cpu $cpu"
    userin=""
    read -p 'user chooses: ' userin
    userchoice=0
    
    # userin to numeric choice
    if [ $userin == 'rock' ];
    then
        userchoice=0
    elif [ $userin == 'paper' ];
    then
        userchoice=1
    elif [ $userin == 'scissors' ];
    then
        userchoice=2
    else
        clear
        echo 'invalid input'
        continue
    fi
    
    # computer choice
    
    
    # scoring
    
done
