import random 
import ipywidgets as widgets
from IPython.display import Image, HTML, display

values = [ "ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "jack", "queen", "king" ]
suits  = [ "clubs", "diamonds", "hearts", "spades" ]
deck = [ v +"_of_"+ s for s in suits for v in values  ] 

random.shuffle(deck) 
price_money = 1000

def show(*card_names):
    length = len(card_names)
    if length == 0:
        print(" There is no card!")
    else:
        card_list = []
        for i in range(length):
            path_name = './deck/'+ card_names[i] + '.png'
            img = open(path_name, 'rb').read()
            img_resize = widgets.Image(value= img, format='png', width=60, height=40)
            card_list.append(img_resize)
        sidebyside = widgets.HBox(card_list)
        display(sidebyside)

def solution_1_a():
    
    # Function
    def get_points():
        card = deck.pop()
        if card.startswith("ace"):
            return card,11
        elif card.startswith("jack"):
            return card,10
        elif card.startswith("queen"):
            return card,10
        elif card.startswith("king"):
            return card,10
        else:
            points = card.split("_")[0]
            return card,int(points)
    
    
    # (2) Driver Program
    crds = []
    pnts = []
    while True:
        if len(deck) != 0:
            card, point = get_points()
            crds.append(card)
            pnts.append(point)
            print(f"card name: {card}, point: {point}")
            print('play again(anykey) or exit (y):')
        if input().lower() == "y" or len(deck) == 0:
            print("-----------------")
            print(f"Total points: {sum(pnts)}")
            print(f"They are: {crds}")
            break


def solution_1_b():
    global price_money
    
    def draw_card():
        card = deck.pop()
        if card.startswith("ace"):
            return 11, card
        elif card.startswith("jack"):
            return 10, card
        elif card.startswith("queen"):
            return 10, card
        elif card.startswith("king"):
            return 10, card
        else:
            points = card.split("_")[0]
            return int(points), card
        
    def get_bet_money(user):
        point1, card1 = draw_card()
        point2, card2 = draw_card()    
        total_points = int(point1) + int(point2)
        show(card1, card2)
        print(f"Total points of {user}: {total_points}")
        return total_points

    while True:
        if len(deck) >= 4 or price_money!=0:
            player_bet = get_bet_money("player")
            dealer_bet = get_bet_money("dealer")

            if player_bet > dealer_bet:
                price_money += player_bet
                print("YOU WON!")
            elif player_bet < dealer_bet:
                price_money -= player_bet
                print("YOU LOST!")
            print(f"Total money left: ${price_money}")
            print('play again(anykey) or exit (y):')
        if input().lower() == "y" or len(deck) < 4 or price_money==0:
            if len(deck) < 4:
                print("YOU RAN OUT OF CARDS TO PLAY")
            if price_money==0:
                print("TOTAL MONEY LEFT: $0")
            print(f"Thank you for Playing")
            break

def solution_1_c():    
    def draw_card():
        card = deck.pop()
        if card.startswith("ace"):
            return 11, card
        elif card.startswith("jack"):
            return 10, card
        elif card.startswith("queen"):
            return 10, card
        elif card.startswith("king"):
            return 10, card
        else:
            points = card.split("_")[0]
            return int(points), card
    
    def show_all_cards(player_cards, player_bet, dealer_cards, dealer_bet):
        show(*player_cards)
        print(f"Total points of player: {player_bet}")
        show(*dealer_cards)
        print(f"Total points of dealer: {dealer_bet}")

    def declare_results(player_bet, dealer_bet):
        global price_money
        if player_bet > dealer_bet:
            price_money += player_bet
            print("YOU WON!")
        elif player_bet < dealer_bet:
            price_money -= player_bet
            print("YOU LOST!")
        else:
            print("ITS A TIE!")

    def get_bet_money(user, num_of_cards, user_points):
        total_points = []
        total_cards = []
        for i in range(num_of_cards):
            point, card = draw_card()
            total_points.append(point)
            total_cards.append(card)
        total_points = user_points + sum(total_points)
        if user == "player":
            show(*total_cards)
            print(f"Total points: {total_points}")
        return total_cards, total_points

    price_money = 1000

    while True:
        if len(deck) >= 4 or price_money!=0:
            player_cards, player_bet = get_bet_money("player", 2, 0)
            dealer_cards, dealer_bet = get_bet_money("dealer", 2, 0)

            chances = 1
            while True:
                if chances >=3:
                    break
                else:
                    print(f"Chance {chances}: 'Hit' or 'Stand'?")
                    choice = input()
                    if choice == "Hit":
                        p_card, player_bet = get_bet_money("player", 1, player_bet)
                        player_cards.append(p_card[0])

                        d_card, dealer_bet = get_bet_money("dealer", 1, dealer_bet)
                        dealer_cards.append(d_card[0])
                        
                        chances+=1
                    elif choice == "Stand" or chances==2:
                        chances+=1
                        pass
                    else:
                        print("Please choose a correct option between 'Hit' or 'Stand'")
                    if player_bet > 21:
                        print("Bust!!!")
                        player_bet = 0
                        print(f"Total points : {player_bet}")
            
            show_all_cards(player_cards, player_bet, dealer_cards, dealer_bet)
            declare_results(player_bet, dealer_bet)
            print(f"Total money left: ${price_money}")
            print('play again(anykey) or exit (y):')
        
        if input().lower() == "y" or len(deck) < 4 or price_money==0:
            if len(deck) < 4:
                print("YOU RAN OUT OF CARDS TO PLAY")
            if price_money==0:
                print("TOTAL MONEY LEFT: $0")
            print(f"Thank you for Playing")
            break