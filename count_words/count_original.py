def count_words(input_string):
    word_list = input_string.split()
    word_count = dict()
    for word in word_list:
        word_count[word.lower()] = word_count.get(word,0) + 1
    return word_count