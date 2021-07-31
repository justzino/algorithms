from collections import defaultdict


class Song:
    def __init__(self, play, idx):
        self.play = play
        self.idx = idx


def solution(genres, plays):
    n = len(plays)
    songs_by_genre = defaultdict(list)
    time_of_genre = defaultdict(int)

    for i in range(n):
        song = Song(plays[i], i)
        songs_by_genre[genres[i]].append(song)
        time_of_genre[genres[i]] += plays[i]

    time_of_genre = list(zip(time_of_genre.keys(), time_of_genre.values()))
    time_of_genre.sort(key=lambda x: -x[1])

    answer = []
    for genre, time in time_of_genre:
        songs = songs_by_genre[genre]
        songs.sort(key=lambda x: (-x.play, x.idx))
        answer.append(songs[0].idx)
        if len(songs) >= 2:
            answer.append(songs[1].idx)

    return answer
