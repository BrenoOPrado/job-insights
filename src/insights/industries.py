from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    file = read(path)
    industries = set()
    for item in file:
        if len(item["industry"]) > 0:
            industries.add(item["industry"])
    return industries
    # raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    all_jobs_by_industry = []
    for item in jobs:
        if item["industry"] == industry:
            all_jobs_by_industry.append(item)
    return all_jobs_by_industry
    # raise NotImplementedError
