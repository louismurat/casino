import random
# we define all that we are gonna need:
# To begin we need an example of a list of bet
list_mise = [80, 20, 80, 100, 10, 100, 30, 400, 70, 120]
# a list of example of bet
list_bet = [1, 2, 2, 3, 2, 8, 9, 17, 21, 20]
minimal_value = 50


# we define the function
def AboveMinimum (list_mise):

    # we create a vector
    amount_booleans = []

    for i in list_mise:
        if i < 0:  # the first condition to check if there is no problem in the list
            return print("problem of number")
        elif i < minimal_value:  # the second condition to check if it's inferior to the minimal value
            i = False
            # we add the boolean to a list
            amount_booleans.append(bool(i))

        elif i >= minimal_value:  # for the second case
            i = True
            amount_booleans.append(bool(i))
    print(list_mise)
    return amount_booleans

AboveMinimum(list_mise)


def SpinTheWheel(list_b2):
    # we define what we are going to need and we create a random number
    number_winner=0
    random_number = random.randint(0, 36)
    list_resultat=[]

    for i in list_b2:
        if i < 0 or i > 36:  # we first verify that there is not a wrong number added
            return print("Not a good bet")

        elif i == random_number:  # if there is a winner
            # first we add one to the number of winner
            number_winner += 1
            # we create a new list composed of 0 and 1 to tell us where is the winner
            i = 1
            list_resultat.append(int(i))

        elif i != random_number:
            # in the other case we put a 0
            i = 0
            list_resultat.append(int(i))
    print("Spinning The Wheel")
    print("Ball lands on", random_number)
    print(list_resultat)
    if number_winner == 0:  # if number of winner is equal to 0 no one won
        print("there are no winners")
        return list_resultat, number_winner

    elif number_winner != 0:
        print("there are", number_winner, "correct bets")
        return list_resultat, number_winner


SpinTheWheel(list_bet)


def SimulateGame(list_m2, list_b2):
    # we now simulate the game we use the same structure that the previous games
    list_mise2_verifie = []
    money_casino = 0
    instant_loss = 0
    list_money = []
    if len(list_m2) != len(list_b2):
        return print("problem of bet")
    elif len(list_m2) == len(list_b2):
        for i in list_m2:

            if i < minimal_value:
                # we create instant loss which will collect all the bet inferior to the minimal value

                instant_loss += i
                # we create a new list with all the result
                i = 0
                list_mise2_verifie.append(int(i))
            elif i >= minimal_value:

                list_mise2_verifie.append(int(i))

        number_winner = 0
        random_number = random.randint(0, 36)

        total_money = sum(list_m2)
        money_betted = sum(list_mise2_verifie)
        money_won = []
        list_resultat = []
        list_winner = []
        for i in list_b2:
            if i < 0 or i > 36:
                return print("Not a good bet")

            elif i == random_number:
                number_winner += 1
                i = 1
                list_resultat.append(int(i))

            elif i != random_number:
                i = 0
                list_resultat.append(int(i))

        # we create the list of winner where we multiply each number of the list of the bet woth the list of resulata
        list_winner = [list_mise2_verifie[i] * list_resultat[i] for i in range(0, len(list_resultat))]
        # This gave how much someone that has win has bet

        for i in list_winner:
            # we multiply it by 30
            money_won.append(i * 30)

        # we compute the money won by the casino
        money_casino = total_money - sum(money_won)
        if number_winner == 0:
            print("The casino has won", total_money)
            return print("there are no winner this round")

        else:
            print("the casino has won", money_casino)
            print(list_winner)
            return print("there is", number_winner, "winner this round")


SimulateGame(list_mise, list_bet)
