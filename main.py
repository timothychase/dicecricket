import random

game = [100, 0, 0]
game_two = [100, 0, 0]
heads_or_tails = ["won", "lost"]
balls = 0
wickets = 1
total_runs = 2


def roll_dice(num):
    return random.randint(1, num)


def ball(g:list):
    input("\nBowler runs in...")
    outcome = roll_dice(5)
    if outcome == 1:
        print("quick single")
        g[total_runs] += outcome
    elif outcome == 2:
        split = roll_dice(2)
        if split == 1:
            runs = 2
            print("clipped away for two")
            g[total_runs] += runs
        elif split == 2:
            runs = 4
            print("driven through the covers for four")
            g[total_runs] += runs
    elif outcome == 3:
        split = roll_dice(3)
        if split == 1:
            print("swings and misses - no run")
        elif split == 2:
            print("pushed back to the bowler - no run")
        elif split == 3:
            print("straight to the fielder - no run")
    elif outcome == 4:
        split = roll_dice(2)
        if split == 1:
            runs = 4
            print("pulled away for four")
            g[total_runs] += runs
        elif split == 2:
            runs = 6
            print("hammered into the stands for six")
            g[total_runs] += runs
    elif outcome == 5:
        g[wickets] = appeal(g[wickets])
    g[balls] += -1
    print("Score - " + str(g[total_runs]) + "/" + str(g[wickets]))
    print("Balls remaining - " + str(g[balls]))
    return g


def appeal(w):
    if w in (0, 1, 2, 3, 4):
        outcome = roll_dice(5)
        if outcome == 1:
            print("bowled!")
            w += 1
        elif outcome == 2:
            print("caught behind!")
            w += 1
        elif outcome in (3, 4, 5):
            print("straight to the fielder - no run")
    elif w in (5, 6, 7):
        outcome = roll_dice(5)
        if outcome == 1:
            print("trapped in front - LBW!")
            w += 1
        elif outcome == 2:
            print("looks to clear the infield - caught!")
            w += 1
        elif outcome == 3:
            print("quick single - run out!")
            w += 1
        elif outcome in (4, 5):
            print("straight to the fielder - no run")
    elif w in (8, 9, 10):
        outcome = roll_dice(5)
        if outcome in (1, 2, 3, 4):
            print("slogged away - caught in the deep!")
            w += 1
        elif outcome == 5:
            print("swings and misses - no run")
    return w


def innings_one(g:list):
    while g[wickets] < 10 and g[balls] > 0:
        g = ball(g)
    print("\nInnings Over")
    return g

def innings_two(g:list):
    while g[wickets] < 10 and g[balls] > 0 and g[total_runs] <= game[total_runs]:
        g = ball(g)
        print("Runs required - " + str(game[total_runs] - g[total_runs] + 1))
    print("\nInnings Over")
    return g

def toss(h:list):
    print("The Toss")
    answer = input("Call heads or tails ")
    while answer not in ("heads", "tails"):
        answer = input("Call heads or tails")
    print("You have called " + answer)
    flip = roll_dice(2)
    if flip == 1:
        outcome = "heads"
        print("Coin lands on heads")
    elif flip == 2:
        outcome = "tails"
        print("Coin lands on tails")
    if answer == outcome:
        print("You have won the toss")
        return h[0]
    else:
        print("You have lost the toss")
        return h[1]


def toss_won():
    if heads_or_tails == "won":
        answer = input("\nWould you like to bat or bowl? ")
        while answer not in ("bat", "bowl"):
            answer = input("\nWould you like to bat or bowl? ")
        if answer == "bat":
            print("You are the batting team")
        elif answer == "bowl":
            print("You are the bowling team")
        return answer
    elif heads_or_tails == "lost":
        flip = roll_dice(2)
        if flip == 1:
            print("\nYou are the batting team")
            return "bat"
        elif flip == 2:
            print("\nYou are the bowling team")
            return "bowl"


def toss_two():
    if bat_or_bowl_first == "bat":
        print("\nYou are the bowling team")
    elif bat_or_bowl_first == "bowl":
        print("\nYou are the batting team")


def result():
    if bat_or_bowl_first == "bat":
        if game[total_runs] > game_two[total_runs]:
            print("You won!")
        else:
            print("You lost!")
    elif bat_or_bowl_first == "bowl":
        if game[total_runs] < game_two[total_runs]:
            print("You won!")
        else:
            print("You lost!")


heads_or_tails = toss(heads_or_tails)

bat_or_bowl_first = toss_won()

game = innings_one(game)

toss_two()

game_two = innings_two(game_two)

result()