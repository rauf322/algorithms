import random


def roll():
    roll = random.randint(1,6)
    return roll 
def main():
    players = int(input("Enter the number of Players from 2 to 4: "))
    while players < 2 or players > 4:
        players = int(input("Enter the number of Players from 2 to 4: "))
    player_score = [0 for _ in range(players)]
    while max(player_score) < 50:
        i = int(input("Who wanna try your lucky? "))
        player_score[i-1] += roll()
        for i in range(len(player_score)):
            print(f"Total Score of Player {i+1}:{player_score[i]}")

main()
