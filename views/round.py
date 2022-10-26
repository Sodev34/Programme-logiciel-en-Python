from prettytable import PrettyTable


class RoundViews:
    def __init__(self):
        self.table = PrettyTable()

        self.round_field = [
            "Match ",
            "Nom Joueur 1",
            "Classement Joueur 1",
            "Score Joueur 1",
            " ",
            "Nom Joueur 2",
            "Classement Joueur 2",
            "Score Joueur 2",
        ]

        self.results_field = ["Classement du Tournoi", "Nom", "Score Final", "Classement Global"]

    def display_matches(self, matches):

        self.table.clear()
        self.table.field_names = self.round_field

        for i in range(len(matches)):
            row = list(matches[i])
            row.insert(0, str(i + 1))
            row.insert(4, "vs.")

            self.table.add_row(row)

        print(self.table)

    def display_results(self, cur_tour):

        self.table.clear()
        self.table.field_names = self.results_field

        for i in range(len(cur_tour.players)):
            self.table.add_row(
                [
                    i + 1,
                    cur_tour.players[i]["last_name"] + ", " + cur_tour.players[i]["first_name"],
                    cur_tour.players[i]["score"],
                    cur_tour.players[i]["rank"],
                ]
            )

        print("\n------ SCORES FINAL ------\n")
        print(f"{cur_tour.name}, {cur_tour.location} | Description : {cur_tour.description}")
        print(
            f"Début : {cur_tour.start_date} | Fin : {cur_tour.end_date} | Controle du temps : {cur_tour.time_control}\n"
        )

        print(self.table)

    def round_header(cur_tour, start_time):

        print("\n\n")

        s_1 = f"{cur_tour.name}, {cur_tour.location} | Description : {cur_tour.description}"
        s_2 = f"Début : {cur_tour.start_date} | Controle du temps : {cur_tour.time_control}\n"
        s_3 = f"- TOUR {cur_tour.rounds}/{cur_tour.nb_rounds} - {start_time} -"

        print(s_1.center(50, " "))
        print(s_2.center(50, " "))
        print(s_3.center(50, " "))

    def extra_round():
        print("\nEncore un tour ? [ok]")
        print("Retour au menu principal ? [retour]")

    def result_options(match_nb):
        print("\nMatch ", match_nb)
        print("[0] Match nul")
        print("[1] Joueur 1 gagne")
        print("[2] Joueur 2 gagne")
        print("\n[retour] Retour au menu principal")

    def score_input():
        print("\nEntrer le résultat :", end=" ")
