from controllers.reports import ReportsController
from controllers.tournament import TournamentController
from models.match import Match
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
            self.reports_menu()

        elif user_input == "5":
            self.menu_view.are_you_exit()
            user_input = input()

            if user_input == "o":
                exit()
            elif user_input == "n":
                self.menu_start()

        else:
            self.menu_view.input_error()
            self.menu_start()

    def new_tournament(self):
        self.menu_view.show_new_tournament()
        tournament_information = []
        options = ["nom", "localisation", "description"]

        for data in options:
            self.menu_view.input_option(data)
            user_input = input()

            if user_input == "retour":
                self.menu_start()

            else:
                tournament_information.append(user_input)

        tournament_information.append(self.input_time_control())
        tournament_players = self.choose_players(8)

        self.menu_view.tournament_validation(tournament_information, tournament_players)
        user_input = input()

        if user_input == "o":
            tournament = Tournament(
                tour_num=0,
                name=tournament_information[0],
                location=tournament_information[1],
                start_date="En attente",
                end_date="TBD",
                description=tournament_information[2],
                time_control=tournament_information[3],
                players=tournament_players,
                rounds=1,
                rounds_stock=[],
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
            self.menu_view.menu_start()

        for i in range(len(tournament_list)):
            if user_input == str(tournament_list[i]["number"]):
                tournament = tournament_list[i]
                tournament = Tournament(
                    tournament["number"],
                    tournament["name"],
                    tournament["location"],
                    tournament["start_date"],
                    tournament["end_date"],
                    tournament["description"],
                    tournament["time_control"],
                    tournament["rounds"],
                    tournament["players"],
                    tournament["rounds_stock"],
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
                rank=player_information[4],
            )
            player.add_player_db()
            self.menu_view.player_registration()
            self.menu_start()

            #  def update_player(self):

            #     players = Player.load_player_db()

            #    self.menu_view.choose_players(players, "par son numéro")
            #   self.menu_view.option_main()
            #  user_input = input()

            #   if user_input == "retour":
        #  self.menu_start()

    #   player = players[int(user_input) - 1]
    #   player = Player(
    #      player["player_id"],
    #     player["last_name"],
    #     player["first_name"],
    #        player["date_of_birth"],
    #        player["gender"],
    #        player["rank"],
    #    )

    #    options = ["du nom", "du prénom", "de la date de naissance", "du sexe", "du classement"]

    #    self.menu_view.update_player_information(player, options)
    #    self.menu_view.option_main()
    #    user_input = input()

    #    if user_input == "retour":
    #        self.menu_start()

    #    elif int(user_input) <= len(options):
    #        update_information = options[int(user_input) - 1]  # .replace(" ", "_")
    #        self.menu_view.input_option(f"modification {options[int(user_input)  - 1]}")
    #        user_input = input()

    #        if user_input == "retour":
    #            self.menu_start()

    #       else:
    #            player.update_player_db(user_input, update_information)
    #           self.menu_view.player_registration()

    #            self.update_player()

    #    else:
    #        self.menu_view.input_error()
    #        self.update_player()

    def reports_menu(self):

        self.menu_view.show_reports()
        self.menu_view.option_main()
        user_input = input()

        if user_input == "1":
            self.show_reports_player(Player.load_player_db)

        elif user_input == "2":
            self.show_reports_player(self.reports_controller.tournament_players())

        elif user_input == "3":
            self.reports_controller.all_tournaments()

        elif user_input == "4":
            self.reports_controller.tournament_rounds()

        elif user_input == "5":
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

        elif user_input == "2":
            self.reports_controller.all_players_rank(players)

        elif user_input == "retour":
            self.menu_start()
