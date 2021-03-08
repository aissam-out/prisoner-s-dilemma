from utils import *

def playmultiple(iterations, follow_up=False):
    '''Play prisoner's dilemma multiple times'''

    # score of the two players
    sum_y = 0
    sum_o = 0
    # history of inputs from the user
    hist_you = []
    # history of inputs from the opponent
    hist_opp = []
    # randomly select a strategy
    strategy = unknown_strategy()

    # intro to the game
    introd = introduction(extra=True)
    print(introd)

    # play n times
    for i in range(iterations):
        # generate the opponent action
        opp = opponent(hist_you, hist_opp, sum_y, sum_o, iterations, i, strategy)
        # input in validate the user's choice
        you = input('Your turn: ')
        you = check_input(you)
        # score the two players
        score_y, score_o = evaluate(you, opp)
        sum_y += score_y
        sum_o += score_o
        # print an adequate message
        msg = message(you, opp) + f"Score: {sum_y}:{sum_o}"
        print(msg)
        # append the last input from the user & opponent
        hist_you.append(you)
        hist_opp.append(opp)

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
