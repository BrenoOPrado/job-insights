from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path) as file:
        csv_file = csv.DictReader(file)
        result = []
        for item in csv_file:
            result.append(item)
        return result
    # raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    file = read(path)
    job_types = set()
    for item in file:
        job_types.add(item["job_type"])
    return job_types
    # raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    all_jobs_by_type = []
    for item in jobs:
        if item["job_type"] == job_type:
            all_jobs_by_type.append(item)
    return all_jobs_by_type
    # raise NotImplementedError
