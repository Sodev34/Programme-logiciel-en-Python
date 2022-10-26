class MenuViews:
    def __init__(self):
        pass

    @staticmethod
    def title():
        print("*******************************")
        print("*                             *")
        print("*        CLUB D'ECHECS        *")
        print("*                             *")
        print("*******************************")

    @staticmethod
    def main_menu():
        print()
        print("------- MENU PRINCIPAL -------")
        print()
        print("[1] Créer un nouveau tournoi")
        print("[2] Charger un tournoi")
        print("[3] Ajouter un nouveau joueur")
        # print("[4] Modififer un joueur")
        print("[4] Rapports")
        print("[5] Quitter")
        print()

    @staticmethod
    def show_new_tournament():
        print()
        print("------- NOUVEAU TOURNOI -------")
        print()

    @staticmethod
    def show_time_control():
        print()
        print("Choix du controle du temps :")
        print()
        print("[1] Bullet")
        print("[2] Blitz")
        print("[3] Rapid")
        print()
        print("[retour] Retour au Menu principal")

    @staticmethod
    def tournament_validation(information, players):
        print()
        print("------- CRÉATION D'UN NOUVEAU TOURNOI -------")
        print()
        print(f"{information[0]}", end=" | ")
        print(f"{information[1]}", end=" | ")
        print(f"Description : {information[2]}", end=" | ")
        print("Tours : 4", end=" | ")
        print(f"Contrôle du temps: {information[3]}")
        print("\nJoueurs (8 total) :\n")

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
        print(f"\nChoisir un joueur {player_number} :\n")
        for i in range(len(players)):
            print(f"{players[i]['player_id']}", end=" | ")
            print(f"{players[i]['last_name']}, {players[i]['first_name']}", end=" | ")
            print(f"{players[i]['gender']} | {players[i]['date_of_birth']}", end=" | ")
            print(f"Classement : {players[i]['rank']}")

        print("\n[retour] Retour au menu principal")

    @staticmethod
    def choose_tournament(tournaments):
        print()
        print("------- CHOISIR UN TOURNOI -------\n")

        for i in range(len(tournaments)):
            print(f"[{tournaments[i]['number']}]", end=" | ")
            print(tournaments[i]["name"], end=" | ")
            print(tournaments[i]["location"], end=" | ")
            print(tournaments[i]["description"], end=" | ")
            print(f"Début : {tournaments[i]['start_date']}", end=" | ")
            print(f"Fin : {tournaments[i]['end_date']}", end=" | ")
            print(f"Tours {tournaments[i]['rounds']-1}/{tournaments[i]['nb_rounds']}")

        print("\n[retour] Retour au menu principal")

    @staticmethod
    def show_new_player():
        print()
        print()
        print("------- NOUVEAU JOUEUR -------\n")

    @staticmethod
    def player_validation(information):
        print()
        print("Nouveau joueur créé :\n")
        print(f"{information[0]}, {information[1]}", end=" | ")
        print(f"Date de naissance : {information[2]}", end=" | ")
        print(f"Sexe : {information[3]}", end=" | ")
        print(f"Classemnt : {information[4]}")
        print("\nEnregistrer ? [o/n] ", end="")

    @staticmethod
    def update_player_information(player, options):
        print()
        print("------- METTRE A JOUR UN JOUEUR -------\n")
        print(f"Mise à jour {player.last_name}, {player.first_name}\n")
        for i in range(len(options)):
            print(f"[{i+1}] Mise à jour {options[i]}")

        print("\n[retour] Retour au menu principal")

    @staticmethod
    def player_registration():
        print("\nLe joueur est enregistré !")

    @staticmethod
    def show_reports():
        print("------- RAPPORTS -------")
        print("[1] Les joueurs")
        print("[2] Les joueurs d'un tournoi")
        print("[3] Les tournois")
        print("[4] Les tours d'un tournoi")
        print("[5] Les matchs d'un tournoi")
        print("\n[retour] Retour au menu principal")

    @staticmethod
    def show_reports_player():
        print("[1] Trier par nom")
        print("[2] Trier par classement")
        print("\n[retour] Retour au menu principal")

    @staticmethod
    def input_option(option):
        print(f"\n{option} : ", end="")

    @staticmethod
    def option_main():
        print("\nChoisir une [option] et appuyez sur Entrée : ", end="")

    @staticmethod
    def are_you_exit():
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
    def update_header(player):
        print(f"\nMise à jour {player.last_name}, {player.first_name}")
