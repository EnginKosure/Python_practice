from compute_launch import days_until_launch


def test_days_until_launch_4():
    assert(days_until_launch(22, 26) == 4)


def test_days_until_launch_0():
    assert(days_until_launch(253, 253) == 0)


def test_days_until_launch_0_negative():
    assert(days_until_launch(83, 64) == -19)


def test_days_until_launch_1():
    assert(days_until_launch(9, 10) == 1)

# The name of the test file must start with test_, conventionally the same with the test_file_to_be_tested
# only writing pytest on terminal is enough for running tests.
