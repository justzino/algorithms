from collections import defaultdict


def solution(genres, plays):
    n = len(plays)

    genres_dict = defaultdict(list)
    n_by_genre = defaultdict(int)

    for i in range(n):
        genres_dict[genres[i]].append((plays[i], i))
        n_by_genre[genres[i]] += plays[i]

    sorted_genres = sorted(n_by_genre.items(), key=lambda x: -x[1])

    answer = []
    for genre, play in sorted_genres:
        genres_dict[genre].sort(key=lambda x: (-x[0], x[1]))

        answer.append(genres_dict[genre][0][1])
        if len(genres_dict[genre]) >= 2:
            answer.append(genres_dict[genre][1][1])

    print(genres_dict)
    return answer


"""
장르별 2개씩 베스트 -> 앨범
장르 순서 : 속한 노래 재생 횟수
노래 순서 : (재생 횟수, 낮은 고유번호)
"""