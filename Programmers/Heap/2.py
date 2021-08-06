from collections import deque
import heapq


def solution(jobs):
    n = len(jobs)
    jobs.sort()
    ready_q = []
    jobs = deque(jobs)

    # 초기값 작업
    job_request = jobs.popleft()
    now_job = [job_request[1], job_request[0]]  # (작업 소요시간, 요청시간)
    time = now_job[1]
    answer = 0

    print(f"jobs: {jobs}")
    print(f"time + now_job : {time}, {now_job}")
    print()

    while True:
        # jobs 가 있고, 새로운 job이 request 되는 시점
        while jobs and time == jobs[0][0]:
            job_request = jobs.popleft()
            heapq.heappush(ready_q, job_request[1])

        print(f"ready_q: {ready_q}")

        # 현재 진행중인 job 이 아직 안 끝난 경우
        if time < now_job[0] + now_job[1]:
            print(f"time + now_job : {time}, {now_job[0] + now_job[1]}")
            print()
            time += 1
            answer += len(ready_q) + 1
            continue

        print(f"time + now_job : {time}, {now_job}")
        print()

        # 진행 중이 job 이 끝남
        # ready_q 와, jobs 둘다 없는 경우
        if not jobs and not ready_q:
            break

        # ready_q가 없는데, 아직 요청되지 않은 jobs 가 있는 경우
        if not ready_q:
            time = jobs[0][0]
            continue

        # ready_q가 있는 경우
        now_job = [heapq.heappop(ready_q), time]
        time += 1
        answer += len(ready_q) + 1

    print(answer)
    answer //= n

    return answer


if __name__ == '__main__':
    print(solution([[0, 3], [1, 9], [2, 6]]))
    print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]))   # 14
    print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]))  # 25
    print(solution([[0, 3], [1, 9], [2, 6]]))       # 9
    print(solution([[0, 1]]))   # 1
    print(solution([[1000, 1000]]))   # 1000
    print(solution([[0, 1], [0, 1], [0, 1]]))    # 2
    print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]))    # 2
    print(solution([[0, 1], [1000, 1000]]))    # 500
    print(solution([[100, 100], [1000, 1000]]))    # 500
    print(solution([[10, 10], [30, 10], [50, 2], [51, 2]])) # 6
    print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]))  # 7
    print([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]])    # 72
    print([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]])    # 72

