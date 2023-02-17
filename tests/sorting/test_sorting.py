from src.pre_built.sorting import sort_by

jobs = [
    {"min_salary": 5000, "max_salary": 10000, "date_posted": "2015-07-09"},
    {"min_salary": 2000, "max_salary": 5000, "date_posted": "2020-01-02"},
    {"min_salary": 600, "max_salary": 1000, "date_posted": "2022-01-03"},
    {"min_salary": 3500, "max_salary": 7500, "date_posted": "2002-05-02"},
    {"min_salary": 9000, "max_salary": 15000, "date_posted": "2005-10-15"},
    {"min_salary": 7, "max_salary": 10, "date_posted": "2021-12-25"},
]


def test_sort_by_criteria():
    jobs_max_sorted = [
        {"min_salary": 9000, "max_salary": 15000, "date_posted": "2005-10-15"},
        {"min_salary": 5000, "max_salary": 10000, "date_posted": "2015-07-09"},
        {"min_salary": 3500, "max_salary": 7500, "date_posted": "2002-05-02"},
        {"min_salary": 2000, "max_salary": 5000, "date_posted": "2020-01-02"},
        {"min_salary": 600, "max_salary": 1000, "date_posted": "2022-01-03"},
        {"min_salary": 7, "max_salary": 10, "date_posted": "2021-12-25"},
    ]

    sort_by(jobs, "max_salary")
    assert jobs == jobs_max_sorted

    jobs_min_sorted = [
        {"min_salary": 7, "max_salary": 10, "date_posted": "2021-12-25"},
        {"min_salary": 600, "max_salary": 1000, "date_posted": "2022-01-03"},
        {"min_salary": 2000, "max_salary": 5000, "date_posted": "2020-01-02"},
        {"min_salary": 3500, "max_salary": 7500, "date_posted": "2002-05-02"},
        {"min_salary": 5000, "max_salary": 10000, "date_posted": "2015-07-09"},
        {"min_salary": 9000, "max_salary": 15000, "date_posted": "2005-10-15"},
    ]

    sort_by(jobs, "min_salary")
    assert jobs == jobs_min_sorted

    jobs_date_sorted = [
        {"min_salary": 600, "max_salary": 1000, "date_posted": "2022-01-03"},
        {"min_salary": 7, "max_salary": 10, "date_posted": "2021-12-25"},
        {"min_salary": 2000, "max_salary": 5000, "date_posted": "2020-01-02"},
        {"min_salary": 5000, "max_salary": 10000, "date_posted": "2015-07-09"},
        {"min_salary": 9000, "max_salary": 15000, "date_posted": "2005-10-15"},
        {"min_salary": 3500, "max_salary": 7500, "date_posted": "2002-05-02"},
    ]

    sort_by(jobs, "date_posted")
    assert jobs == jobs_date_sorted
