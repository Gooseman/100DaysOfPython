import unittest
from types import SimpleNamespace
from unittest.mock import patch

import birthday_wisher


def make_person(name: str, email: str, year: int, month: int, day: int):
    return {"Name": name, "Email": email, "Year": year, "Month": month, "Day": day}


class TestBirthdayWisher(unittest.TestCase):

    @patch("birthday_wisher.read_birthdays")
    def test_get_all_birthdays_all_born_on_same_day_one_group_with_all(self, mock_read):
        person = [
            make_person(f"P{i}", f"p{i}@example.com", 1990 + (i % 30), 1, 1)
            for i in range(10)
        ]
        birthday_group = SimpleNamespace(to_dict=lambda **kwargs: person)

        mock_read.return_value = [((1, 1), birthday_group)]

        birthdays = birthday_wisher.get_all_birthdays()

        self.assertIn((1, 1), birthdays)
        self.assertEqual(len(birthdays[(1, 1)]), 10)
        self.assertEqual(birthdays[(1, 1)], person)

    @patch("birthday_wisher.read_birthdays")
    def test_get_all_birthdays_one_person_one_group(self, mock_read):
        person = make_person("P0", "p0@example.com", 1990, 1, 1)
        birthday_group = SimpleNamespace(to_dict=lambda **kwargs: [person])

        mock_read.return_value = [((1, 1), birthday_group)]

        all_birthdays = birthday_wisher.get_all_birthdays()

        self.assertIn((1, 1), all_birthdays)
        self.assertEqual(len(all_birthdays[(1, 1)]), 1)
        self.assertEqual(all_birthdays[(1, 1)], [person])

    @patch("birthday_wisher.read_birthdays")
    def test_get_all_birthdays_multiple_people_share_multiple_birthdays_distinct_groups(
        self, mock_read
    ):
        birthdays_1 = [
            make_person("A1", "a1@example.com", 1990, 1, 1),
            make_person("A2", "a2@example.com", 1991, 1, 1),
        ]
        birthdays_2 = [
            make_person("B1", "b1@example.com", 1985, 2, 2),
            make_person("B2", "b2@example.com", 1986, 2, 2),
            make_person("B3", "b3@example.com", 1987, 2, 2),
        ]
        birthday_1_group = SimpleNamespace(to_dict=lambda **kwargs: birthdays_1)
        birthday_2_group = SimpleNamespace(to_dict=lambda **kwargs: birthdays_2)

        mock_read.return_value = [
            ((1, 1), birthday_1_group),
            ((2, 2), birthday_2_group),
        ]

        all_birthdays = birthday_wisher.get_all_birthdays()

        self.assertEqual(all_birthdays[(1, 1)], birthdays_1)
        self.assertEqual(all_birthdays[(2, 2)], birthdays_2)

    @patch("birthday_wisher.read_birthdays")
    def test_get_all_birthdays_one_person_per_birthday_distinct_keys_for_each(
        self, mock_read
    ):
        birthdays_1 = [make_person("A1", "a1@example.com", 1990, 1, 1)]
        birthdays_2 = [make_person("A2", "a2@example.com", 1992, 2, 1)]
        birthdays_3 = [make_person("B1", "b1@example.com", 1985, 2, 2)]
        birthday_1_group = SimpleNamespace(to_dict=lambda **kwargs: birthdays_1)
        birthday_2_group = SimpleNamespace(to_dict=lambda **kwargs: birthdays_2)
        birthday_3_group = SimpleNamespace(to_dict=lambda **kwargs: birthdays_3)

        mock_read.return_value = [
            ((1, 1), birthday_1_group),
            ((2, 2), birthday_2_group),
            ((2, 1), birthday_3_group),
        ]

        all_birthdays = birthday_wisher.get_all_birthdays()

        self.assertEqual(all_birthdays[(1, 1)], birthdays_1)
        self.assertEqual(all_birthdays[(2, 2)], birthdays_2)
        self.assertEqual(all_birthdays[(2, 1)], birthdays_3)

    @patch("birthday_wisher.read_birthdays")
    def test_get_all_birthdays_empty(self, mock_read):
        mock_read.return_value = []

        all_birthdays = birthday_wisher.get_all_birthdays()

        self.assertEqual(all_birthdays, {})

    @patch("birthday_wisher.get_today", return_value=(2026, 6, 16))
    def test_get_todays_birthdays_no_matching_date_returns_empty_list(self, _):
        birthdays = {(1, 1): [make_person("X", "x@example.com", 1990, 1, 1)],
                     (2, 2): [make_person("Y", "y@example.com", 1991, 2, 2)]}
        result_no_match = birthday_wisher.get_todays_birthdays(birthdays)
        self.assertEqual(result_no_match, [])

    @patch("birthday_wisher.get_today", return_value=(2026, 6, 16))
    def test_get_todays_birthdays_matching_date_with_multiple_people_returns_list(self, _):
        todays = [
            make_person("Bob", "b@example.com", 1990, 6, 16),
            make_person("Carol", "c@example.com", 1985, 6, 16),
        ]
        birthdays = {(6, 16): todays, (7, 7): [make_person("D", "d@example.com", 2000, 7, 7)]}

        result = birthday_wisher.get_todays_birthdays(birthdays)
        self.assertEqual(result, todays)

    @patch("birthday_wisher.get_today", return_value=(2026, 6, 16))
    def test_get_age_ending_with_1_returns_1st(self, _):
        self.assertEqual(birthday_wisher.get_age(2005), "21st")

    @patch("birthday_wisher.get_today", return_value=(2026, 6, 16))
    def test_get_age_ending_with_2_returns_2nd(self, _):
        self.assertEqual(birthday_wisher.get_age(2004), "22nd")

    @patch("birthday_wisher.get_today", return_value=(2026, 6, 16))
    def test_get_age_ending_with_3_returns_3rd(self, _):
        self.assertEqual(birthday_wisher.get_age(2003), "23rd")

    @patch("birthday_wisher.get_today", return_value=(2026, 6, 16))
    def test_get_age_ending_with_11_returns_11th(self, _):
        self.assertEqual(birthday_wisher.get_age(2015), "11th")

    @patch("birthday_wisher.get_today", return_value=(2026, 6, 16))
    def test_get_age_ending_with_12_returns_12th(self, _):
        self.assertEqual(birthday_wisher.get_age(2014), "12th")

    @patch("birthday_wisher.get_today", return_value=(2026, 6, 16))
    def test_get_age_ending_with_13_returns_13th(self, _):
        self.assertEqual(birthday_wisher.get_age(2013), "13th")

    @patch("birthday_wisher.get_today", return_value=(2026, 6, 16))
    def test_get_age_ending_with_6_returns_6th(self, _):
        self.assertEqual(birthday_wisher.get_age(2000), "26th")


if __name__ == "__main__":
    unittest.main()
