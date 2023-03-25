from typing import Union, List, Dict
from src.insights.jobs import read
from src.utils.verify_dict import verify_keys, verify_values


def get_max_salary(path: str) -> int:
    jobs = read(path)

    max_salary = 0

    for job in jobs:
        if job["max_salary"] and job["max_salary"] != "invalid":
            if int(job["max_salary"]) > max_salary:
                max_salary = int(job["max_salary"])

    return max_salary


def get_min_salary(path: str) -> int:
    jobs = read(path)

    min_salary = min(
        int(job["min_salary"])
        for job in jobs
        if job["min_salary"] and job["min_salary"] != "invalid"
    )

    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        verify_keys(job)
        verify_values([job["max_salary"], job["min_salary"], salary])

    except (TypeError, ValueError):
        raise ValueError()

    else:
        return int(salary) in list(
            range(int(job["min_salary"]), int(job["max_salary"]))
        )


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:

    filtered_jobs = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)

        except (TypeError, ValueError):
            ...

    return filtered_jobs
