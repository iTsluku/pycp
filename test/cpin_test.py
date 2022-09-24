import unittest
from unittest.mock import patch

from src import cpin


@patch("builtins.input")
class TestCompetitiveProgrammingInput(unittest.TestCase):
    def test_single_int(self, mock_input):
        mock_input.return_value = "7"
        single_int = cpin.si()
        assert single_int == 7

    def test_multiple_int(self, mock_input):
        mock_input.return_value = "7 3 2"
        multiple_int = cpin.mi()
        assert multiple_int == [7, 3, 2]

    def test_single_str(self, mock_input):
        mock_input.return_value = "7"
        single_str = cpin.ss()
        assert single_str == "7"

    def test_multiple_str(self, mock_input):
        mock_input.return_value = "7 3 2"
        multiple_str = cpin.ms()
        assert multiple_str == ["7", "3", "2"]

    def test_multiple_int_with_sep(self, mock_input):
        mock_input.return_value = "7,3,2"
        multiple_int = cpin.mi(sep=",")
        assert multiple_int == [7, 3, 2]

    def test_multiple_str_with_sep(self, mock_input):
        mock_input.return_value = "7.3.2"
        multiple_str = cpin.ms(sep=".")
        assert multiple_str == ["7", "3", "2"]

    def test_multiple_str_with_maxsplit(self, mock_input):
        mock_input.return_value = "7 3 2"
        multiple_str = cpin.ms(maxsplit=1)
        assert multiple_str == ["7", "3 2"]

    def test_multiple_int_with_maxsplit(self, mock_input):
        mock_input.return_value = "7 3 2"
        with self.assertRaises(ValueError):
            cpin.mi(maxsplit=1)
