from controllers.reports import ReportsController
from controllers.tournament import TournamentController
from models.player import Player
from models.tournament import Tournament
from views.menu import MenuViews


class MenuController:
    def __init__(self):
        self.menu_view = MenuViews()
        self.tournament_controller = TournamentController()
        self.reports_controller = ReportsController()

    def menu_start(self):
        self.menu_view.main_menu()
        self.menu_view.option_main()
        user_input = input()

        if user_input == "1":
            self.new_tournament()

        elif user_input == "2":
            self.continue_tournament()

        elif user_input == "3":
            self.new_player()

        elif user_input == "4":
            self.player_reports_sorted(Player.load_player_db())

        elif user_input == "5":
            self.reports_menu()

        elif user_input == "6":
            self.menu_view.go_out()
            user_input = input()

            if user_input == "o":
                quit()
            elif user_input == "n":
                self.menu_start()

        else:
            self.menu_view.input_error()
            self.menu_start()

    def new_tournament(self):
        self.menu_view.show_new_tournament()
        tournament_information = []
        options = [
            "nom",
            "localisation",
            "description",
            "nombre de joueurs (8 joueurs par défaut)",
            "nombre de tours (4 tours par défaut)",
        ]

        for data in options:
            self.menu_view.input_option(data)
            user_input = input()

            if user_input == "retour":
                self.menu_start()

            else:
                tournament_information.append(user_input)

        tournament_information.append(self.input_time_control())
        tournament_players = self.choose_players(int(tournament_information[3] or 8))

        self.menu_view.tournament_validation(tournament_information, tournament_players)
        user_input = input()

        if user_input == "o":
            tournament = Tournament(
                tour_num=0,
                name=tournament_information[0],
                location=tournament_information[1],
                start_date="en attente",
                end_date="en attente",
                description=tournament_information[2],
                time_control=tournament_information[5],
                players=tournament_players,
                actual_round=int(1),
                rounds=[],
                nb_rounds=int(tournament_information[4] or 4),
            )
            tournament.add_tournament_db()
            self.menu_view.tournament_registration()

            self.menu_view.start_tournament()
            user_input = input()

            if user_input == "o":
                self.tournament_controller.start_tournament(tournament)
            elif user_input == "n":
                self.menu_start()

        elif user_input == "n":
            self.menu_start

    def input_time_control(self):
        self.menu_view.show_time_control()
        self.menu_view.option_main()
        user_input = input()

        if user_input == "1":
            return " Bullet"
        elif user_input == "2":
            return "Blitz"
        elif user_input == "3":
            return "Rapid"
        elif user_input == "retour":
            self.menu_start()
        else:
            self.menu_view.input_error()
            self.input_time_control()

    def choose_players(self, players_total):
        players = Player.load_player_db()
        players_id_list = []
        for i in range(len(players)):
            players_id_list.append(players[i]["player_id"])

        tournament_players = []

        i = 0

        while i < players_total:
            self.menu_view.choose_players(players, i + 1)
            self.menu_view.option_main()
            user_input = input()

            if user_input == "retour":
                self.menu_view.menu_start()

            elif not user_input.isdigit():
                self.menu_view.input_error()

            elif int(user_input) in players_id_list:
                index = players_id_list.index(int(user_input))
                tournament_players.append(players[index])
                players_id_list.remove(players_id_list[index])
                players.remove(players[index])
                i += 1

            else:
                self.menu_view.player_selected()

        return tournament_players

    def continue_tournament(self):
        tournament_list = Tournament.load_tournament_db()

        self.menu_view.choose_tournament(tournament_list)
        self.menu_view.option_main()
        user_input = input()

        if user_input == "retour":
            self.menu_start()

        for i in range(len(tournament_list)):
            if user_input == str(tournament_list[i]["number"]):
                tournament = tournament_list[i]
                tournament = Tournament(
                    tournament["number"],
                    tournament["name"],
                    tournament["location"],
                    tournament["start_date"],
                    tournament["end_date"],
                    tournament["actual_round"],
                    tournament["players"],
                    tournament["time_control"],
                    tournament["description"],
                    tournament["rounds"],
                    tournament["nb_rounds"],
                )
                self.tournament_controller.start_tournament(tournament)

    def new_player(self):
        self.menu_view.show_new_player()
        player_information = []
        options = ["nom", "prénom", "date de naissance (jj.mm.aaaa)", "sexe [M/F]", "classement"]
        for data in options:
            self.menu_view.input_option(data)
            user_input = input()
            if user_input == "retour":
                self.menu_start()
            else:
                player_information.append(user_input)

        MenuViews.player_validation(player_information)
        user_input = input()

        if user_input == "o":
            player = Player(
                player_id=0,
                last_name=player_information[0],
                first_name=player_information[1],
                date_of_birth=player_information[2],
                gender=player_information[3],
                rank=int(player_information[4]),
            )
            player.add_player_db()
            self.menu_view.player_registration()
            self.menu_start()

        elif user_input == "n":
            self.menu_start()

    def reports_menu(self):

        self.menu_view.show_reports()
        self.menu_view.option_main()
        user_input = input()

        if user_input == "1":
            self.player_reports_sorted(self.reports_controller.tournament_players())

        elif user_input == "2":
            self.reports_controller.all_tournaments()

        elif user_input == "3":
            self.reports_controller.tournament_rounds()

        elif user_input == "4":
            self.reports_controller.tournament_matches()

        elif user_input == "retour":
            self.menu_start()

        else:
            self.menu_view.input_error()
            self.reports_menu()

        self.menu_view.other_report()
        user_input = input()

        if user_input == "o":
            self.reports_menu()

        elif user_input == "n":
            self.menu_start()

    def player_reports_sorted(self, players):
        self.menu_view.show_reports_player()
        self.menu_view.option_main()
        user_input = input()

        if user_input == "1":
            self.reports_controller.all_players_name(players)
            self.menu_view.option_main()
            user_input = input()

            if user_input == "retour":
                self.menu_start()

        elif user_input == "2":
            self.reports_controller.all_players_rank(players)
            self.menu_view.option_main()
            user_input = input()

            if user_input == "retour":
                self.menu_start()

        elif user_input == "3":
            self.tournament_controller.update_ranks(players)
            self.menu_start()

        elif user_input == "retour":
            self.menu_start()
