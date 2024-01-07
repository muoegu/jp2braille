from jisho_api.word import Word

# def filter_ambiguous(only_kanji):
#     def is_valid_entry(input_word):
#         try:
#             word_results = Word.request(input_word)
#             if word_results.meta.status == 200 and word_results.data:
#                 return any(
#                     len([entry for entry in word_config.japanese if entry.word == input_word]) > 1
#                     for word_config in word_results.data
#                 )
#             return False
#         except Exception as e:  # It's good to know what kind of exception occurred
#             print(f"Error while processing word '{input_word}': {e}")
#             return False

#     filtered_kanji = []
#     for word in only_kanji:
#         if is_valid_entry(word):
#             filtered_kanji.append(word)

#     return filtered_kanji

from jisho_api.word import Word
'''
def filter_ambiguous(only_kanji):
    filtered_kanji = []

    for word in only_kanji:
        try:
            word_results = Word.request(word)
            if word_results.meta.status == 200 and word_results.data:
                if any(
                    len([entry for entry in word_config.japanese if entry.word == word]) > 1
                    for word_config in word_results.data
                ):
                    filtered_kanji.append(word)
        except Exception as e:
            print(f"Error while processing word '{word}': {e}")

    return filtered_kanji
'''

def filter_ambiguous(indexed_kanji_list):
    filtered_kanji = []

    for item in indexed_kanji_list:
        for index, word in item.items():
            try:
                word_results = Word.request(word)
                if word_results.meta.status == 200 and word_results.data:
                    if any(
                        len([entry for entry in word_config.japanese if entry.word == word]) > 1
                        for word_config in word_results.data
                    ):
                        filtered_kanji.append({index: word})
            except Exception as e:
                print(f"Error while processing word '{word}': {e}")

    return filtered_kanji


