import random


def get_user_score():
    while True:
        try:
            user_score = int(input("Enter your score (1,000-100,000): "))
            if 1000 <= user_score <= 100000:
                return user_score
            else:
                print("Invalid score. Enter a score in the range 1,000 to 100,000.")
        except ValueError:
            print("Invalid input. Please enter a valid score.")


def get_computer_score(num_players=3):
    computer_score = [random.randint(1000, 100000) for _ in range(num_players)]
    return computer_score


def ranking_system(user_score, computer_scores):
    # combine user score and computer scores
    all_scores = [user_score] + computer_scores

    # sort the scores in descending order
    sorted_scores = sorted(all_scores, reverse=True)

    # display user rank
    user_rank = sorted_scores.index(user_score) + 1

    # display user rank
    print(f"You are ranked {user_rank} out of {len(all_scores)}!")

    # display scores and ranks
    print("\nOther Players:")
    for i, score in enumerate(all_scores, start=1):
        print(f"Player {i}: Score - {score}, Rank - {sorted_scores.index(score) + 1}")


# Example usage
while True:
    user_score = get_user_score()
    computer_scores = get_computer_score()
    ranking_system(user_score, computer_scores)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
