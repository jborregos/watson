import unittest

from translator import englishtofrench, englishtogerman

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(
            englishtofrench("This is a simple case"),
            "C'est un cas simple")
        self.assertEqual(
            englishtofrench("The rain in Spain stays mainly in the plain"),
            "La pluie en Espagne reste principalement dans la plaine")
        self.assertEqual(
            englishtofrench("What a wonderful day!"),
            "Quelle belle journée !")
        self.assertEqual(englishtofrench(None),None)
        self.assertEqual(englishtofrench("Hello"),"Bonjour")

class TestEnglishToGerman(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(
            englishtogerman("This is a simple case"),
            "Dies ist ein einfacher Fall")
        self.assertEqual(
            englishtogerman("The rain in Spain stays mainly in the plain"),
            "Der Regen in Spanien bleibt vor allem in der Ebene")
        self.assertEqual(
            englishtogerman("What a wonderful day!"),
            "Was für ein wunderbarer Tag!")
        self.assertEqual(englishtogerman(None),None)
        self.assertEqual(englishtogerman("Hello"),"Hallo")


unittest.main()
