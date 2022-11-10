from datetime import datetime
from models.player import Player
from models.round import Round
from views.round import RoundViews
from views.menu import MenuViews


class TournamentController:
    def __init__(self):
        self.menu_view = MenuViews()
        self.round_view = RoundViews()

        self.timer = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def start_tournament(self, tour):
        """Permet de commencer ou de reprendre un tournoi avec la mise à jour du début
        et de la fin du tournoi dans la base de données"""

        if tour.actual_round == 1:
            tour.start_date = self.timer
            tour.update_tournament_time_db(tour.start_date, "start_date")

            self.first_round(tour)
            tour.actual_round += 1
            tour.update_tournament_db()

            while tour.actual_round <= tour.nb_rounds:
                self.next_rounds(tour)
                tour.actual_round += 1
                tour.update_tournament_db()

            tour.end_date = self.timer
            tour.update_tournament_time_db(tour.end_date, "end_date")
            self.tournament_end(tour)

        elif 1 < tour.actual_round <= tour.nb_rounds:
            while tour.actual_round <= tour.nb_rounds:
                self.next_rounds(tour)
                tour.actual_round += 1
                tour.update_tournament_db()

            tour.end_date = self.timer
            tour.update_tournament_time_db(tour.end_date, "end_date")
            self.tournament_end(tour)

        elif tour.actual_round > tour.nb_rounds:
            self.tournament_end(tour)

    def first_round(self, tour):
        """Permet de définir le premier tour avec le choix
        des joueurs (les meilleurs et les derniers joueurs) et d'enregistrer
        le tour dans la base de donnés"""
        r = Round("Tour 1", self.timer, "en attente")
        tour.sorted_rank()
        upper_players, lower_players = tour.divide_players()
        self.round_view.round_header(tour, r.round_start)

        for i in range(tour.nb_rounds):
            r.pair_of_players(upper_players[i], lower_players[i])
            upper_players[i], lower_players[i] = self.update_challengers(upper_players[i], lower_players[i])

        self.round_view.display_matches(r.matches)

        self.round_view.extra_round()
        self.menu_view.option_main()
        user_input = input()

        results_list = []

        if user_input == "oui":
            r.round_end = self.timer
            tour.rounds.append(r.list_round())
            tour.assemble_players(upper_players, lower_players)

            self.end_of_round(results_list, tour, r.matches)

        elif user_input == "retour":
            self.back()

    def next_rounds(self, tour):
        """Permet de définir les tours suivant avec le choix
        des joueurs (en fonction des options) et d'enregistrer
        les tours dans la base de données"""
        r = Round(("Tour " + str(tour.actual_round)), self.timer, "en attente")
        tour.sorted_result()
        self.round_view.round_header(tour, r.round_start)

        usable_list = tour.players
        players_added = []

        e = 0
        while e < tour.nb_rounds:
            if usable_list[1]["player_id"] in usable_list[0]["challengers"]:
                try:
                    usable_list, players_added = self.match_next_option(usable_list, players_added, r)
                    tour.players = players_added

                except IndexError:
                    usable_list, players_added = self.match_option(usable_list, players_added, r)
                    tour.players = players_added

            elif usable_list[1]["player_id"] not in usable_list[0]["challengers"]:
                usable_list, players_added = self.match_option(usable_list, players_added, r)
                tour.players = players_added

            e += 1

        self.round_view.display_matches(r.matches)

        self.round_view.extra_round()
        self.menu_view.option_main()
        user_input = input()
        results_list = []

        if user_input == "oui":
            r.round_end = self.timer
            tour.rounds.append(r.list_round())
            self.end_of_round(results_list, tour, r.matches)

        elif user_input == "retour":
            self.back()

    def match_option(self, usable_list, players_added, r):
        """Permet de définir la composition des matchs avec
        les joueurs disponibles (usable_list) et les joueurs en cours de match
        (players_added)"""

        r.pair_of_players(usable_list[0], usable_list[1])
        usable_list[0], usable_list[1] = self.update_challengers(usable_list[0], usable_list[1])

        usable_list, players_added = self.update_player_lists(
            usable_list[0], usable_list[1], usable_list, players_added
        )

        return usable_list, players_added

    def match_next_option(self, usable_list, players_added, r):
        """Permet d'obtenir une option alternative pour la composition des matchs avec
        les joueurs disponibles (usable_list) et les joueurs en cours de match
        (players_added)"""
        r.pair_of_players(usable_list[0], usable_list[2])
        usable_list[0], usable_list[2] = self.update_challengers(usable_list[0], usable_list[2])

        usable_list, players_added = self.update_player_lists(
            usable_list[0], usable_list[2], usable_list, players_added
        )

        return usable_list, players_added

    def end_of_round(self, results_list: list, tour, matches):
        """Permet d'afficher et de mettre à jour les resultats des
        joueurs à la fin du tour dans la base de données"""
        for i in range(tour.nb_rounds):
            self.round_view.result_options(i + 1, matches[i])
            response = self.input_results()
            results_list = self.get_result(response, results_list)

        tour.players = self.update_results(tour.players, results_list)

        return tour.players

    def input_results(self):
        """Permet de saisir les résultats"""
        self.round_view.result_input()
        response = input()
        return response

    def get_result(self, response, results_list: list):
        """Permet d'enregistrer les résultats dans la
        liste des résultats"""
        if response == "0":
            results_list.extend([0.5, 0.5])
            return results_list
        elif response == "1":
            results_list.extend([1.0, 0.0])
            return results_list
        elif response == "2":
            results_list.extend([0.0, 1.0])
            return results_list
        elif response == "retour":
            self.back()
        else:
            self.menu_view.input_error()
            self.input_results()

    @staticmethod
    def update_results(players, results_list: list):
        """Permet de mettre à jour les résultats des joueurs"""
        for i in range(len(players)):
            players[i]["result"] += results_list[i]

        return players

    @staticmethod
    def update_player_lists(player_one, player_two, usable_list, players_added):
        """Permet de mettre à jour les joueurs dans les différentes catégories
        de liste de joueurs"""
        players_added.extend([player_one, player_two])
        usable_list.remove(player_one)
        usable_list.remove(player_two)

        return usable_list, players_added

    @staticmethod
    def update_challengers(player_one, player_two):
        player_one["challengers"].append(player_two["player_id"])
        player_two["challengers"].append(player_one["player_id"])

        return player_one, player_two

    def tournament_end(self, tour):
        """Permet d'afficher et de mettre à jour les résultats des joueurs à
        la fin du tournoi avec la possibilité de mettre à jour
        le classement dans la base de données"""

        tour.sorted_rank()
        tour.sorted_result()

        self.round_view.display_results(tour)

        self.menu_view.update_rank()
        user_input = input()

        players = tour.players

        if user_input == "n":
            self.back()

        elif user_input == "o":
            while True:
                self.update_ranks(players)

    def update_ranks(self, players):
        """Permet de mettre à jour le classement dans la base de données"""
        self.menu_view.choose_players(players, " ")
        self.menu_view.option_main()
        user_input = input()

        if user_input == "retour":
            self.back()

        for i in range(len(players)):
            if int(user_input) == players[i]["player_id"]:
                p = players[players.index(players[i])]
                p = Player(p["player_id"], p["last_name"], p["first_name"], p["date_of_birth"], p["gender"], p["rank"])

                self.menu_view.rank_update(p)
                self.menu_view.input_option("nouveau classement")
                user_input = input()

                if user_input == "retour":
                    self.back()

                else:
                    p.update_player_db(int(user_input), "rank")
                    players[i]["rank"] = int(user_input)

                    return players

    @staticmethod
    def back():
        from controllers.menu import MenuController

        MenuController().menu_start()
