from player import Player

# Some sample code that uses the Player class.
p1 = Player('Candy', 50)
p2 = Player('Ferb', 250)
p3 = Player('Phineas', 150)

ls = [p1, p2, p3]
best = Player.best_score(ls)
msg = '{} has the best score, with {} points!'.format(best.name, best.score)
print(msg) # Ferb has the best score, with 25 points!
