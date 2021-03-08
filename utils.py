from strategies import *
from extra_text import *

grp_1 = [random_action, jesus, susej, tit_for_tat, aggressive_tit_for_tat, dolphin, lite_dolphin, kind_lizard, unkind_lizard]
grp_2 = [judas, saduj, vampire]
grp_3 = [split, noob_mentalist]
all_strategies = grp_1 + grp_2 + grp_3

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

def opponent(hist_you, hist_opp, sum_y, sum_o, iterations, i, strategy):
    '''
    plays the action of the opponent.
    '''
    if strategy in grp_1:
        opp = strategy(hist_you, hist_opp)
    elif strategy in grp_2:
        opp = strategy(hist_you, sum_o, sum_y)
    elif strategy in grp_3:
        opp = strategy(hist_you, iterations, i)
    else:
        opp = random_action()
    return opp

def check_input(you):
    '''
    validate the input.
    '''
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

def unknown_strategy():
    '''
    IMPORTANT: THIS IS A META STRATEGY
    random strategy
    '''
    ## This could be calibrated using a custom probability distribution
    return random.choice(all_strategies)

def message(you, opp):
    '''
    personalized answers after each iteration
    '''

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
    '''
    know more about each strategy
    '''

    answer = input(f"\nDo you want to know more about {strategy.__name__} strategy? ")
    if answer in yes_intents:
        result = strategy.__doc__
    else:
        result = "okay, bye!"

    return result

def introduction(extra=False):
    '''
    welcome + explain the game concept and rules
    '''

    # game concept and rules
    if extra:
        if input("Hey! welcome to the prisoner's dilemma game\n\nDo you want to know more about the prisoner's dilemma?") in yes_intents:
            answer = intro
        else:
            answer = "\nOk. Let's play now!"

    return answer
