class Player:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def best_score(players):
        """
        This is a class method
        """
        best_player = players[0]
        i = 0
        while i < len(players):
            if players[i].score > best_player.score:
                best_player = players[i]

            i += 1

        return best_player


