from src.cpin import si, mi, ss, ms
from unittest.mock import patch

test_case_mock = {
    0: ("4", "3 1 4 3"),
    1: ("5", "1 1 1 1 1"),
    2: ("1", "1"),
    3: ("6", "6 5 4 3 2 1"),
    4: ("7", "1 2 1 7 1 2 1"),
}


@patch("builtins.input")
def cpin_suite(mock_input) -> None:
    mock_input.return_value = "5"
    t = si()  # number of test cases
    for i in range(t):
        mock_input.return_value = test_case_mock[i][0]
        n = si()  # length of sequence a
        mock_input.return_value = test_case_mock[i][1]
        a = mi()  # sequence a, containing n int values

    mock_input.return_value = "hello"
    x = ss()
    mock_input.return_value = "hello world"
    y = ms()


if __name__ == "__main__":
    cpin_suite()
