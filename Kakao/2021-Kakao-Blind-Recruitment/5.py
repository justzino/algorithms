from collections import deque


def solution(play_time, adv_time, logs):
    play_time = convert_to_sec(play_time)
    adv_time = convert_to_sec(adv_time)

    if play_time == adv_time:
        return "00:00:00"

    starts = []
    ends = []
    for log in logs:
        start, end = log.split('-')
        start = convert_to_sec(start)
        end = convert_to_sec(end)

        starts.append(start)
        ends.append(end)

    starts.sort()  # 정렬
    ends.sort()

    #### 테스트용 ####
    # tmp_starts = [convert_to_time(x) for x in starts]
    # tmp_ends = [convert_to_time(x) for x in ends]
    # print("starts: ", tmp_starts)
    # print("ends: ", tmp_ends)

    starts = deque(starts)  # 큐로 변환
    ends = deque(ends)
    # 투 포인터
    start = starts.popleft()
    end = ends.popleft()
    count = 0  # 시간별 count 기록
    all_times = [0] * (play_time + 1)  # 시간별 누적 count 기록
    max_ad_times = 0  # 가장 큰 공익광고 누적 재생시간
    max_ad_start = 0  # 누적 재생시간 가장 클 때의 시작 시간
    for t in range(play_time + 1):
        if t != 0:
            all_times[t] += all_times[t - 1]  # 시간별 누적 count 기록
        all_times[t] += count

        while t == start:
            count += 1
            if starts:
                start = starts.popleft()
            if not starts:
                break

        while t == end:
            count -= 1
            if ends:
                end = ends.popleft()
            if not ends:
                break

        # 광고 끝날 수 있는 시간 확보했을 때부터 누적시간 계산
        if t >= adv_time:
            ad_start = t - adv_time
            if max_ad_times < all_times[t] - all_times[ad_start]:
                max_ad_times = all_times[t] - all_times[ad_start]
                max_ad_start = ad_start
                # print(f"{convert_to_time(ad_start)}-{convert_to_time(t)}, max_ad_times: {convert_to_time(max_ad_times)}")

    result = convert_to_time(max_ad_start)

    return result


def convert_to_sec(time: str):  # time = "hh:mm:ss"
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s


def convert_to_time(time: int):
    m, s = divmod(time, 60)
    h, m = divmod(m, 60)
    return str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2)