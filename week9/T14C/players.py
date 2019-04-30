import player
p4 = player.Player('Brett', 500)
p5 = player.Player('Nancy', 2050)
p6 = player.Player('Phillip', 1150)
# this is a private variable, shouldn't be changed
#p4._score = 4 # bad!
ls = [p4, p5, p6]
best = player.Player.best_score(ls)
msg = "{} has the best score, with {} points!".format(best.name(), best.score())
print(msg)
