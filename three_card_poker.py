import itertools
import random

class ThreeCardHand:
    hand_types = {
        'ROYAL_FLUSH' : 7,
        'STRAIGHT_FLUSH' : 6,
        'THREE_OF_KIND' : 5,
        'STRAIGHT' : 4,
        'FLUSH' : 3,
        'PAIR' : 2,
        'HIGH_CARD' : 1
    }
    RANK_AS_NUM = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                   'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    def __init__(self):
        self.cards = []
        self.sorted_card_values = []
        self.hand_type = ""
        self.rank = 0

    def add_card(self, card):
        if len(self.cards) < 3:
            if card in self.cards:
                raise ValueError("Duplicate card added to hand")
            store_value = [self.RANK_AS_NUM[card[0:-1]], card[-1]]
            self.cards.append(card)
            self.sorted_card_values.append(self.RANK_AS_NUM[card[0:-1]])
            if len(self.cards) == 3:
                self.sorted_card_values = sorted(self.sorted_card_values)
                self.__calc_score()
        else:
            raise ValueError("Too many cards")

    def is_flush(self):
        return self.cards[0][1] == self.cards[1][1] and self.cards[0][1] == self.cards[2][1]

    def is_straight(self):
        return (self.sorted_card_values[1] - self.sorted_card_values[0] == 1 and
                self.sorted_card_values[2] - self.sorted_card_values[1] == 1)

    def is_pair(self):
        # Don't need to check 0/2 since its in sorted order
        return (self.sorted_card_values[0] == self.sorted_card_values[1] or
                self.sorted_card_values[1] == self.sorted_card_values[2])

    def __calc_score(self):
        # Flush
        if self.is_flush():
            if 'A' in self.sorted_card_values and 'K' in self.sorted_card_values and 'Q' in self.sorted_card_values:
                self.hand_type = 'ROYAL_FLUSH'
                # No extra data for royal flush
            elif self.is_straight():
                self.hand_type = 'STRAIGHT_FLUSH'
                self.rank = self.sorted_card_values[2]
            else:
                self.hand_type = 'FLUSH'
                # Calc so that highest cards compare first
                temp_rank = self.sorted_card_values[2] * 100000
                temp_rank += self.sorted_card_values[1] * 100
                temp_rank += self.sorted_card_values[0]
                self.rank = temp_rank
        elif self.is_straight():
            self.hand_type = 'STRAIGHT'
            # Calc so that highest cards compare first
            temp_rank = self.sorted_card_values[2] * 100000
            temp_rank += self.sorted_card_values[1] * 100
            temp_rank += self.sorted_card_values[0]
            self.rank = temp_rank
        elif self.is_pair():
            if self.sorted_card_values[0] == self.sorted_card_values[2]:
                self.hand_type = 'THREE_OF_KIND'
                self.rank = self.sorted_card_values[0]
            else:
                self.hand_type = 'PAIR'
                if self.sorted_card_values[0] == self.sorted_card_values[1]:
                    self.rank = self.sorted_card_values[0]
                else:
                    self.rank = self.sorted_card_values[2]
        else:
            self.hand_type = 'HIGH_CARD'
            temp_rank = self.sorted_card_values[2] * 100000
            temp_rank += self.sorted_card_values[1] * 100
            temp_rank += self.sorted_card_values[0]
            self.rank = temp_rank

    def __str__(self):
        return str(self.cards) + "," + str(self.hand_type) + "," + str(self.rank)

    def __lt__(self, other):
        if self.hand_types[self.hand_type] < other.hand_types[other.hand_type]:
            return True
        elif self.hand_types[self.hand_type] == other.hand_types[other.hand_type]:
            return self.rank < other.rank
        else:
            return False

    def __gt__(self, other):
        if self.hand_types[self.hand_type] > other.hand_types[other.hand_type]:
            return True
        elif self.hand_types[self.hand_type] == other.hand_types[other.hand_type]:
            return self.rank > other.rank
        else:
            return False

SUITS = ["D", "S", "H", "C"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
def create_deck(option=0):
    if option == 0:
        deck = set()
        for suite in SUITS:
            suite_cards = {f'{rank}{suite}' for rank in RANKS}
            deck.update(suite_cards)
        deck = list(deck)
        random.shuffle(deck)
        return deck
    else:
        deck = []
        for s in SUITS:
            for r in RANKS:
                deck.append(r + s)
        random.shuffle(deck)
        return deck

with open('Output.txt') as file:
    min = -1000000000
    for line in file.readlines():
        profit = int(line.split(',')[0])
        if profit > -600000:
            print(line)
        if profit > min:
            min = profit
print(min)


hand_comp = ThreeCardHand()
hand_comp.add_card("2H")
hand_comp.add_card("6D")
hand_comp.add_card("QS")
no_action_thres = ThreeCardHand()
no_action_thres.add_card("QH")
no_action_thres.add_card("2D")
no_action_thres.add_card("3S")
comps = []
all_ordered = []
for rank in RANKS:
    first = rank + "D"
    for rank2 in RANKS:
        second = rank2 + "H"
        for rank3 in RANKS:
            third = rank3 + "S"
            ordered = sorted([rank, rank2, rank3])
            if ordered not in all_ordered:
                hand_comp = ThreeCardHand()
                hand_comp.add_card(first)
                hand_comp.add_card(second)
                hand_comp.add_card(third)
                if hand_comp.hand_type == 'HIGH_CARD':
                    comps.append(hand_comp)
                    all_ordered.append(ordered)

# for comp in comps:
#     print(comp)
# print(len(comps))
# out = open('Output.txt', 'a')
# iterations = 500000
# ante = 10
# for y in range(len(comps)):
#     hand_comp = comps[y]
#     wins = losses = ties = folds = no_action = 0
#     for x in range(iterations):
#         deck = create_deck(option=1)
#         dealer_cards = ThreeCardHand()
#         player_cards = ThreeCardHand()
#         # deal cards
#         for z in range(3):
#             dealer_cards.add_card(deck.pop())
#             player_cards.add_card(deck.pop())
#         if player_cards < hand_comp:
#             folds += 1
#             continue
#         if dealer_cards < no_action_thres:
#             no_action += 1
#             continue
#         if dealer_cards < player_cards:
#             wins += 1
#         elif player_cards < dealer_cards:
#             losses += 1
#         else:
#             ties += 1
#
#     plays = iterations - folds
#     print(f'Wins: {wins} ({wins / plays})')
#     print(f'Losses: {losses} ({losses / plays})')
#     print(f'Ties: {ties} ({ties / plays})')
#     print(f'Folds: {folds} ({folds / iterations})')
#     print(f'No action: {no_action} ({no_action / plays})')
#     print(f'Profit on hands played: {(wins + no_action) / plays}')
#     print(f'Profit on total hands: {(wins + no_action) / iterations}')
#     cost = (iterations+plays) * 10 - (no_action*10)
#     gross = wins*40 + no_action*20
#     # print(cost)
#     # print(gross)
#     print(f'Cost: {cost}; Gross: {gross}; Profit: {gross - cost}')
#     write_str = f'{gross-cost},({hand_comp}),{wins},{folds},{no_action}\n'
#     out.write(write_str)
#     out.flush()
# out.close()
