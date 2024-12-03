import random

def draw_card():
    """Draws a random card from the deck."""
    return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])

def hand_value(hand):
    """Calculates the value of a hand."""
    value = sum(hand)
    # Adjust for aces if value exceeds 21
    while value > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        value = sum(hand)
    return value

def play_hand(player_hand, dealer_hand, balance, bet):
    """Recursive gameplay for the player."""
    print(f"\nYour hand: {player_hand} (value: {hand_value(player_hand)})")
    print(f"Dealer's hand: [{dealer_hand[0]}, ?]")
    
    if hand_value(player_hand) > 21:
        print("You busted! Dealer wins!")
        return balance - bet

    action = input("Hit (H) or Stand (S)? ").strip().upper()
    if action == "H":
        player_hand.append(draw_card())
        return play_hand(player_hand, dealer_hand, balance, bet)
    elif action == "S":
        return dealer_turn(player_hand, dealer_hand, balance, bet)
    else:
        print("Invalid input. Please enter H or S.")
        return play_hand(player_hand, dealer_hand, balance, bet)

def dealer_turn(player_hand, dealer_hand, balance, bet):
    """Recursive dealer gameplay."""
    print(f"\nDealer's hand: {dealer_hand} (value: {hand_value(dealer_hand)})")
    if hand_value(dealer_hand) < 17:
        dealer_hand.append(draw_card())
        return dealer_turn(player_hand, dealer_hand, balance, bet)
    
    player_score = hand_value(player_hand)
    dealer_score = hand_value(dealer_hand)
    
    if dealer_score > 21 or player_score > dealer_score:
        print("You win!")
        return balance + bet
    elif player_score < dealer_score:
        print("Dealer wins!")
        return balance - bet
    else:
        print("It's a tie!")
        return balance

def start_game(balance):
    """Main menu for the game."""
    print("\n--- Welcome to Recursive Blackjack! ---")
    print("B: Bet")
    print("X: Exit")
    choice = input("Choose an option: ").strip().upper()

    if choice == "B":
        try:
            bet = int(input(f"Your balance: {balance}\nEnter your bet: "))
            if bet > balance or bet <= 0:
                print("Invalid bet amount.")
                return start_game(balance)
            player_hand = [draw_card(), draw_card()]
            dealer_hand = [draw_card(), draw_card()]
            balance = play_hand(player_hand, dealer_hand, balance, bet)
            print(f"\nYour new balance: {balance}")
            return start_game(balance)
        except ValueError:
            print("Please enter a valid number.")
            return start_game(balance)
    elif choice == "X":
        print("Thanks for playing! Your final balance:", balance)
        return
    else:
        print("Invalid choice. Try again.")
        return start_game(balance)

# Start the game
start_game(100)  # Initial balance