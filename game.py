import random as rd

def Game_Win(Comp , you):
    
    if Comp == you:
        return None
    elif Comp == 'S':
        if you == 'W':
            return False
        elif you == 'G':
            return True
    
    elif Comp == 'W':
        if you == 'G':
            return False
        elif you == 'S':
            return True
    elif Comp == 'G':
        if you == 'S':
            return False
        elif you == 'W':
            return True
        
#computer turn
print('Computer turn : Snake(S) or Water(W) or gun(G) ?')
random_Number = rd.randint(1,3)
if random_Number == 1 :
    Comp = 'S'
elif random_Number == 2:
    Comp = 'W'
elif random_Number == 3:
    Comp = 'G'

#your turn
you = input('Your turn : Snake(S) or Water(W) or gun(G) ?')
result = Game_Win(Comp , you)

print(f"Computer chose {Comp}")
print(f"You chose {you}")

if result == None :
    print('The match is a TIE..')
elif result == True :
    print('You WIN !!')
else :
    print('You LOOSE !')