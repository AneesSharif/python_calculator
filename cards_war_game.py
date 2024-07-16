import random
import cards_data


class Card():
    def __init__(self, shape, rank):
        self.shape = shape
        self.rank = rank
        self.value = cards_data.values[rank]

    def __str__(self):
        return f"{self.rank} of {self.shape}"
    

class Deck():
    def __init__(self):
        self.cards = [Card(shape,rank) for shape in cards_data.shapes for rank in cards_data.ranks]
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


class Plyaer():
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_cards(self, new_card):
        
        if type(new_card) == type([]):
            self.hand.extend(new_card)
        else:
            self.hand.append(new_card)
    
    def remove_card(self):
        return self.hand.pop(0)

    
    def __str__(self):
        return f"{self.name} has {len(self.hand)} card"


def war_game():

    player_1 = Plyaer("One")
    player_2 = Plyaer("Two")

    new_deck = Deck()

    for _ in range(26):
        player_1.add_cards(new_deck.draw())
        player_2.add_cards(new_deck.draw())

    game_on = True
    round_number = 0
    while game_on:
        
        round_number +=1
        print(f"we are at round number {round_number}")
         

        if len(player_1.hand) == 0:
            print("player 1 not have enough cards")
            print("player 2 won the game")
            game_on = False
            break

        elif len(player_2.hand) == 0:
            print("player 2 do not have enough card")
            print("So player 1 won the game")
            game_on = False
            break

        player_1_card = []
        player_1_card.append(player_1.remove_card())

        player_2_card = []
        player_2_card.append(player_2.remove_card())

        print(f"Player 1 card {player_1.hand} Player 2 card {player_2.hand}")

        at_war = True

        while at_war:
            if player_1_card[-1].value > player_2_card[-1].value:
                player_1.add_cards(player_1_card)
                player_1.add_cards(player_2_card)
                at_war = False
            
            elif player_2_card[-1].value > player_1_card[-1].value:
                player_2.add_cards(player_2_card)
                player_2.add_cards(player_1_card)
                at_war = False

            else:
                print("We are at war")
                if len(player_1.hand)< 5:
                    print("Player 1 do not have enogh cards")
                    print("player 2 won the game")
                    game_on = False
                    break

                elif len(player_2.hand)< 5:
                    print("Player 2 do not have enogh cards")
                    print("player 1 won the game")
                    game_on = False
                    break
                
                else:
                    for _ in range(5):
                        player_1_card.append(player_1.remove_card())
                        player_2_card.append(player_2.remove_card())
    
                    

war_game()