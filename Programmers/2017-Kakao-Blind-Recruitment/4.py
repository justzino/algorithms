notes_dict = {
    'C': 'a',
    'C#': 'b',
    'D': 'c',
    'D#': 'd',
    'E': 'e',
    'F': 'f',
    'F#': 'g',
    'G': 'h',
    'G#': 'i',
    'A': 'j',
    'A#': 'k',
    'B': 'l'
}


def get_duration(start, end):
    start_hour, start_min = map(int, start.split(':'))
    end_hour, end_min = map(int, end.split(':'))

    return (end_hour - start_hour) * 60 + end_min - start_min


def convert_note_to_code(notes):
    new_notes = notes[0]
    n = len(notes)

    for i in range(1, n):
        if notes[i] == '#':
            new_notes += '#'
        elif new_notes[-1] != '#':
            new_notes = new_notes[:-1] + notes_dict[new_notes[-1]] + notes[i]
        else:
            new_notes = new_notes[:-2] + notes_dict[new_notes[-2:]] + notes[i]

    if new_notes[-1] in notes_dict.keys():
        new_notes = new_notes[:-1] + notes_dict[new_notes[-1]]

    return new_notes


def get_played_notes(duration, notes):
    times, rest = divmod(duration, len(notes))
    new_notes = notes * times + notes[:rest]

    return new_notes


def solution(m, musicinfos):
    listen = convert_note_to_code(m)
    result = []

    for music in musicinfos:
        start, end, title, notes = music.split(',')
        duration = get_duration(start, end)
        new_notes = convert_note_to_code(notes)
        new_notes = get_played_notes(duration, new_notes)

        print(listen, duration, title, new_notes)

        if listen in new_notes:
            result.append((duration, title))

    answer = ''
    if len(result) <= 0:
        answer = '(None)'

    elif len(result) == 1:
        answer = result[0][1]

    else:
        result = sorted(result, key=lambda x: (-x[0]))
        answer = result[0][1]

    return answer
