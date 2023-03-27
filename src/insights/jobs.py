from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    try:
        with open(path, 'r') as file:
            csv_jobs = list(csv.DictReader(file, delimiter=","))
        return csv_jobs
    except FileNotFoundError as err:
        return err


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    all_types = set()
    for job_type in data:
        type = job_type["job_type"]
        all_types.add(type)
    return all_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    data = []
    for job in jobs:
        if job['job_type'] == job_type:
            data.append(job)
    return data


if __name__ == "__main__":
    print(read("data/jobs.csv"))
