from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)

    list_jobs_industry = list(
        set(job["industry"] for job in jobs if job["industry"] != "")
    )

    return list_jobs_industry


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    list_jobs_industry = [job for job in jobs if job["industry"] == industry]

    return list_jobs_industry
