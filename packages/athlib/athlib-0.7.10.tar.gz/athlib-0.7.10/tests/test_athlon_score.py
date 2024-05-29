"""Unit tests for iaaf_score.py."""

from unittest import TestCase, main
from athlib.athlon_score import performance, scoring_key, score, unit_name
from athlib.implements import get_implement_weight, get_specific_event_code


class MastersImplementWeightTests(TestCase):
    def test_specific_weight(self):
        self.assertEqual(get_implement_weight('JT', 'M', 'V80'), '400')
        self.assertEqual(get_implement_weight('JT', 'M', 'V85'), '400')

class IaafScoreTests(TestCase):
    """Test suite for the IAAF score calculation module."""

    def test_performance(self):
        """
        Test the function to calculate the required performance for a given
        score.
        """
        self.assertEqual(performance("F", "10000", 915), 2400.73)
        self.assertEqual(performance("M", "110H", 973), 14.01)
        self.assertEqual(performance("M", "110H", 974), 14)
        self.assertEqual(performance("F", "HJ", 1000), 1.82)
        self.assertEqual(performance("M", "WT", 1), 1.53)
        self.assertEqual(performance("F", "JT", 700), 41.68)
        self.assertEqual(performance("M", "PV", 1284), 6.16)

        # You need 1m to score 0, so that's what you get back
        self.assertEqual(performance("M", "PV", 0), 1.0)
        self.assertEqual(performance("M", "PV", -100), 1.0)
        self.assertEqual(performance("M", "NA", 500), None)


    def test_scoring_key(self):
        """
        Test the function to calculate the scoring key from the gender and
        event code.
        """
        self.assertEqual(scoring_key("m", "100"), "M-100")
        self.assertEqual(scoring_key("f", "400h"), "F-400H")
        self.assertEqual(scoring_key("M", "3000SC"), "M-3000SC")
        self.assertEqual(scoring_key("F", "lJ"), "F-LJ")
        self.assertEqual(scoring_key("m", "Hj"), "M-HJ")
        self.assertEqual(scoring_key("f", "jt"), "F-JT")
        self.assertEqual(scoring_key("M", "WT"), "M-WT")

    def test_score(self):
        """Test the function to calculate the score for a given performance."""
        self.assertEqual(score("F", "10000", 2400), 915)
        self.assertEqual(score("M", "110H", 14.01), 973)
        self.assertEqual(score("M", "110H", 14), 975)
        self.assertEqual(score("F", "HJ", 1.93), 1145)
        self.assertEqual(score("M", "WT", 1.53), 1)
        self.assertEqual(score("M", "WT", 1), 0)
        self.assertEqual(score("F", "JT", 41.68), 700)
        self.assertEqual(score("M", "PV", 6.16), 1284)

        self.assertEqual(score("M", "LJ", 0.5), 0)
        self.assertEqual(score("M", "100", 45), 0)

        self.assertEqual(score("?", "NA", 42), None)

        self.assertEqual(score("M", "1000", 150), 988)



    def test_unit_name(self):
        """Test the unit names for jumps, throws and track events."""
        self.assertEqual(unit_name("100"), "seconds")
        self.assertEqual(unit_name("200H"), "seconds")
        self.assertEqual(unit_name("3000SC"), "seconds")
        self.assertEqual(unit_name("LJ"), "metres")
        self.assertEqual(unit_name("PV"), "metres")
        self.assertEqual(unit_name("SP"), "metres")
        self.assertEqual(unit_name("WT"), "metres")

    def test_wma_adjusted_score(self):
        "Extra bonus for being old, used by WMA"
        self.assertEqual(score("M", "60H", 10.58), 437)


        self.assertEqual(score("M", "60H", 11.25, 50), 489)
        self.assertEqual(score("M", "LJ", 4.77, 50), 556)
        self.assertEqual(score("M", "1000", 272.91, 62), 299)

        # Javelin for different ages - reintroduce with some proper jav test data
        # self.assertEqual(score("M", "JT", 30.0), 299) # senior
        # self.assertEqual(score("M", "JT", 30.0, 50), 396) # M50
        # self.assertEqual(score("M", "JT", 30.0, 80), 781)
        # self.assertEqual(score("M", "JT", 30.0, 85), 937)

        
        self.assertEqual(score("M", "SP", 7.33, 63), 425)

        self.assertEqual(score("F", "60H", 10.90, 53), 777)
        self.assertEqual(score("F", "HJ", 1.29, 53), 644)

        # tests from BMAF indoor pentathlon 2023
        self.assertEqual(score("M", "LJ", 3.57, 77), 593)
        self.assertEqual(score("M", "LJ", 5.43, 35), 508)

        # real one - Amanda Broadhurst at BMAF indoor pentathlon
        # https://data.opentrack.run/en-gb/x/2023/GBR/bmaf-ipen/event/
        self.assertEqual(score("F", "60H", 12.18, 40), 485)


        # 2023, someone changed the WMA Hammer factors for some reason.
        # Hammer only done by Masters,  Cheshire Tables has changed too
        # Brian Slaughter's throw from BMAF Throws Pentathlon...
        self.assertEqual(score("M", "HT", 29.43, 65), 504)
        self.assertEqual(score("F", "WT", 13.62, 65), 824)



    def test_esaa_adjusted_score(self):
        # Tha famous boys 800 issue.
        self.assertEqual(score("M", "800", 120, esaa=True), 769)





if __name__ == '__main__':
    main()
