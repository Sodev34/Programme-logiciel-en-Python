from tinydb import TinyDB


class Tournament:
    def __init__(
        self,
        tour_num,
        name,
        location,
        start_date,
        end_date,
        rounds: int,
        players,
        time_control,
        description,
        rounds_stock: int,
        nb_rounds=4,
    ):
        self.tour_num = tour_num
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.players = players
        self.time_control = time_control
        self.description = description
        self.rounds_stock = rounds_stock
        self.nb_rounds = nb_rounds

        self.tournament_db = TinyDB("database/tournaments_chess.json")

    def serialized_tournament(self):
        return {
            "number": self.tour_num,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "rounds": self.rounds,
            "players": self.players,
            "time_control": self.time_control,
            "description": self.description,
            "rounds_stock": self.rounds_stock,
            "nb_rounds": self.nb_rounds,
        }

    def sorted_rank(self):
        self.players = sorted(self.players, key=lambda x: x.get("rank"))
        return self.players

    def sorted_result(self):
        self.players = sorted(self.players, key=lambda x: x.get("result"), reverse=True)

    def divide_players(self):
        half = len(self.players) // 2
        return self.players[:half], self.players[half:]

    def assemble_players(self, upper_players, lower_players):
        assembled_players = []
        for i in range(len(self.players) // 2):
            assembled_players.append(upper_players[i])
            assembled_players.append(lower_players[i])

        self.players = assembled_players

    def add_tournament_db(self):
        db = self.tournament_db
        self.tour_num = db.insert(self.serialized_tournament())
        db.update({"number": self.tour_num}, doc_ids=[self.tour_num])

    def update_tournament_db(self):
        db = self.tournament_db
        db.update({"players": self.players}, doc_ids=[self.tour_num])
        db.update({"rounds": self.rounds}, doc_ids=[self.tour_num])
        db.update({"rounds_stock": self.rounds_stock}, doc_ids=[self.tour_num])

    def update_tournament_time_db(self, time, start_date, end_date):
        db = self.tournament_db
        db.update({start_date: time}, doc_ids=[self.tour_num])
        db.update({end_date: time}, doc_ids=[self.tour_num])

    def load_tournament_db():
        db = TinyDB("database/tournaments_chess.json")
        db.all()
        tour_list = []
        for line in db:
            tour_list.append(line)

        return tour_list
