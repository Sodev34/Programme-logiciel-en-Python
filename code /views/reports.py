from prettytable import PrettyTable


class Reports:
    def __init__(self):

        self.table = PrettyTable()

        self.player_report_field = ["Nom", "Prénom", "Sexe", "Date de naissance", "Classement"]

        self.tournament_report_field = [
            "numéro",
            "Nom",
            "Lieu",
            "Description",
            "Début",
            "Fin",
            "Cadence",
            "Tour",
        ]

        self.matches_report_field = [
            "Joueur 1",
            "Score Joueur 1",
            " ",
            "Joueur 2",
            "Score Joueur 2",
        ]

        self.rounds_report_field = ["Tour ", "Début", "Fin", "Matchs"]

    def display_players(self, players, order):
        """Permet d'afficher le rapport de la liste des joueurs"""
        self.table.clear()
        self.table.field_names = self.player_report_field
        self.table.align = "l"

        for i in range(len(players)):
            self.table.add_row(
                [
                    players[i]["last_name"],
                    players[i]["first_name"],
                    players[i]["gender"],
                    players[i]["date_of_birth"],
                    players[i]["rank"],
                ]
            )

        print(f"\n\n             - Liste des joueurs ({order}) -\n")
        print(self.table)
        print("\n[retour] Retour au menu principal\n")

    def display_tournaments_report(self, tournaments):
        """Permet d'afficher le rapport de la liste des tournois"""
        self.table.clear()
        self.table.field_names = self.tournament_report_field
        self.table.align = "l"

        for i in range(len(tournaments)):

            self.table.add_row(
                [
                    tournaments[i]["number"],
                    tournaments[i]["name"],
                    tournaments[i]["location"],
                    tournaments[i]["description"],
                    tournaments[i]["start_date"],
                    tournaments[i]["end_date"],
                    tournaments[i]["time_control"],
                    str(tournaments[i]["actual_round"] - 1) + "/" + str(tournaments[i]["nb_rounds"]),
                ]
            )
        print("\n")
        print(("-------- Liste des tournois --------\n").center(100, " "))
        print(self.table)

    def display_matches_report(self, matches):
        """Permet d'afficher le rapport de la liste des matchs"""
        self.table.clear()
        self.table.field_names = self.matches_report_field
        self.table.align = "l"

        for i in range(len(matches)):
            matches[i].insert(2, "vs.")
            self.table.add_row(matches[i])

        print("\n")
        print((f" -------- {len(matches)} matchs joués au total --------\n").center(75, " "))
        print(self.table)

    def display_rounds_report(self, rounds):
        """Permet d'afficher le rapport de la liste des tours"""
        self.table.clear()
        self.table.field_names = self.rounds_report_field
        self.table.align = "l"

        for i in range(len(rounds)):
            for g in range(4):
                if g == 0:
                    self.table.add_row([rounds[i][0], rounds[i][1], rounds[i][2], rounds[i][3][g]])
                else:
                    self.table.add_row([" ", " ", " ", rounds[i][3][g]])

        print("\n")
        print(("-------- Liste des tours joués --------\n").center(100, " "))
        print(self.table)

    @staticmethod
    def report_header(information):
        """Permet d'afficher les informations du tournoi concerné par le rapport"""
        print("\n\n")
        print(f"{information['name']}, {information['location']} - Description : {information['description']}")
        print(
            f"Début : {information['start_date']} | "
            f"Fin : {information['end_date']} | "
            f"Controle du temps : {information['time_control']} | "
            f"Tours joués : {information['actual_round']-1}/{information['nb_rounds']}"
        )
