import random
list_bet = [2, 2, 2, 6, 11, 4, 8, 10, 7, 7]
amount = [100, 400, 200, 60, 190, 200, 100, 300, 40, 80]
minimal_value = 50
amount_craps_verifie = []

list_bool = []


def AboveMinimum(amount_craps):
    for i in amount_craps:
        # we check like for roulette if a number from the list is inferior to the minimal value
        if i > minimal_value:
            # if it's, we equal it to 0 and put it in a new list
            i = 1
            list_bool.append(bool(i))
        elif i < minimal_value:
            i = 0
            list_bool.append(bool(i))

    return print(list_bool)

AboveMinimum(amount)

random_dice1 = random.randint(1, 6)
random_dice2 = random.randint(1, 6)


def Dices(dice1, dice2):
    return dice1+dice2

Dices(random_dice1, random_dice2)


def RollTheDices(bets, dice1, dice2):
    number_winner = 0
    result_bet = []
    result_dices = Dices(dice1, dice2)

    print("dice falls on", result_dices)

    for i in bets:

        if i == result_dices:

            i = True
            result_bet.append(bool(i))
            number_winner += 1
        elif i != result_dices:
            i = False
            result_bet.append(bool(i))
    if number_winner == 0:
        return print("there is no winner")
    elif number_winner > 0:
        return print("there is", number_winner, "number of winner")


RollTheDices(list_bet, random_dice1, random_dice2)


def SimulateGame(list_m2, list_b2):
    list_mise2_verifie = []
    money_casino = 0
    instant_loss = 0

    for i in list_m2:

        if i < minimal_value:

            instant_loss += i
            i = 0
            list_mise2_verifie.append(int(i))
        elif i >= minimal_value:

            list_mise2_verifie.append(int(i))
            print(list_mise2_verifie)
            print(instant_loss)

    number_winner = 0
    random_number = random.randint(1, 6)+random.randint(1, 6)

    total_money = sum(list_m2)
    money_betted = sum(list_mise2_verifie)
    money_won = []
    list_resultat = []
    list_winner = []
    for i in list_b2:
        if i == random_number:
            if i == 2 or i == 12:

                number_winner += 1
                i = 30
                list_resultat.append(int(i))

            elif i == 3 or i == 11:
                number_winner += 1
                i = 15
                list_resultat.append(int(i))

            elif i == 4 or i == 10:
                number_winner += 1
                i = 10
                list_resultat.append(int(i))

            elif i == 5 or i == 9:
                number_winner += 1
                i = 7.5
                list_resultat.append(int(i))
            elif i == 6 or i == 8:
                number_winner += 1
                i = 6
                list_resultat.append(int(i))
            elif i == 7:
                number_winner += 1
                i = 4
                list_resultat.append(int(i))

        elif i != random_number:
            i = 0
            list_resultat.append(int(i))

    print(list_resultat)

    list_winner = [list_mise2_verifie[i] * list_resultat[i] for i in range(0, len(list_resultat))]

    for i in list_winner:
        money_won.append(i)

    print(money_won)
    money_casino = total_money - sum(money_won)
    if number_winner == 0:
        print("The casino has won", total_money)
        return print("there are no winner this round")

    else:
        print("the casino has won", money_casino)
        print(list_winner)
        return print("there is", number_winner, "winner this round")


SimulateGame(amount, list_bet)