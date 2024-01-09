""" 

Simple Black Jack game
 
"""

import random


class Deck:
    def __init__(self):
        suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
        ranks = ('2', '3', '4', '5', '6', '7', '8', '9',
                 '10', 'Jack', 'Queen', 'King', 'Ace')
        self.cards = [(rank, suit) for suit in suits for rank in ranks]
        # self.shuffle()

    def __str__(self):
        deck_as_string = ""
        for card in self.cards:
            deck_as_string += (f"{card}\n")
        return deck_as_string

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards=1):
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards


def calculate_score(dealt_cards):
    score = 0
    num_aces = 0

    # Beräkna poängen för spelarens hand
    for card in dealt_cards:
        if card[0].isdigit():
            score += int(card[0])
        elif card[0] in ['Jack', 'Queen', 'King']:
            score += 10
        elif card[0] == 'Ace':
            num_aces += 1
            score += 11  # Standardvärde för ess är 11

    # Justera för ess
    while num_aces > 0 and score > 21:
        score -= 10
        num_aces -= 1

    return score


game_deck = Deck()
player_score = 0
dealer_score = 0
#print(f"Debug: {game_deck}")
game_deck.shuffle()
#print(f"Debug: {game_deck}")

dealer_hand = game_deck.deal(2)
player_hand = game_deck.deal(2)

while True:
    dealer_score = calculate_score(dealer_hand)
    player_score = calculate_score(player_hand)

    print(f"Dealer first card: {dealer_hand[0][0]} of {dealer_hand[0][1]}")

    for card in player_hand:
        print(f"Player hand: {card[0]} of {card[1]}")

    print(f"Player score: {player_score}")

    # Kolla om spelaren har blackjack
    if player_score == 21:
        print("Blackjack! You win!")
        break

    player_choice = input(
        "Type 'y' to get another card, 'n' to pass: ").lower()

    if player_choice == 'y':
        player_hand += game_deck.deal(1)

        player_score = calculate_score(player_hand)

        # Kolla om spelaren har överskridit 21 poäng (gått över)
        if player_score > 21:
            for card in player_hand:
                print(f"Player hand: {card[0]} of {card[1]}")
            print("Busted! You lose.")
            break
    elif player_choice == 'n':
        # Datorns tur att spela
        while dealer_score < 17:
            dealer_hand += game_deck.deal(1)
            dealer_score = calculate_score(dealer_hand)

        print(
            f"Your final hand: {[card[0] for card in player_hand]}, Your final score: {player_score}")
        print(
            f"Dealer's final hand: {[card[0] for card in dealer_hand]}, Dealer's final score: {dealer_score}")

        # Kolla vinnaren baserat på poäng
        if dealer_score > 21:
            print("Dealer busted! You win!")
        elif dealer_score > player_score:
            print("You lose.")
        elif dealer_score < player_score:
            print("You win!")
        else:
            print("It's a draw!")

        break
