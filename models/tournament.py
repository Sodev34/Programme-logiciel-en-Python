from tinydb import TinyDB


class Tournament:
    def __init__(
        self,
        tour_num: int,
        name,
        location,
        start_date,
        end_date,
        actual_round: int,
        players,
        time_control,
        description,
        rounds: int,
        nb_rounds=int(4),
    ):
        self.tour_num = tour_num
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.actual_round = actual_round
        self.players = players
        self.time_control = time_control
        self.description = description
        self.rounds = rounds
        self.nb_rounds = nb_rounds

        self.tournament_db = TinyDB("data_tinydb/tournaments_chess.json")

    def serialized_tournament(self):
        """Renvoi les informations d'un tournoi sérialisé"""
        return {
            "number": self.tour_num,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "actual_round": self.actual_round,
            "players": self.players,
            "time_control": self.time_control,
            "description": self.description,
            "rounds": self.rounds,
            "nb_rounds": self.nb_rounds,
        }

    def sorted_rank(self):
        """Permet d'obtenir le classement des joueurs par classement"""
        self.players = sorted(self.players, key=lambda x: x.get("rank"))

    def sorted_result(self):
        """Permet d'obtenir le classement des joueurs par resultat"""
        self.players = sorted(self.players, key=lambda x: x.get("result"), reverse=True)

    def divide_players(self):
        """Permet de diviser les joueurs en deux groupes (supérieur et inférieur)"""
        half = len(self.players) // 2
        return self.players[:half], self.players[half:]

    def assemble_players(self, upper_players, lower_players):
        """Permet fusionner les meilleurs et les derniers joueurs"""
        assembled_players = []
        for i in range(len(self.players) // 2):
            assembled_players.append(upper_players[i])
            assembled_players.append(lower_players[i])

        self.players = assembled_players

    def add_tournament_db(self):
        """Enregistre un nouveau tournoi dans la base de données"""
        db = self.tournament_db
        self.tour_num = db.insert(self.serialized_tournament())
        db.update({"number": self.tour_num}, doc_ids=[self.tour_num])

    def update_tournament_db(self):
        """Permet de mettre à jour un tournoi"""
        db = self.tournament_db
        db.update({"players": self.players}, doc_ids=[self.tour_num])
        db.update({"rounds": self.rounds}, doc_ids=[self.tour_num])
        db.update({"actual_round": self.actual_round}, doc_ids=[self.tour_num])

    def update_tournament_time_db(self, time, information):
        """Permet de mettre à jour le début et la fin d'un tournoi"""
        db = self.tournament_db
        db.update({information: time}, doc_ids=[self.tour_num])

    def load_tournament_db():
        """Télécharge les tournois de la base de données"""
        db = TinyDB("data_tinydb/tournaments_chess.json")
        db.all()
        tour_list = []
        for line in db:
            tour_list.append(line)

        return tour_list
