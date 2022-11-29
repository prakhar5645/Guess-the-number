n=[18, 56, 78, 45, 99, 4]
number_of_guess = 1
i=0
fch = 1
live = len(n) + 1
while (fch == 1):
    print(f"""\t\t***Welcome to Number guessing game***\n \t\t choose \t 1. Info \t 2. Start a Game \t 3. exit\n\t\t Thank you enjoy it \n\t\t""")
    wn = int(input())
    match wn:
        case 1:
            print(f"This game has {len(n)} level only. \n\t you have {live} lives. \n You have to choose the number exactly what is computer is thinking \n\t------Now Enjoy it-----\t write 1 for continue \t\t")
            fch=int(input("-->"))
        case 2:
            ch = 'y'
            while ch=='y':
                while(number_of_guess <= 9):
                    gn = n[i]
                    guess_number = int(input("----------Enter your number it will between [0-100]----------:\t\t"))
                    if guess_number < gn:
                        print("You Enter less number, please enter greater number.\n")
                    elif guess_number > gn:
                        print("You Enter greater number, please enter smaller number.\n")
                    else:
                        print("----------YOU WON----------")
                        print(number_of_guess, " lives you took to finish.\n")
                        if i >= (len(n) - 1):
                            print(f"You have Won all *{len(n)}* level og this.\n\t\t I hope you love this game.")
                            i=0
                            print("Do you want play this game again. Yes----> y OR No----> n :\t", end="")
                            ch = input()
                        else:
                            i += 1
                            print(f"Do you want play {i+1} level. Yes----> y OR No----> n :\t", end="")
                            ch = input()
                            print("")
                        break
                    print(f"{9-number_of_guess} lives left")
                    number_of_guess += 1

                if number_of_guess > 9:
                    print("----------***GAME OVER***----------")
                    number_of_guess = 1
                    print("Do you want play this game again. Yes----> y OR No----> n :\t", end="")
                    ch = input()
        
        case 3:
            print("****Thank you****")
            exit()