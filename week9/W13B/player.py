class Player:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def best_score(players):
        """
        param: players - list of Player objects
        """
        best_player = players[0]
        # Assume first player to be best player

        i = 0
        while i < len(players):
            player = players[i]
            if player.score > best_player.score:
                best_player = player

            i+=1

        return best_player

