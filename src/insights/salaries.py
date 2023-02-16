from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    file = read(path)
    salaries = set()
    for item in file:
        if item["max_salary"].isdigit():
            salaries.add(int(item["max_salary"]))
    highest_salary = max(salaries)
    return highest_salary
    # raise NotImplementedError


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    file = read(path)
    salaries = set()
    for item in file:
        if item["min_salary"].isdigit():
            salaries.add(int(item["min_salary"]))
    lowest_salary = min(salaries)
    return lowest_salary
    # raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    try:
        min_s = int(job["min_salary"])
        max_s = int(job["max_salary"])
        int(salary)
    except Exception:
        raise ValueError
    if min_s > max_s:
        raise ValueError
    return min_s <= int(salary) <= max_s
    # raise NotImplementedError


def filter_by_salary_range_conditions(
    salary: Union[str, int],
    min_s: int,
    max_s: int
) -> bool:
    try:
        if min_s < max_s and min_s <= int(salary) <= max_s:
            return True
        else:
            return False
    except Exception:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    all_jobs_by_salary = []
    for job in jobs:
        try:
            min_s = int(job["min_salary"])
            max_s = int(job["max_salary"])
            if filter_by_salary_range_conditions(salary, min_s, max_s):
                all_jobs_by_salary.append(job)
        except Exception:
            print()
    return all_jobs_by_salary

    # raise NotImplementedError
