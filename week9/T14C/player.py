class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # this is a getter function
    def score(self):
        return self.score

    def best_score(players):
        best = players[0]
        i = 1
        while i < len(players):
            if players[i].score() > best.score():
                best = players[i]
        return best

if __name__ == "__main__":
    p1 = Player('Candy', 50)
    p2 = Player('Ferb', 250)
    p3 = Player('Phineas', 150)
    ls = [p1, p2, p3]
    best = Player.best_score(ls)
    msg = "{} has the best score, with {} points!".format(best.name, best.score())
    print(msg)
