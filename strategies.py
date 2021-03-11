import random

choices = ['C', 'D']

def random_action(*args):
    '''
    The opponent acts randomly.
    '''
    return random.choice(choices)

def jesus(*args):
    '''
    The opponent always cooperates.
    '''
    return 'C'

def susej(*args):
    '''
    Inverted Jesus: The opponent always defects.
    '''
    return 'D'

def tit_for_tat(hist_you, *args):
    '''
    The opponent starts by cooperating, then cooperates if you cooperated last time, and defects otherwise.
    '''
    if len(hist_you) == 0:
        return 'C'
    else:
        return hist_you[-1]

def aggressive_tit_for_tat(hist_you, *args):
    '''
    The opponent starts by defecting, then cooperates if you cooperated last time, and defects otherwise.
    '''
    if len(hist_you) == 0:
        return 'D'
    else:
        return hist_you[-1]

def dolphin(hist_you, *args):
    '''
    The opponent have a long memory.
    If you betray him, the opponent will never cooperate with you again.
    '''
    if (hist_you.count('D') >= 1):
        return 'D'
    else:
        return 'C'

def lite_dolphin(hist_you, *args):
    '''
    The opponent have a long memory, but they turn a blind eye to a single betrayal.
    If you betray him more than once, the opponent will never cooperate with you again.
    '''
    if (hist_you.count('D') >= 2):
        return 'D'
    else:
        return 'C'

def judas(hist_you, sum_o, sum_y, *args):
    '''
    The opponent cooperates if they are winning, and defects if they are losing.
    '''
    # sum_o, sum_y: scores of the two players
    if (sum_o > sum_y):
        return 'C'
    else:
        return 'D'

def saduj(hist_you, sum_o, sum_y, *args):
    '''
    Inverted Judas:
    The opponent defects if they are winning, and cooperates if they are losing.
    '''
    # sum_o, sum_y: scores of the two players
    if (sum_o > sum_y):
        return 'D'
    else:
        return 'C'

def split(hist_you, iterations, i, *args):
    '''
    The opponent cooperates in the beginning, then changes behavior abruptly and starts defecting for the rest of the game.
    '''
    # iterations is the number of iterations in a game
    # i is the number of the current iteration
    half = int(iterations/2)

    if (i < half):
        return 'C'
    else:
        return 'D'

def vampire(hist_you, sum_o, sum_y, *args):
    '''
    The opponent acts randomly, but once they got a score superior to yours, they don't cooperate anymore.
    '''
    # sum_o, sum_y: scores of the two players
    if (sum_o > sum_y):
        return 'D'
    else:
        return random.choice(choices)

def kind_lizard(hist_you, *args):
    '''
    The opponent adapts to your average choices.
    If your number of cooperations equals your number of betrayals, they cooperate.
    '''
    if (hist_you.count('D') > hist_you.count('C')):
        return 'D'
    else:
        return 'C'

def unkind_lizard(hist_you, *args):
    '''
    The opponent adapts to your average choices.
    If your number of cooperations equals your number of betrayals, they defect.
    '''
    if (hist_you.count('D') >= hist_you.count('C')):
        return 'D'
    else:
        return 'C'

def noob_mentalist(hist_you, iterations, i, *args):
    '''
    The opponent tries to read your strategy by first defecting then cooperating.
    If you cooperate both times, they assume jesus and begin cooperating.
    If you defect both times, they assume susej and begin defecting.
    If you cooperate then defect, they assume tit for tat and begin cooperating until the last round then defect.
    If you defect then cooperate, they assume noob mentalist and begin cooperating.
    '''
    # iterations is the number of iterations in a game
    # i is the number of the current iteration
    if (i == 0):
        return 'D'
    elif (i == 1):
        return 'C'

    elif (hist_you[0] == 'C') and (hist_you[1] == 'C'):
        ## assume Jesus
        return 'C'

    elif (hist_you[0] == 'C') and (hist_you[1] == 'D'):
        ## assume Tit For Tat
        if (i == iterations-1):
            return 'D'
        else:
            return 'C'

    elif (hist_you[0] == 'D') and (hist_you[1] == 'C'):
        ## assume Noob Mentalist
        return 'C'

    elif (hist_you[0] == 'D') and (hist_you[1] == 'D'):
        ## assume Susej
        return 'D'
