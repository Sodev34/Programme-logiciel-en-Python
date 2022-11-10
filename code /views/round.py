from prettytable import PrettyTable


class RoundViews:
    def __init__(self):
        self.table = PrettyTable()

        self.round_field = [
            "Match ",
            "Joueur 1",
            "Score joueur 1",
            " ",
            "Joueur 2",
            "Score joueur 2",
        ]

        self.results_field = ["Classement du Tournoi", "Joueur", "Score Final", "Classement Global"]

    def display_matches(self, matches):
        """Permet d'afficher les matchs du tour"""
        self.table.clear()
        self.table.field_names = self.round_field

        for i in range(len(matches)):
            row = list(matches[i])
            row.insert(0, str(i + 1))
            row.insert(3, "vs.")

            self.table.add_row(row)

        print(self.table)

    def display_results(self, cur_tour):
        """Permet d'afficher les resultats du tour"""
        self.table.clear()
        self.table.field_names = self.results_field

        for i in range(len(cur_tour.players)):
            self.table.add_row(
                [
                    i + 1,
                    cur_tour.players[i]["last_name"] + " " + cur_tour.players[i]["first_name"],
                    cur_tour.players[i]["result"],
                    cur_tour.players[i]["rank"],
                ]
            )

        print(f"\n{cur_tour.name}, {cur_tour.location} | Description : {cur_tour.description}")
        print(
            f"Début : {cur_tour.start_date} | Fin : {cur_tour.end_date} | Controle du temps : {cur_tour.time_control}\n\n"
        )
        print(("------ SCORES FINAL ------\n").center(75, " "))

        print(self.table)

    @staticmethod
    def round_header(tour, start_time):
        """Permet d'afficher les informations du tournoi concerné par le round"""
        print(f"\n{tour.name}, {tour.location} | Description : {tour.description}")
        print(f"Début : {tour.start_date} | Controle du temps : {tour.time_control}\n\n")
        print((f"*** Tour {tour.actual_round}/{tour.nb_rounds} *** {start_time} ***").center(90, " "))

    @staticmethod
    def extra_round():
        print("\nEncore un tour ? [oui]")
        print("Retour au menu principal ? [retour]")

    @staticmethod
    def result_options(match_nb, row):
        print("\nMatch ", match_nb, ":")
        print("\n[0][ Match nul ]", end="   ")
        print((f"[1][ {row[0]} gagne le match ]"), end="   ")
        print((f"[2][ {row[2]} gagne le match ]"))
        print("\n[retour] Retour au menu principal")

    @staticmethod
    def result_input():
        print("\nEntrer le résultat :", end=" ")
