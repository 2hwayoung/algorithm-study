from collections import defaultdict
def solution(tasks):
    jobs = defaultdict(int)
    for task in tasks:
        jobs[task] = jobs[task] + 1
    answer = 0

    for key, value in jobs.items():
        if value < 2:
            return -1
        num_job = value // 3
        if value % 3 > 0:
            num_job = num_job + 1
        answer = answer + num_job

    return answer