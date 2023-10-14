RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

first=input("Enter the First Player Name : ")
second=input("Enter the Second Player Name :  ")
print("\n")
print("-------------------------------------")
print(f"{GREEN}          SCORE BOARD{RESET}")
print("-------------------------------------")
print("    ",first)
print("\n")
print("    ",second)
print("\n")
print("-------------------------------------")
print("\n")
    
borad = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,len(borad)):
    for j in range(0,len(borad)):
        print("|",borad[i][j],end="   ")
    print()
    print("|-----|-----|-----")
print("\n")   
    
print("Enter 1 to 9")
sum_x = 0
sum_o = 0
l1 = []
l2 = []
l = 0
ll = 0
n=0
i=0
RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"

while(i>=0):
    
    x = int(input("X Trn:- "))
    
    if (x==1):
        borad[0][0] = f"{GREEN}X{RESET}"
        for i in range(0,len(borad)):
            for j in range(0,len(borad)):
                print(borad[i][j]," | ",end=" ")
            print()
            print("---|-----|-----")
            
    elif (x==2):
        borad[0][1] = f"{GREEN}X{RESET}"
        for i in range(0,len(borad)):
            for j in range(0,len(borad)):
                print(borad[i][j]," | ",end=" ")
            print()
            print("---|-----|-----")

    elif (x==3):
        borad[0][2] = f"{GREEN}X{RESET}"
        for i in range(0,len(borad)):
            for j in range(0,len(borad)):
                print(borad[i][j]," | ",end=" ")
            print()
            print("---|-----|-----")

    elif (x==4):
        borad[1][0] = f"{GREEN}X{RESET}"
        for i in range(0,len(borad)):
            for j in range(0,len(borad)):
                print(borad[i][j]," | ",end=" ")
            print()
            print("---|-----|-----")
            
    elif (x==5):
        borad[1][1] = f"{GREEN}X{RESET}"
        for i in range(0,len(borad)):
            for j in range(0,len(borad)):
                print(borad[i][j]," | ",end=" ")
            print()
            print("---|-----|-----")
            
    elif (x==6):
        borad[1][2] = f"{GREEN}X{RESET}"
        for i in range(0,len(borad)):
            for j in range(0,len(borad)):
                print(borad[i][j]," | ",end=" ")
            print()
            print("----------------")
            
    elif (x==7):
        borad[2][0] =f"{GREEN}X{RESET}"
        for i in range(0,len(borad)):
            for j in range(0,len(borad)):
                print(borad[i][j]," | ",end=" ")
            print()
            print("---|-----|-----")
    elif (x==8):
        borad[2][1] =f"{GREEN}X{RESET}"
        for i in range(0,len(borad)):
            for j in range(0,len(borad)):
                print(borad[i][j]," | ",end=" ")
            print()
            print("---|-----|-----")
            
    elif (x==9):
        borad[2][2] = f"{GREEN}X{RESET}"
        for i in range(0,len(borad)):
            for j in range(0,len(borad)):
                print(borad[i][j]," | ",end=" ")
            print()
            print("---|-----|-----")
            
            
    for i in range(0,1):
        for j in range(0,1):
            
                if (borad[i][j] == f'{GREEN}X{RESET}' and borad[i][j+1] == f'{GREEN}X{RESET}' and borad[i][j+2]==f'{GREEN}X{RESET}'):
                    n=1
                    print("Player 1 Win")
                    break
                elif (borad[j][i] == f'{GREEN}X{RESET}' and borad[j+1][i] == f'{GREEN}X{RESET}' and borad[j+2][i]==f'{GREEN}X{RESET}'):
                    n=1
                    print("Player 1 Win")
                    break

                elif (borad[0][0]==f'{GREEN}X{RESET}' and borad[1][1]==f'{GREEN}X{RESET}' and borad[2][2]==f'{GREEN}X{RESET}'):
                    n=1
                    print("Player 1 Win")
                    break

                elif (borad[0][2]==f'{GREEN}X{RESET}' and borad[1][1]==f'{GREEN}X{RESET}' and borad[2][0]==f'{GREEN}X{RESET}'):
                    n=1
                    print("Player 1 Win")
                    break
    if(n==1):
        print(" ____________________________________")
        print("|",f"{GREEN}         SCORE BOARD{RESET}","             |")
        print("|-----------------------------------|")
        print("|    ",first,"           ",f"{GREEN}WINNER{RESET}"," 🏆     |","\n")
        print("|","                                |")
        print("|    ",second,"           ",f"{RED}LOSER{RESET}","         |")
        print("|\n")
        print("|------------------------------------| ")
        
        break
    o = int(input("0 Trn:- "))
    l2.append(o)
    l = l + x

    if (o==1):
        borad[0][0] = f"{RED}O{RESET}"
        for i in range(0,len(borad)):
            for j in range(0,len(borad)):
                print(borad[i][j]," | ",end=" ")
            print()
            print("---|-----|-----")
            
    elif (o==2):
        borad[0][1] = f"{RED}O{RESET}"
        for i in range(0,len(borad)):
            for j in range(0,len(borad)):
                print(borad[i][j]," | ",end=" ")
            print()
            print("---|-----|-----")

    elif (o==3):
        borad[0][2] = f"{RED}O{RESET}"
        for i in range(0,len(borad)):
            for j in range(0,len(borad)):
                print(borad[i][j]," | ",end=" ")
            print()
            print("---|-----|-----")

    elif (o==4):
        borad[1][0] = f"{RED}O{RESET}"
        for i in range(0,len(borad)):
            for j in range(0,len(borad)):
                print(borad[i][j]," | ",end=" ")
            print()
            print("---|-----|-----")

    elif (o==5):
        borad[1][1] = f"{RED}O{RESET}"
        for i in range(0,len(borad)):
            for j in range(0,len(borad)):
                print(borad[i][j]," | ",end=" ")
            print()
            print("---|-----|-----")
    elif (o==6):
        borad[1][2] = f"{RED}O{RESET}"
        for i in range(0,len(borad)):
            for j in range(0,len(borad)):
                print(borad[i][j]," | ",end=" ")
            print()
            print("---|-----|-----")
            
    elif (o==7):
        borad[2][0] = f"{RED}O{RESET}"
        for i in range(0,len(borad)):
            for j in range(0,len(borad)):
                print(borad[i][j]," | ",end=" ")
            print()
            print("---|-----|-----")
    elif (o==8):
        borad[2][1] = f"{RED}O{RESET}"
        for i in range(0,len(borad)):
            for j in range(0,len(borad)):
                print(borad[i][j]," | ",end=" ")
            print()
            print("---|-----|-----")
            
    elif (o==9):
        borad[2][2] = f"{RED}O{RESET}"
        for i in range(0,len(borad)):
            for j in range(0,len(borad)):
                print(borad[i][j]," | ",end=" ")
            print()
            print("---|-----|-----")
            
            
    for i in range(0,1):
        for j in range(0,1):
            if (borad[i][j] == f'{RED}O{RESET}' and borad[i][j+1] == f'{RED}O{RESET}' and borad[i][j+2]==f'{RED}O{RESET}'):
                n=2
                print("Player 2 Win")
                break
            elif (borad[j][i] == f'{RED}O{RESET}' and borad[j+1][i] == f'{RED}O{RESET}' and borad[j+2][i]==f'{RED}O{RESET}'):
                n=2
                print("Player 2 Win")
                break
            
            elif (borad[0][0]==f'{RED}O{RESET}' and borad[1][1]==f'{RED}O{RESET}' and borad[2][2]==f'{RED}O{RESET}'):
                n=2
                print("Player 2 Win")
                break
                
            elif (borad[0][2]==f'{RED}O{RESET}' and borad[1][1]==f'{RED}O{RESET}' and borad[2][0]==f'{RED}O{RESET}'):
                n=2
                print("Player 2 Win")
                break
    if(n==2):
        print("-------------------------------------")
        print(f"{GREEN}          SCORE BOARD{RESET}")
        print("-------------------------------------")
        print("    ",first,"           ",f"{GREEN}LOSER{RESET}")
        print("\n")
        print("    ",second,"           ",f"{RED}WINNER{RESET}")
        print("\n")
        print("-------------------------------------")
        print("\n")
        break
break


    
