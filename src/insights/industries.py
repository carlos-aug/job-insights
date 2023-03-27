from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    all_industries = set()
    for ind in data:
        if ind['industry'] != '':
            all_industries.add(ind['industry'])
    return all_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    data = []
    for job in jobs:
        if job['industry'] == industry:
            data.append(job)
    return data


if __name__ == "__main__":
    print(get_unique_industries('data/jobs.csv'))
