import random

def roll_dice():
    return random.randint(1, 6)

def calculate_probability(num_trials):
    same_count = 0
    for _ in range(num_trials):
        dice1 = roll_dice()
        dice2 = roll_dice()
        if dice1 == dice2:
            same_count += 1
    probability = same_count / num_trials
    return probability

def main():
    num_trials = int(input("Enter the number of trials: "))
    probability = calculate_probability(num_trials)
    print(f"The probability of getting the same number on both dice in {num_trials} trials is: {probability:.4f}")

if _name_ == "_main_":
    main()