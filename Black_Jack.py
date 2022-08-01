import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self, suit, rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    
    def __init__(self):
        self.deck = []  
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
                
    
    def __str__(self):
        deck_comp = ''
        for i in self.deck:
            deck_comp += '\n '+ i.__str__()
        return "The deck has: " + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []  
        self.value = 0   
        self.aces = 0    
    
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self):
        self.total = 100  
        self.bet = 0
        
    def win_bet(self):
        self.total+=self.bet
    
    def lose_bet(self):
        self.total-=self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("Enter number of chips: "))
        
        except ValueError:
            print("Not an integer, try again.")
        
        else:
            if chips.bet>chips.total:
                print("Sorry, your bet exceeded total: ",chips.total)
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        x = input("Enter 'h' for Hit or 's' for Stand: ")
        if x[0].lower()=='h':
            hit(deck, hand)
        elif x[0].lower()=='s':
            print("Player Stands, Dealer is playing.")
            playing=False
        else:
            print("Invalid response, try again:")
            continue
        break

#display 1 card of dealer and all of player
def show_some(player,dealer):
    #show only one of the dealer's card
    print("\n Dealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])
    #show all (2 cards) of the player's hands/cards
    print("\nplayer's hand: ")
    for i in player.cards:
        print(i)
    pass

#display all cards of dealer and player    
def show_all(player,dealer):
    print("\ndealer's hand: ")
    for i in dealer.cards:
        print(i)
        
    print(f"Value of dealer's hand: {dealer.value}")
    
    print("\nplayer's hand: ")
    for i in player.cards:
        print(i)
        
    print(f"Value of dealer's hand: {player.value}")
    pass


#end results
def player_busts(player,dealer,chips):
    print("Busted!")
    chips.lose_bet()
    pass

def player_wins(player,dealer,chips):
    print("Player won!")
    chips.win_bet()
    pass

def dealer_busts(player,dealer,chips):
    print("Dealer Busted!")
    chips.win_bet()
    pass
    
def dealer_wins(player,dealer,chips):
    print("Dealer won!")
    chips.lose_bet()
    pass
    
def push(player,dealer):
    print("It's a tie!")
    pass


#Algorithm

while True:
    print("Welcome to Black Jack!")
    

    new_deck=Deck()
    new_deck.shuffle()
    
    player=Hand()
    player.add_card(new_deck.deal())
    player.add_card(new_deck.deal())
    
    dealer=Hand()
    dealer.add_card(new_deck.deal())
    dealer.add_card(new_deck.deal())
    
    player_chips=Chips()
    
    #ask for bet
    take_bet(player_chips)
    
    #show cards of player and 1 card of dealer
    show_some(player, dealer)
    
    while playing:
        
        #asking for hit or stand
        hit_or_stand(new_deck, player)
        
        show_some(player, dealer)
        
        #checking for a bust
        if player.value > 21:
            player_busts(player, dealer, player_chips)
            break

    if player.value<=21:
        while dealer.value < 17:
            hit(new_deck, dealer)
            
        show_all(player, dealer)

        #checking for bust
        if dealer.value>21:
            dealer_busts(player, dealer, player_chips)
            
        elif dealer.value > player.value:
            dealer_wins(player, dealer, player_chips)
            
        elif player.value > dealer.value:
            player_wins(player, dealer, player_chips)
                
        else:
            push(player, dealer)
    
    #chips total
    print(f"Total chips left: {player_chips.total}")
    
    # Ask to play again
    x=input('Press "y" if want to play again, else press "n"')
    if x=='y':
        playing=True
        continue
    elif x=='n':
        break