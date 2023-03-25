from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, "r") as file:
        jobs_reader = csv.DictReader(file)
        return list(jobs_reader)


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)

    list_jobs_type = []

    for job in jobs:
        if job["job_type"] not in list_jobs_type:
            list_jobs_type.append(job["job_type"])

    return list_jobs_type


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    list_jobs_type = [job for job in jobs if job["job_type"] == job_type]

    return list_jobs_type
