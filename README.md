# Prisoner's dilemma

The prisoners’ dilemma is the best-known game of strategy in Game Theory. In its traditional version, two members of a criminal gang are arrested and imprisoned. Each prisoner is in solitary confinement with no means of communicating with the other. 

Simultaneously, the prosecutors offer each prisoner a bargain. Each prisoner is given the opportunity either to betray the other by testifying that the other committed the crime, or to cooperate with the other by remaining silent [[ref]](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma). The possible outcomes are:

- If A and B each betray the other, each of them serves two years in prison
- If A betrays B but B remains silent, A will be set free and B will serve three years in prison
- If A remains silent but B betrays A, A will serve three years in prison and B will be set free
- If A and B both remain silent, both of them will serve only one year in prison (on the lesser charge).

In this project, we are implementing a slightly different version of the Prisoner's dilemma: We actually keep the same concept and change the rewards to:

- If they both betray each other, they get nothing.
- If one cooperates whereas the other defects, the former get 5 points while the latter get nothing.
- If they both cooperate, each of them gets 3 points.

## Strategies

In this implementation, the opponent picks (randomly) one of the following strategies, and plays a 10 iterations game.

**- Random action:** The opponent acts randomly.

**- Jesus:** The opponent always cooperates.

