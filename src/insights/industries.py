from typing import List, Dict
from jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    industries = set()
    for industry in data:
        ind = industry['industry']
        print(ind)
        industries.add(ind)
    print(ind)

    return industries


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
    raise NotImplementedError


if __name__ == "__main__":
    industries = read("data/.csv")
