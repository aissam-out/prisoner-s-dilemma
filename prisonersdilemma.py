from utils import *

def playmultiple(iterations, follow_up=False):
    '''Play prisoner's dilemma multiple times'''

    # score of the two players
    sum_y = 0
    sum_o = 0
    # last input from the user
    last_you = None
    # randomly select a strategy
    strategy = unknow_strategy()

    # intro to the game
    welcome, rules = introduction(extra=True)
    print(welcome)
    print(rules)

    # play n times
    for i in range(iterations):
        # generate the opponent action
        opp = opponent(last_you, strategy)
        # iput in validate the user's choice
        you = input('Your turn: ')
        you = check_input(you)
        # score the two players
        score_y, score_o = evaluate(you, opp)
        sum_y += score_y
        sum_o += score_o
        # print an adequate message
        msg = message(you, opp) + f"Score: {sum_y}:{sum_o}"
        print(msg)
        # keep the last input from the user to the next iteration
        last_you = you

    # reveal the opponent's strategy
    reveal_strategy = f"Your opponent was using {strategy.__name__} strategy."
    print(reveal_strategy)

    # more information about the opponent's strategy
    if follow_up:
        answer = doc_strategies(strategy)
        print(answer)


if __name__ == "__main__":
    iterations = 5
    playmultiple(iterations, True)
