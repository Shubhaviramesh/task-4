import random
def rock_paper_scissor():
    user_score=0
    computer_score=0

    while True:
        print("Let's play Rock-Paper-Scissor!!!")
        print("Choose your move : rock, paper, or scissor")
        user_choice=input().lower()
        computer_choice=random.choice(['rock', 'paper', 'scissor'])
        print(f"Your choice : {user_choice}")
        print(f"Computer's choice : {computer_choice}")
        if user_choice==computer_choice:
            print("IT'S A TIE !")
        elif (user_choice == 'rock' and computer_choice == 'scissor') or \
             (user_choice == 'scissor' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock') :
             print("You win!")
             user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        print(f"Your score : {user_score} , Computer's score : {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
if __name__ == "__main__":        
    rock_paper_scissor()