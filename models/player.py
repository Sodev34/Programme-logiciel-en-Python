from tinydb import TinyDB


class Player:
    def __init__(self, player_id: int, last_name, first_name, date_of_birth, gender, rank: int):
        self.player_id = player_id
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.rank = rank
        self.result = 0
        self.challengers = []

        self.player_db = TinyDB("database/players_chess.json")

    def serialized_player(self):
        """Renvoi les informations d'un joueur sérialisé"""
        return {
            "player_id": self.player_id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "rank": self.rank,
            "result": self.result,
            "challengers": self.challengers,
        }

    def add_player_db(self):
        """Enregistre un nouveau joueur dans la base de données"""
        players_db = self.player_db
        self.player_id = players_db.insert(self.serialized_player())
        players_db.update({"player_id": self.player_id}, doc_ids=[self.player_id])

    def update_player_db(self, information, option):
        """Permet de mettre à jour un joueur"""
        db = self.player_db
        db.update({option: information}, doc_ids=[self.player_id])

    def load_player_db():
        """Télécharge les joueurs de la base de données"""
        players_db = TinyDB("database/players_chess.json")
        players_db.all()
        players = []
        for line in players_db:
            players.append(line)

        return players
