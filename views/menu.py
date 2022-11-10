class MenuViews:
    def __init__(self):
        pass

    @staticmethod
    def title():
        print("\n*******************************")
        print("*                             *")
        print("*        CLUB D'ECHECS        *")
        print("*                             *")
        print("*******************************")

    @staticmethod
    def main_menu():
        print("\n------- MENU PRINCIPAL -------\n")
        print("[1] Créer un nouveau tournoi")
        print("[2] Charger un tournoi")
        print("[3] Ajouter un nouveau joueur")
        print("[4] Liste des joueurs")
        print("[5] Rapports")
        print("[6] Quitter\n")

    @staticmethod
    def show_new_tournament():
        print("\n------- NOUVEAU TOURNOI -------\n")

    @staticmethod
    def show_time_control():
        print("\nChoix du controle du temps :\n")
        print("[1] Bullet")
        print("[2] Blitz")
        print("[3] Rapid")
        print("\n[retour] Retour au Menu principal")

    @staticmethod
    def tournament_validation(information, players):
        """Confirmation des informations d'un tournoi avant son
        enregistrement dans la base de données"""
        print("\n------- CRÉATION D'UN NOUVEAU TOURNOI -------\n")
        print(f"{information[0]}", end=" | ")
        print(f"{information[1]}", end=" | ")
        print(f"Description : {information[2]}", end=" | ")
        print(f"Tours :{information[4]}", end=" | ")
        print(f"Contrôle du temps: {information[5]}")
        print("\n" f"Joueurs ({information[3]} total) :" "\n")

        for data in players:
            print(f"Joueur {players.index(data) + 1} : ", end="")
            print(f"{data['last_name']}, {data['first_name']}", end=" | ")
            print(f"{data['date_of_birth']}", end=" | ")
            print(f"Classement : {data['rank']}")

        print("\nEnregistrer ? [o/n] ", end="")

    @staticmethod
    def tournament_registration():
        print("\nLe tournoi est enregistré !")

    @staticmethod
    def start_tournament():
        print("\nCommencer le tournoi ? [o/n] ", end="")

    @staticmethod
    def choose_players(players, player_number):
        """Affiche la liste des joueurs à sélectionner"""
        print(f"\nChoisir un joueur {player_number} :\n")
        for i in range(len(players)):
            print(f"{players[i]['player_id']}", end=" | ")
            print(f"{players[i]['last_name']}, {players[i]['first_name']}", end=" | ")
            print(f"{players[i]['gender']} | {players[i]['date_of_birth']}", end=" | ")
            print(f"Classement : {players[i]['rank']}")

        print("\n[retour] Retour au menu principal")

    @staticmethod
    def choose_tournament(tournaments):
        """Affiche la liste des tournois à sélectionner"""
        print("\n")
        print(("-------- CHOISIR UN TOURNOI --------\n").center(110, " "))

        for i in range(len(tournaments)):
            print(f"[{tournaments[i]['number']}]", end=" | ")
            print(tournaments[i]["name"], end=" | ")
            print(tournaments[i]["location"], end=" | ")
            print(tournaments[i]["description"], end=" | ")
            print(f"Début : {tournaments[i]['start_date']}", end=" | ")
            print(f"Fin : {tournaments[i]['end_date']}", end=" | ")
            print(f"Tours {tournaments[i]['actual_round']-1}/{tournaments[i]['nb_rounds']}")

        print("\n[retour] Retour au menu principal")

    @staticmethod
    def show_new_player():
        print("\n\n------- NOUVEAU JOUEUR -------\n")

    @staticmethod
    def player_validation(information):
        """Confirmation des informations d'un joueur avant son
        enregistrement dans la base de données"""
        print("\nNouveau joueur créé :\n")
        print(f"{information[0]}, {information[1]}", end=" | ")
        print(f"Date de naissance : {information[2]}", end=" | ")
        print(f"Sexe : {information[3]}", end=" | ")
        print(f"Classemnt : {information[4]}")
        print("\nEnregistrer ? [o/n] ", end="")

    @staticmethod
    def player_registration():
        print("\nLe joueur est enregistré !")

    @staticmethod
    def show_reports():
        print("\n------- RAPPORTS -------\n")
        print("[1] Les joueurs d'un tournoi")
        print("[2] Les tournois")
        print("[3] Les tours d'un tournoi")
        print("[4] Les matchs d'un tournoi")
        print("\n[retour] Retour au menu principal")

    @staticmethod
    def show_reports_player():
        print("\n[1] Trier par nom")
        print("[2] Trier par classement")
        print("[3] Mettre à jour le classement")
        print("\n[retour] Retour au menu principal")

    @staticmethod
    def input_option(option):
        print(f"\n{option} : ", end="")

    @staticmethod
    def option_main():
        print("\nChoisir une [option] et appuyez sur Entrée : ", end="")

    @staticmethod
    def go_out():
        print("\nEtes-vous sûr de vouloir quitter le programme ? [o/n] ", end="")

    @staticmethod
    def input_error():
        print("\nErreur de saisie, veuillez entrer une option valide.")

    @staticmethod
    def player_selected():
        print("\nJoueur déjà sélectionné. Veuillez sélectionner un autre joueur.")

    @staticmethod
    def other_report():
        print("\nSouhaitez-vous voir un autre rapport? [o/n] ", end="")

    @staticmethod
    def update_rank():
        print("\nMettre à jour les classements ? [o/n] ", end="")

    @staticmethod
    def rank_update(player):
        print(f"\nMise à jour {player.last_name}, {player.first_name}")
