from unittest import TestCase

from src.number_to_french import convert_number_to_french

test_cases = [
    (0, "zéro"),
    (1, "un"),
    (5, "cinq"),
    (10, "dix"),
    (11, "onze"),
    (15, "quinze"),
    (20, "vingt"),
    (21, "vingt-et-un"),
    (30, "trente"),
    (35, "trente-cinq"),
    (50, "cinquante"),
    (51, "cinquante-et-un"),
    (68, "soixante-huit"),
    (70, "soixante-dix"),
    (75, "soixante-quinze"),
    (99, "quatre-vingt-dix-neuf"),
    (100, "cent"),
    (101, "cent-un"),
    (105, "cent-cinq"),
    (111, "cent-onze"),
    (123, "cent-vingt-trois"),
    (168, "cent-soixante-huit"),
    (171, "cent-soixante-onze"),
    (175, "cent-soixante-quinze"),
    (199, "cent-quatre-vingt-dix-neuf"),
    (200, "deux-cents"),
    (201, "deux-cent-un"),
    (555, "cinq-cent-cinquante-cinq"),
    (999, "neuf-cent-quatre-vingt-dix-neuf"),
    (1000, "mille"),
    (1001, "mille-un"),
    (1111, "mille-cent-onze"),
    (1199, "mille-cent-quatre-vingt-dix-neuf"),
    (1234, "mille-deux-cent-trente-quatre"),
    (1999, "mille-neuf-cent-quatre-vingt-dix-neuf"),
    (2000, "deux-milles"),
    (2001, "deux-mille-un"),
    (2020, "deux-mille-vingt"),
    (2021, "deux-mille-vingt-et-un"),
    (2345, "deux-mille-trois-cent-quarante-cinq"),
    (9999, "neuf-mille-neuf-cent-quatre-vingt-dix-neuf"),
    (10000, "dix-milles"),
    (11111, "onze-mille-cent-onze"),
    (12345, "douze-mille-trois-cent-quarante-cinq"),
    (123456, "cent-vingt-trois-mille-quatre-cent-cinquante-six"),
    (654321, "six-cent-cinquante-quatre-mille-trois-cent-vingt-et-un"),
    (999999, "neuf-cent-quatre-vingt-dix-neuf-mille-neuf-cent-quatre-vingt-dix-neuf")
]


class Test(TestCase):
    def test_convert_number_to_french(self):
        for number, expected_french in test_cases:
            self.assertEqual(convert_number_to_french(number), expected_french)
