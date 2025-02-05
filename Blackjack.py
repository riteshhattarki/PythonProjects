import p1_random as p1
rng = p1.P1Random()


choice = 0
hand_value = 0
game_number = 1
player_wins = 0
dealer_wins = 0
num_ties = 0

random_number = rng.next_int(13) + 1
hand_value += random_number
print(f"START GAME #{game_number}")
print()
print("Your card is a", str(random_number) + "!")
print(f"Your hand is: {hand_value}")

while choice != 4:
    print()
    print("1. Get another card")
    print("2. Hold hand")
    print("3. Print statistics")
    print("4. Exit")
    print()
    choice = int(input("Choose an option: "))

    if choice == 1:
        random_number = rng.next_int(13) + 1
        # hand_value += random_number
        if random_number == 1:
            print()
            print("Your card is a ACE!")
            hand_value += random_number
            print(f"Your hand is: {hand_value}")
        elif random_number == 11:
            print()
            print("Your card is a JACK!")
            hand_value += 10
            print(f"Your hand is: {hand_value}")
        elif random_number == 12:
            print()
            print("Your card is a QUEEN!")
            hand_value += 10
            print(f"Your hand is: {hand_value}")
        elif random_number == 13:
            print()
            print("Your card is a KING!")
            hand_value += 10
            print(f"Your hand is: {hand_value}")
        else:
            print()
            print("Your card is a", str(random_number) + "!")
            hand_value += random_number
            print(f"Your hand is: {hand_value}")
        if hand_value == 21:
            print("BLACKJACK! You win!")
            player_wins += 1
            game_number += 1
            hand_value = 0
            random_number = rng.next_int(13) + 1
            print(f"START GAME #{game_number}")
            print()
            if random_number == 1:
                print()
                print("Your card is a ACE!")
                hand_value += random_number
                print(f"Your hand is: {hand_value}")
            elif random_number == 11:
                print()
                print("Your card is a JACK!")
                hand_value += 10
                print(f"Your hand is: {hand_value}")
            elif random_number == 12:
                print()
                print("Your card is a QUEEN!")
                hand_value += 10
                print(f"Your hand is: {hand_value}")
            elif random_number == 13:
                print()
                print("Your card is a KING!")
                hand_value += 10
                print(f"Your hand is: {hand_value}")
            else:
                print()
                print("Your card is a", str(random_number) + "!")
                hand_value += random_number
                print(f"Your hand is: {hand_value}")
        elif hand_value > 21:
            print("You exceeded 21! You lose.")
            dealer_wins += 1
            game_number += 1
            hand_value = 0
            random_number = rng.next_int(13) + 1
            print(f"START GAME #{game_number}")
            print()
            if random_number == 1:
                print("Your card is a ACE!")
                hand_value += random_number
                print(f"Your hand is: {hand_value}")
            elif random_number == 11:
                print("Your card is a JACK!")
                hand_value += 10
                print(f"Your hand is: {hand_value}")
            elif random_number == 12:
                print("Your card is a QUEEN!")
                hand_value += 10
                print(f"Your hand is: {hand_value}")
            elif random_number == 13:
                print("Your card is a KING!")
                hand_value += 10
                print(f"Your hand is: {hand_value}")
            else:
                print("Your card is a", str(random_number) + "!")
                hand_value += random_number
                print(f"Your hand is: {hand_value}")
    elif choice == 2:
        dealer_random_number = rng.next_int(11) + 16
        print()
        print(f"Dealer's hand: {dealer_random_number}")
        print(f"Your hand is: {hand_value}")
        print()
        if dealer_random_number > 21:
            print("You win!")
            game_number += 1
            player_wins += 1
            hand_value = 0
            random_number = rng.next_int(13) + 1
            print()
            print(f"START GAME #{game_number}")
            print()
            # hand_value += random_number
            if random_number == 1:
                print("Your card is a ACE!")
                hand_value += random_number
                print(f"Your hand is: {hand_value}")
            elif random_number == 11:
                print("Your card is a JACK!")
                hand_value += 10
                print(f"Your hand is: {hand_value}")
            elif random_number == 12:
                print("Your card is a QUEEN!")
                hand_value += 10
                print(f"Your hand is: {hand_value}")
            elif random_number == 13:
                print("Your card is a KING!")
                hand_value += 10
                print(f"Your hand is: {hand_value}")
            else:
                print("Your card is a", str(random_number) + "!")
                hand_value += random_number
                print(f"Your hand is: {hand_value}")
        elif dealer_random_number == hand_value:
            print("It's a tie! No one wins!")
            game_number += 1
            num_ties += 1
            hand_value = 0
            random_number = rng.next_int(13) + 1
            print(f"START GAME #{game_number}")
            print()
            if random_number == 1:
                print()
                print("Your card is a ACE!")
                hand_value += random_number
                print(f"Your hand is: {hand_value}")
            elif random_number == 11:
                print()
                print("Your card is a JACK!")
                hand_value += 10
                print(f"Your hand is: {hand_value}")
            elif random_number == 12:
                print()
                print("Your card is a QUEEN!")
                hand_value += 10
                print(f"Your hand is: {hand_value}")
            elif random_number == 13:
                print()
                print("Your card is a KING!")
                hand_value += 10
                print(f"Your hand is: {hand_value}")
            else:
                print()
                print("Your card is a", str(random_number) + "!")
                hand_value += random_number
                print(f"Your hand is: {hand_value}")
        elif dealer_random_number > hand_value:
            print("Dealer wins!")
            dealer_wins += 1
            game_number += 1
            hand_value = 0
            random_number = rng.next_int(13) + 1
            print(f"START GAME #{game_number}")
            print()
            if random_number == 1:
                print("Your card is a ACE!")
                hand_value += random_number
                print(f"Your hand is: {hand_value}")
            elif random_number == 11:
                print("Your card is a JACK!")
                hand_value += 10
                print(f"Your hand is: {hand_value}")
            elif random_number == 12:
                print("Your card is a QUEEN!")
                hand_value += 10
                print(f"Your hand is: {hand_value}")
            elif random_number == 13:
                print("Your card is a KING!")
                hand_value += 10
                print(f"Your hand is: {hand_value}")
            else:
                print("Your card is a", str(random_number) + "!")
                hand_value += random_number
                print(f"Your hand is: {hand_value}")
            #print("Your card is a", str(random_number) + "!")
            #hand_value += random_number
            #print(f"Your hand is: {hand_value}")
    elif choice == 3:
        print()
        print("Number of Player wins:", player_wins)
        print("Number of Dealer wins:", dealer_wins)
        print("Number of tie games:", num_ties)
        print("Total # of games played is:", game_number - 1)
        print("Percentage of Player wins:", str(round((player_wins / (game_number - 1)), 2) * 100) + "%")
    elif choice == 4:
        break
    else:
        print("Invalid input!")
        print()
        print("Please enter an integer value between 1 and 4.")



