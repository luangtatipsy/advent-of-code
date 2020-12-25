from collections import deque


class Player:
    def __init__(self, deck):
        self.deck = deque(deck)

    def draw(self):
        return self.deck.popleft()

    def collect(self, cards):
        self.deck.extend(cards)


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.winner = None

    def start(self):
        _round = 1

        while len(self.p1.deck) > 0 and len(self.p2.deck) > 0:
            self.winner = self.play()

            _round += 1

        return self.winner

    def play(self):
        winner = None
        p1_card = self.p1.draw()
        p2_card = self.p2.draw()

        if p1_card > p2_card:
            self.p1.collect([p1_card, p2_card])
            winner = self.p1

        elif p1_card < p2_card:
            self.p2.collect([p2_card, p1_card])
            winner = self.p2

        return winner


def main(p1_deck, p2_deck):
    p1 = Player(p1_deck)
    p2 = Player(p2_deck)
    game = Game(p1, p2)

    winner = game.start()

    score = 0
    for card, order in zip(winner.deck, range(len(winner.deck), 0, -1)):
        score += card * order

    return score


if __name__ == "__main__":
    with open("input.txt") as f:
        p1_deck, p2_deck = [
            [int(card) for card in deck.splitlines() if card.strip().isdigit()]
            for deck in f.read().split("\n\n")
        ]

    score = main(p1_deck, p2_deck)
    print(score)
