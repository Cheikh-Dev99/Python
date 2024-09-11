# Python : la géstion des erreurs (ValueError, TypeError, IndexError, Exception)

def verifier_age(age):
    """Vérifie que l'utilisateur a plus de 12 ans pour s'inscrire au club."""
    if age <= 12:
        raise ValueError("Vous devez avoir plus de 12 ans pour rejoindre le club.")
    return True


def verifier_nombre_sessions(nombre):
    """Vérifie que le nombre de sessions est un nombre positif."""
    if nombre <= 0:
        raise ValueError("Le nombre de sessions doit être supérieur à zéro.")
    return True


def verifier_nom(nom):
    """Vérifie que le nom ne contient que des lettres et des espaces."""
    if not all(c.isalpha() or c.isspace() for c in nom):
        raise ValueError("Le nom ne peut contenir que des lettres et des espaces.")
    return True


def inscription_club():
    niveaux_competence = ["Débutant", "Intermédiaire", "Avancé"]
    sessions_disponibles = {"Débutant": 5, "Intermédiaire": 7, "Avancé": 10}

    while True:
        try:
            # 1. Demander le nom de l'utilisateur
            nom = input("Veuillez entrer votre nom : ")
            verifier_nom(nom)

            # 2. Demander l'âge de l'utilisateur
            while True:  # Boucle pour s'assurer que l'âge est valide
                age = input("Veuillez entrer votre âge : ")
                if not age.isdigit():
                    print("Erreur : L'âge doit être un nombre entier.")
                else:
                    age = int(age)
                    try:
                        verifier_age(age)
                        break  # Sortir de la boucle si l'âge est valide
                    except ValueError as ve:
                        print(f"Erreur : {ve}")

            print(f"Bienvenue, {nom} !\n")

            # 3. Afficher les niveaux de compétence disponibles
            print("Sélectionnez votre niveau de compétence en programmation :")
            for i, niveau in enumerate(niveaux_competence):
                print(f"{i}. {niveau}")

            # 4. Sélectionner un niveau de compétence
            while True:  # Boucle pour s'assurer que l'indice est valide
                niveau_index = input("\nEntrez le numéro correspondant à votre niveau de compétence : ")
                if not niveau_index.isdigit():
                    print("Erreur : Le numéro doit être un nombre entier.")
                else:
                    niveau_index = int(niveau_index)
                    if 0 <= niveau_index < len(niveaux_competence):
                        competence_choisie = niveaux_competence[niveau_index]
                        break  # Sortir de la boucle si l'indice est valide
                    else:
                        print("Erreur : L'indice que vous avez entré n'est pas valide.")
            print(f"Vous avez choisi le niveau : {competence_choisie}")

            # 5. Vérifier le nombre de sessions disponibles pour ce niveau
            sessions_max = sessions_disponibles.get(competence_choisie)
            if sessions_max is None:
                print("Erreur : Le niveau de compétence n'est pas valide.")
                continue

            # 6. Demander combien de sessions l'utilisateur souhaite suivre
            while True:  # Boucle pour s'assurer que le nombre de sessions est valide
                nombre_sessions = input(f"Combien de sessions souhaitez-vous suivre (max {sessions_max}) ? ")
                if not nombre_sessions.isdigit():
                    print("Erreur : Le nombre de sessions doit être un nombre entier.")
                else:
                    nombre_sessions = int(nombre_sessions)
                    try:
                        verifier_nombre_sessions(nombre_sessions)
                        if nombre_sessions > sessions_max:
                            print(
                                f"Erreur : Le nombre de sessions ne peut pas dépasser {sessions_max} pour le niveau {competence_choisie}.")
                        else:
                            break  # Sortir de la boucle si le nombre de sessions est valide
                    except ValueError as ve:
                        print(f"Erreur : {ve}")

            # Si tout est correct, afficher un message de confirmation
            print(f"Félicitations, {nom} ! Vous êtes inscrit à {nombre_sessions} session(s) en {competence_choisie}.")
            break  # Sortir de la boucle principale après une inscription réussie

        except ValueError as ve:
            print(f"Erreur de saisie : {ve}")
        except TypeError as te:
            print(f"Erreur de type : {te}")
        except IndexError:
            print("Erreur : L'indice que vous avez entré n'est pas valide.")
        except KeyError as ke:
            print(f"Erreur de clé : {ke}")
        except Exception as e:
            print(f"Erreur inattendue : {e}")

    print("\nMerci d'avoir rejoint notre club de programmation. À bientôt !")


# Lancer l'inscription
inscription_club()

