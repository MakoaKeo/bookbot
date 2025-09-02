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