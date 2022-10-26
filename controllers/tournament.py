from datetime import datetime

from models.player import Player
from models.round import Round
from models.match import Match
from views.round import RoundViews
from views.menu import MenuViews


class TournamentController:
    def __init__(self):
        self.menu_view = MenuViews()
        self.round_view = RoundViews()

        self.timer = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def start_tournament(self, tour):

        if tour.rounds == 1:
            tour.start_date = self.timer
            tour.update_tournament_time_db(tour.start_date, "start_date")

            self.first_round(tour)
            tour.rounds += 1
            tour.update_tournament_db()

            while tour.rounds <= tour.nb_rounds:
                self.next_rounds(tour)
                tour.rounds += 1
                tour.update_tournament_db()

        elif 1 < tour.rounds <= tour.nb_rounds:
            while tour.rounds <= tour.nb_rounds:
                self.next_rounds(tour)
                tour.rounds += 1
                tour.update_tournament_db()

            tour.end_date = self.timer
            tour.update_tournament_time_db(tour.end_date, "end_date")
            self.tournament_end(tour)

        elif tour.rounds > tour.nb_rounds:
            self.tournament_end(tour)

    def first_round(self, tour):
        r = Round("Round 1", self.timer, "TBD")
        tour.sorted_rank()
        upper_players, lower_players = tour.divide_players()
        self.round_view.round_header(tour, r.round_start)

        for i in range(tour.nb_rounds):
            r.pair_of_players(upper_players[i], lower_players[i])
            upper_players[i], lower_players[i] = self.update_challengers(upper_players[i], lower_players[i])

        self.round_view.display_matches(r.matches)
        self.menu_view.option_main()
        user_input = input()
        scores_list = []

        if user_input == "ok":
            r.round_end = self.timer
            tour.rounds.append(r.set_round())
            tour.assemble_players(upper_players, lower_players)

            self.end_of_round(scores_list, tour)

        elif user_input == "back":
            self.back_to_menu()

    def next_rounds(self, tour):
        r = Round(("Round " + str(tour.rounds)), self.timer, "TBD")
        tour.sorted_result()
        self.round_view.round_header(tour, r.round_start)

        available_list = tour.players
        players_added = []

        e = 0
        while e < tour.nb_rounds:
            if available_list[1]["player_id"] in available_list[0]["challengers"]:
                try:
                    available_list, players_added = self.match_next_option(available_list, players_added, r)
                    tour.players = players_added

                except IndexError:
                    available_list, players_added = self.match_option(available_list, players_added, r)
                    tour.players = players_added

            elif available_list[1]["player_id"] not in available_list[0]["challengers"]:
                available_list, players_added = self.match_option(available_list, players_added, r)
                tour.players = players_added

            e += 1

        self.round_view.display_matches(r.matches)

        self.round_view.extra_round()
        self.menu_view.option_main()
        user_input = input()
        scores_list = []

        if user_input == "ok":
            r.round_end = self.timer
            tour.rounds.append(r.set_round())
            self.end_of_round(scores_list, tour)

        elif user_input == "back":
            self.back_to_menu()

    def match_option(self, available_list, players_added, r):

        r.pair_of_players(available_list[0], available_list[1])
        available_list[0], available_list[1] = self.update_challengers(available_list[0], available_list[1])

        available_list, players_added = self.update_player_lists(
            available_list[0], available_list[1], available_list, players_added
        )

        return available_list, players_added

    def match_next_option(self, available_list, players_added, r):
        r.pair_of_players(available_list[0], available_list[2])
        available_list[0], available_list[2] = self.update_challengers(available_list[0], available_list[2])

        available_list, players_added = self.update_player_lists(
            available_list[0], available_list[2], available_list, players_added
        )

        return available_list, players_added

    def end_of_round(self, scores_list: list, tour):
        for i in range(tour.nb_rounds):
            self.round_view.score_options(i + 1)
            response = self.input_scores()
            scores_list = self.get_score(response, scores_list)

        tour.players = self.update_scores(tour.players, scores_list)

        return tour.players

    def input_scores(self):
        self.round_view.score_input()
        response = input()
        return response

    def get_score(self, response, scores_list: list):
        if response == "0":
            scores_list.extend([0.5, 0.5])
            return scores_list
        elif response == "1":
            scores_list.extend([1.0, 0.0])
            return scores_list
        elif response == "2":
            scores_list.extend([0.0, 1.0])
            return scores_list
        elif response == "back":
            self.back_to_menu()
        else:
            self.menu_view.input_error()
            self.input_scores()

    def update_scores(players, scores_list: list):
        for i in range(len(players)):
            players[i]["score"] += scores_list[i]

        return players

    def update_player_lists(player_1, player_2, available_list, players_added):
        players_added.extend([player_1, player_2])
        available_list.remove(player_1)
        available_list.remove(player_2)

        return available_list, players_added

    def update_challengers(player_1, player_2):
        player_1["challengers"].append(player_2["player_id"])
        player_2["challengers"].append(player_1["player_id"])

        return player_1, player_2

    def tournament_end(self, tour):
        tour.sorted_rank()
        tour.sorted_result()

        self.round_view.display_results(tour)

        self.menu_view.update_rank()
        user_input = input()

        players = tour.players

        if user_input == "n":
            self.back_to_menu()

        elif user_input == "y":
            while True:
                self.update_ranks(players)

    def update_ranks(self, players):
        self.menu_view.select_players(players, "to update")
        self.menu_view.option_main()
        user_input = input()

        if user_input == "back":
            self.back_to_menu()

        for i in range(len(players)):
            if int(user_input) == players[i]["player_id"]:
                p = players[players.index(players[i])]
                p = Player(p["player_id"], p["last_name"], p["first_name"], p["date_of_birth"], p["gender"], p["rank"])

                self.menu_view.rank_update_header(p)
                self.menu_view.input_option("new rank")
                user_input = input()

                if user_input == "back":
                    self.back_to_menu()

                else:
                    p.update_player_db(int(user_input), "rank")
                    players[i]["rank"] = int(user_input)

                    return players

    def back_to_menu():
        from chess.controllers.menu import MenuController

        MenuController().main_menu_start()
