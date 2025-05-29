def get_word_count(file_contents):
    word_count = file_contents.split()
    num_words = 0
    for word in word_count:
        num_words += 1
    return num_words

def get_num_characters(file_contents):
    character_count = {}
    for character in file_contents:
        character = character.lower()
        if character in character_count:
            character_count[character] = character_count[character] + 1
        else:
            character_count[character] = 1
    return character_count

def sort_on(character_count):
    return character_count["num"]

def sort_char_count(character_count):
    characters = []
    for c in character_count:
        if c.isalpha():
            c_count = {"char": c, "num": character_count[c]}
            characters.append(c_count)
    characters.sort(reverse=True, key=sort_on)
    return characters