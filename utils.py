from strategies import *
from extra_text import *

c_choices = ["C", "Cooperate", "c", "cooperate"]
d_choices = ["D", "Defect", "d", "defect"]
all_strategies = [random_action, jesus, susej, tit_for_tat]
yes_intents = ["yes", "yeah", "sure", "y"]
no_intents = ["no", "nah", "n"]


def evaluate(you, opp):
    '''
    (3,3) if both cooperate,
    (0,0) if both defect, and
    (5,0) or (0,5) if one cooperates and one defects
    '''
    if (you == 'C' and opp == 'C'): y = 3; o = 3
    elif (you == 'C' and opp == 'D'): y = 0; o = 5
    elif (you == 'D' and opp == 'C'): y = 5; o = 0
    elif (you == 'D' and opp == 'D'): y = 0; o = 0

    return y, o

def opponent(you, strategy=random_action):
    '''
    this function plays the action of the opponent
    if no strategy is specified, the opponent acts randomly
    '''
    opp = strategy(you)

    return opp

def check_input(you):
    '''validate the input'''
    # the input corresponds to cooperation
    if you in c_choices:
        you = 'C'
    # the input corresponds to defection
    elif you in d_choices:
        you = 'D'
    # the input doesn't correspond neither to cooperation nor to defection
    else:
        you = input("I could not understand what you mean. Do you want to cooperate or defect? ")
        you = check_input(you)

    return you

def unknow_strategy():
    '''
    IMPORTANT: THIS IS A META STRATEGY
    random strategy
    '''
    return random.choice(all_strategies)

def message(you, opp):
    '''personalized answers after each iteration'''

    if (you == 'C' and opp == 'C'):
        msg =  "You have chosen to cooperate, your opponent too. "
    elif (you == 'C' and opp == 'D'):
        msg = "Oups! you have chosen to cooperate, but your opponent betrayed you. "
    elif (you == 'D' and opp == 'C'):
        msg = "You have chosen to defect, yet your opponent cooperated. "
    elif (you == 'D' and opp == 'D'):
        msg = "You both have chosen to defect each other. "

    return msg

def doc_strategies(strategy):
    '''know more about each strategy'''

    answer = input(f"\nDo you want to know more about {strategy.__name__} strategy? ")
    if answer in yes_intents:
        result = strategy.__doc__
    else:
        result = "okay, bye!"

    return result

def introduction(extra=False):
    '''welcome + explain the game concept and rules'''

    # welcome message
    welcome = "Hey! welcome to the prisoner's dilemma game\n"
    print(welcome)
    answer = ""

    # game concept and rules
    if extra:
        if input("Do you want to know more about the prisoner's dilemma?") in yes_intents:
            answer = intro
        else:
            answer = "Ok. Let's play now!"

    return welcome, answer
