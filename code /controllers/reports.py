from models.tournament import Tournament
from views.menu import MenuViews
from views.reports import Reports


class ReportsController:
    def __init__(self):
        self.menu_view = MenuViews()
        self.reports_view = Reports()

    def all_players_name(self, players):
        players = sorted(players, key=lambda x: x.get("last_name"))
        self.reports_view.display_players(players, "par nom")

    def all_players_rank(self, players):
        players = sorted(players, key=lambda x: x.get("rank"))
        self.reports_view.display_players(players, "par classement")

    def tournament_players(self):

        user_input, tournaments = self.tournament_select()

        for i in range(len(tournaments)):
            if user_input == str(tournaments[i]["number"]):
                return tournaments[i]["players"]

    def all_tournaments(self):
        self.reports_view.display_tournaments_report(Tournament.load_tournament_db())

    def tournament_rounds(self):
        user_input, tournaments = self.tournament_select()

        self.reports_view.report_header(tournaments[int(user_input) - 1])
        self.reports_view.display_rounds_report(tournaments[int(user_input) - 1]["rounds"])

    def tournament_matches(self):
        user_input, tournaments = self.tournament_select()

        self.reports_view.report_header(tournaments[int(user_input) - 1])

        rounds = tournaments[int(user_input) - 1]["rounds"]
        round_matches = []
        for i in range(len(rounds)):
            round_matches.append(rounds[i][3])

        matches = []
        for i in range(len(round_matches)):
            for g in range(4):
                matches.append(round_matches[i][g])

        self.reports_view.display_matches_report(matches)

    def tournament_select(self):
        tournaments = Tournament.load_tournament_db()
        self.menu_view.choose_tournament(tournaments)
        self.menu_view.option_main()
        user_input = input()

        if user_input == "retour":
            self.back()

        else:
            return user_input, tournaments

    @staticmethod
    def back():
        from controllers.menu import MenuController

        MenuController().menu_start()
