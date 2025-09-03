def get_num_words(body):
    num_words = len(body.split())

    return num_words


def get_character_count(body):
    character_count = {}
    words = body.split()
    for word in words:
        lc_let = word.lower()
        for letter in lc_let:
            if letter not in character_count:
                character_count[letter] = 1
            else:
                character_count[letter] += 1
    return character_count


def get_sorted_list(character_count):
    def sort_on(items):
        return items["num"]

    dict_list = []
    for ch, n in character_count.items():
        dict_list.append({"char": ch, "num": n})

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
