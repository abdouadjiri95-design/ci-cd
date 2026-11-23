import unittest

from grades import clean_grades, average, mention


class TestCleanGrades(unittest.TestCase):
    def test_garde_valeurs_entre_0_et_20(self):
        self.assertEqual(clean_grades([0, 10, 20]), [0, 10, 20])

    def test_rejette_valeurs_hors_bornes(self):
        self.assertEqual(clean_grades([-5, 25, 12]), [12])

    def test_ignore_valeurs_non_numeriques(self):
        self.assertEqual(clean_grades(["12", None, 8.5]), [8.5])

    def test_liste_vide(self):
        self.assertEqual(clean_grades([]), [])


class TestAverage(unittest.TestCase):
    def test_moyenne(self):
        self.assertEqual(average([10, 12, 14]), 12)

    def test_moyenne_virgule(self):
        self.assertAlmostEqual(average([10, 15]), 12.5)

    def test_liste_vide_retourne_none(self):
        self.assertIsNone(average([]))

    def test_aucune_note_valide_retourne_none(self):
        self.assertIsNone(average([-3, 21, "absent"]))

    def test_ignore_notes_invalides(self):
        self.assertEqual(average([10, "x", 20]), 15)


class TestMention(unittest.TestCase):
    def test_none(self):
        self.assertEqual(mention(None), "Aucune note")

    def test_insuffisant(self):
        self.assertEqual(mention(9.99), "Insuffisant")

    def test_moyen(self):
        self.assertEqual(mention(10), "Moyen")
        self.assertEqual(mention(13.99), "Moyen")

    def test_bien(self):
        self.assertEqual(mention(14), "Bien")
        self.assertEqual(mention(20), "Bien")


if __name__ == "__main__":
    unittest.main()