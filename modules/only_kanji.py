def only_kanji(word_list):
    kanji_words_with_indices = []
    
    for index, entry in enumerate(word_list, start=1):  # Start indexing from 1
        word = entry.get('word', '')
        if any('\u4e00' <= character <= '\u9fff' for character in word):
            kanji_words_with_indices.append({index: word})

    return kanji_words_with_indices