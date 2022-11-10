class Round:
    def __init__(self, round_name, round_start, round_end):
        self.round_name = round_name
        self.round_start = round_start
        self.round_end = round_end
        self.matches = []

    def list_round(self):
        """Renvoi les informations des tours"""
        return [self.round_name, self.round_start, self.round_end, self.matches]

    def pair_of_players(self, player_one, player_two):
        """Permet d'obtenir les joueurs d'un match"""
        match = (
            f"{player_one['last_name']}, {player_one['first_name']}",
            player_one["result"],
            f"{player_two['last_name']}, {player_two['first_name']}",
            player_two["result"],
        )

        self.matches.append(match)
