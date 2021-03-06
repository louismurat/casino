import random
number_of_roulette = 10
number_of_craps = 10
number_of_barmen = 4
minimal_bet = 50
wage = 200
money_begin_casino = 50000
money_bachelor = 200
number_of_regular = 50
number_of_one_time = 40
number_of_bachelor = 10
mise_roulette = random.randint(0, 36)
mise_craps = random.randint(0, 12)


# First we define what we need for the casino : customer and employee
class casino(object):
    def __init__(self, employee, customer):
        self.employee = employee
        self.customer = customer

# then we create the class employee
class employee(casino):
    def __init__(self,money_begin,money_won):
        self.money_begin = money_begin
        self.money_won = money_won


class barman(employee) :
    def __init__(self,money_won,money_beginning):
      self.money_won = money_won

    def money_beginning(self):
        return wage


class croupier(employee):
    def __init__(self,money_begin,money_won):
      self.money_won = money_won

    def money_beginning(self):
        return wage


class casino_banq(employee):
    def __init__(self,money_begin,money_won):
      self.money_won = money_won
    def money_beginning(self):
        return money_begin_casino - number_of_barmen * wage - (number_of_craps + number_of_roulette) * 200 - number_of_bachelor * money_bachelor

#we create the customer class
class customer(casino):
    def __init__(self, money,money_beginning,amount_betted):
      self.money = money
      self.money_beginning = money_beginning
      self.money_bet = money_bet


class regular(customer):
    def __init__(self, money, amount_betted):
      self.money = money

    def amount_betted(self):
        return minimal_bet

    def money_beginning(self):
        money_beginning=random.randint(100,300)
        return(money_beginning)


class one_time(customer):
    def __init__(self,money, money_begining, amount_betted):
      self.money = money

    def amount_betted(self):
        return (random.randint(0,33)/100)*money

    def money_beginning(self):
        money_beginning=random.randint(100, 300)
        return money_beginning


class bachelor(customer):
    def __init__(self, money_arrival, amount_betted):
      self.money = random.randint(200, 500) + money_bachelor

    def amount_betted(self):
        return (random.randint(0, 100) / 100) * money

    def money_beginning(self):
        money_beginning = random.randint(200, 500) + money_bachelor
        return money_beginning