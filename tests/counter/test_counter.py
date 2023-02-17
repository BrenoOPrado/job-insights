from src.pre_built.counter import count_ocurrences


def test_counter():
    counter_lower_case = count_ocurrences('data/jobs.csv', 'python')
    counter_upper_case = count_ocurrences('data/jobs.csv', 'PYTHON')
    counter_all_cases = count_ocurrences('data/jobs.csv', 'PyThOn')
    assert counter_lower_case == 1639
    assert counter_upper_case == 1639
    assert counter_all_cases == 1639
