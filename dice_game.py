import random
while True:
    try:
        number_of_dices = int(input('Enter number of dices: '))
        sum_num=0
        for a in range(number_of_dices):
            random_number = random.randint(1,6)
            sum_num+=random_number
            print('Dice number ',a+1,' rolled ', random_number)
        print('Sum of dices: ',sum_num)
        want_next = False
        while want_next == False:
            next_game = input('Type (n) for new game or (e) to exit\n')
            next_game = next_game.lower()
            if next_game == 'n':
                want_next=True
                continue
            elif next_game == 'e':
                exit()
            else:
                print('I dont know this, try again')
    except ValueError:
        print('Try again')
    
