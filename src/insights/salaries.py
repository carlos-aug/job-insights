from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    max_value = 0
    for max in data:
        if max["max_salary"].isdigit():
            max_result = int(max["max_salary"])
            if max_result > max_value:
                max_value = max_result
    return max_value


def get_min_salary(path: str) -> int:
    data = read(path)
    min_value = 400000
    for min in data:
        if min["min_salary"].isdigit():
            min_result = int(min["min_salary"])
            if min_result < min_value:
                min_value = min_result
    return min_value


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job['min_salary'])
        max_salary_ = int(job['max_salary'])
        is_salary = int(salary)
        if min_salary > max_salary_:
            raise ValueError
    except Exception:
        raise ValueError
    return min_salary <= is_salary <= max_salary_


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    is_true = []
    for i in jobs:
        try:
            if matches_salary_range(i, salary):
                is_true.append(i)
        except ValueError:
            ...

    return is_true


if __name__ == "__main__":
    print(get_max_salary("data/jobs.csv"))
