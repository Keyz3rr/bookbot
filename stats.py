def get_word_count(file_contents):
        word_count = file_contents.split()
        num_words = 0
        for word in word_count:
            num_words += 1
        return num_words