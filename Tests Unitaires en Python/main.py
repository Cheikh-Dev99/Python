# Tests Unitaires en Python : unittest

# Importation du module unittest pour créer et exécuter des tests unitaires
import unittest


# Fonction que nous testons
def doubler(nombre):
    # Vérifie si l'entrée est bien un nombre (entier ou flottant)
    if not isinstance(nombre, (int, float)):
        # Si ce n'est pas un nombre, on lève une exception de type TypeError
        raise TypeError("L'entrée doit être un nombre")
    # Retourne le double du nombre si l'entrée est valide
    return nombre * 2


# Création d'une classe de tests qui hérite de unittest.TestCase
class TestDoublerFunction(unittest.TestCase):

    # Méthode spéciale appelée avant chaque test pour préparer des données (facultative mais utile)
    def setUp(self):
        # Initialisation de variables qui seront utilisées dans les tests
        self.a = 5  # Exemple d'un entier positif
        self.b = 0  # Exemple de zéro
        self.c = -3  # Exemple d'un entier négatif

    # Premier test unitaire : tester plusieurs cas pour la fonction doubler
    def test_doubler(self):
        # Vérifie si doubler(5) retourne 10
        self.assertEqual(doubler(self.a), 10)  # Test réussi si doubler(5) == 10
        # Vérifie si doubler(0) retourne 0
        self.assertEqual(doubler(self.b), 0)  # Test réussi si doubler(0) == 0
        # Vérifie si doubler(-3) retourne -6
        self.assertEqual(doubler(self.c), -6)  # Test réussi si doubler(-3) == -6

    # Deuxième test unitaire : vérifier le comportement avec un mauvais type
    def test_doubler_type(self):
        # Vérifie que la fonction lève une exception TypeError si on passe un string
        # On utilise assertRaises pour s'assurer que l'exception est bien levée
        with self.assertRaises(TypeError):
            doubler("string")  # doubler("string") doit lever une TypeError

    # Troisième test unitaire : tester la fonction avec plusieurs cas en une seule méthode
    def test_multiples(self):
        # Liste de tuples (input, output attendu) pour tester plusieurs cas
        test_cases = [
            (2, 4),  # doubler(2) doit retourner 4
            (0, 0),  # doubler(0) doit retourner 0
            (-3, -6),  # doubler(-3) doit retourner -6
            (5, 10),  # doubler(5) doit retourner 10
        ]
        # Boucle sur chaque cas de test
        for input_value, expected in test_cases:
            # subTest permet de tester plusieurs valeurs indépendamment sans arrêter les tests si un cas échoue
            with self.subTest(input=input_value):
                # Vérifie si doubler(input_value) retourne la valeur attendue
                self.assertEqual(doubler(input_value), expected)

    # Méthode appelée après chaque test pour effectuer des nettoyages (facultative)
    def tearDown(self):
        # Ici, on n'a rien à nettoyer, mais si on utilisait des fichiers ou des connexions, ce serait fait ici
        pass


# Cette partie est nécessaire pour exécuter les tests si le script est lancé directement
if __name__ == '__main__':
    # unittest.main() exécute tous les tests définis dans la classe
    unittest.main()
