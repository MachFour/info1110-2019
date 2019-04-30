import player
p4 = player.Player('Brett', 500)
p5 = player.Player('Nancy', 2050)
p6 = player.Player('Phillip', 1150)
ls = [p4, p5, p6]
best = player.Player.best_score(ls)
msg = "{} has the best score, with {} points!".format(best.name, best.score())
print(msg)
