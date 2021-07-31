def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))

    length_list = set()
    phone_dict = dict()
    answer = True
    in_flag = False

    for phone in phone_book:
        for length in length_list:
            if phone[:length] in phone_dict.keys():
                in_flag = True
                break
        if in_flag:
            answer = False
            break

        phone_dict[phone] = True
        length_list.add(len(phone))

    return answer