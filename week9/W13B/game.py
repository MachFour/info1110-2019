from player import Player

p1 = Player('Candy', 50)
p2 = Player('Phineas', 250)
p3 = Player('Ferb', 150)

ls = [p1, p2, p3]

best = Player.best_score(ls)

print(best.name, best.score)

