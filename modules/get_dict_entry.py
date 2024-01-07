from jisho_api.word import Word
import re

def get_dictionary_entries(word):
    return_list = list()
    word_results = Word.request(word)
    if word_results.meta.status == 200 and word_results.data:
        return_list.append("==========================================")
        return_list.append(f"Dictionary entry for '{word}'")

        word_results = Word.request(word)
            
        for word_config in word_results.data:
            slug = word_config.slug
            japanese = word_config.japanese
            senses = word_config.senses
            
            if re.search(
                rf"\b{re.escape(word)}(-|$)", slug):  
                readings = set()
                for japanese_word in japanese:
                    readings.add(japanese_word.reading)
                reading_string = " or ".join(readings)
                
                return_list.append('\'\'\'')
                return_list.append("If meanings are:")
                for sense in senses:
                    english_definitions = sense.english_definitions
                    parts_of_speech = sense.parts_of_speech
                    return_list.append("- " + ", ".join(english_definitions))
                    # return_list.append("POS:" + ', '.join(parts_of_speech))
                return_list.append(f"Reading should be: '{reading_string}'")
                return_list.append('\'\'\'')
    else:
        return_list.append("No words found.")

    return "\n".join(return_list)


# jisho_data = get_dictionary_entries('人気')
# print(jisho_data)