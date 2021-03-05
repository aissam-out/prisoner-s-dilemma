import random

choices = ['C', 'D']

def random_action(last_you):
    '''
    The opponent acts randomly
    '''
    return random.choice(choices)

def jesus(last_you):
    '''
    The opponent always cooperates
    '''
    return 'C'

def susej(last_you):
    '''
    Inverted Jesus: The opponent always defects
    '''
    return 'D'

def tit_for_tat(last_you):
    '''
    The opponent starts by cooperating, then cooperates if you cooperated,
    and defects otherwise
    '''
    if last_you == None:
        return 'C'
    else:
        return last_you
