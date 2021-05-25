# Prisoner's dilemma

<p>
  <img width="350" align='right' src="https://cdn.britannica.com/s:800x450,c:crop/43/186443-138-A4E61711/overview-prisoners-dilemma.jpg">
  <!--- credits to [https://cdn.britannica.com] --->
</p>

The prisoners’ dilemma is the best-known game of strategy in Game Theory. In its traditional version, two members of a criminal gang are arrested and imprisoned. Each prisoner is in solitary confinement with no means of communicating with the other. 

Simultaneously, the prosecutors offer each prisoner a bargain. Each prisoner is given the opportunity either to betray the other by testifying that the other committed the crime, or to cooperate with the other by remaining silent [[ref]](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma). The possible outcomes are:

- If A and B each betray the other, each of them serves two years in prison
- If A betrays B but B remains silent, A will be set free and B will serve three years in prison
- If A remains silent but B betrays A, A will serve three years in prison and B will be set free
- If A and B both remain silent, both of them will serve only one year in prison (on the lesser charge).

## Evaluation:

In this project, we are implementing a slightly different version of the Prisoner's dilemma: We actually keep the same concept and change the rewards to:

- If they both betray each other, they get nothing.
- If one cooperates whereas the other defects, the former get 5 points while the latter get nothing.
- If they both cooperate, each of them gets 3 points.

:trophy: **Game goal:** Exceed 30 points (in a 10-round game), and maximize your result.

You can look at it this way: You are sentenced to 30 years, each point saves you one year of prison, and beyond 30 each point is worth a fixed amount of money.
So the goal is to first get out of prison, then to maximize the amount of money.

## Strategies:

In this implementation, the opponent picks (randomly) one of the following strategies, and plays a 10 iterations game.

**- Random action:** The opponent acts randomly.

**- Jesus:** The opponent always cooperates.

**- Susej:** Inverted Jesus: The opponent always defects.

**- Tit For Tat:** The opponent starts by cooperating, then cooperates if you cooperated, and defects otherwise

**- Aggressive Tit For Tat:** The opponent starts by defecting, then cooperates if you cooperated last time, and defects otherwise.

**- Dolphin:** The opponent have a long memory. If you betray him, the opponent will never cooperate with you again.

**- Lite Dolphin:** The opponent have a long memory, but they turn a blind eye to a single betrayal. If you betray him more than once, the opponent will never cooperate with you again.

**- Judas:** The opponent cooperates if they are winning, and defects if they are losing.

**- Saduj:** Inverted Judas: The opponent defects if they are winning, and cooperates if they are losing.

**- Split:** The opponent cooperates in the beginning, then changes behavior abruptly and starts defecting for the rest of the game.

**- Vampire:** The opponent acts randomly, but once they got a score superior to yours, they don't cooperate anymore.

**- Kind Lizard:** The opponent adapts to your average choices. If your number of cooperations equals your number of betrayals, they cooperate.

**- Unkind Lizard:** The opponent adapts to your average choices. If your number of cooperations equals your number of betrayals, they defect.

**- Noob Mentalist:** The opponent tries to read your strategy by first defecting then cooperating.

  - If you cooperate both times, they assume _"jesus"_ and begin cooperating.

  - If you defect both times, they assume _"susej"_ and begin defecting.
  
  - If you cooperate then defect, they assume _"tit for tat"_ and begin cooperating until the last round then defect.
  
  - If you defect then cooperate, they assume _"noob mentalist"_ and begin cooperating.

## Extra:

Besides the required building blocks, we also implemented:

- A welcoming introduction to the game
- Documentation about each strategy
- The possibility to include/exclude these additions
- The possibility to customize the number of iterations and strategies

## IMPORTANT!

:warning: The directory [extra_assets/](extra_assets/) contains images used by other applications that are online.

DO NOT DELETE THEM!

## How to use

To use this code, just clone/download this repository, then run `# python prisonersdilemma.py` to start playing.

---
:rotating_light: Feel free to make pull requests to this project if you want to contribute ..
