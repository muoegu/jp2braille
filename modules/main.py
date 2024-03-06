import pandas as pd
# import budoux
from .test_mecab import mecab_test
from .only_kanji import only_kanji
from .filter_ambiguous import filter_ambiguous
from .get_dict_entry import get_dictionary_entries
from .new_llm import llm_test2
from .hira2kana import hira2kana

from .template import create_templeate


def split22lists(filtered_list):
    ambiguous_index = []
    ambiguous_list = []
    ambiguous_index_new = []

    for item in filtered_list:
        for key, value in item.items():
            ambiguous_index.append(key)
            ambiguous_list.append(value)

    for i in ambiguous_index:
        a = i - 1
        ambiguous_index_new.append(a)

    return ambiguous_index_new, ambiguous_list 

def get_jisho_data(filtered_kanji):
    return "\n".join([get_dictionary_entries(kanji) for kanji in filtered_kanji])


def add_index(indices, katakana_words):
    """Convert two lists into a list of dictionaries."""
    return [{index: word} for index, word in zip(indices, katakana_words)]


def update_phonetic(original_list, update_list):
    """Update the phonetic values in the original list based on the update list."""
    for update_dict in update_list:
        for index, new_phonetic in update_dict.items():
            if 0 <= index < len(original_list):
                original_list[index]['phonetic'] = new_phonetic
    return original_list


def get_yomi(updated_list):
    """Join all phonetic values from the list into a single string."""
    phonetics = [entry['phonetic'] for entry in updated_list]
    return ''.join(phonetics)


def convert2kana(input_text): #, context
    mecab_result = mecab_test(input_text)
    only_kanji_r = only_kanji(mecab_result)
    filtered_kanji = filter_ambiguous(only_kanji_r)
    indices, filtered_kanji = split22lists(filtered_kanji)
    jisho_data = get_jisho_data(filtered_kanji)
    llm_result, prompt_text = llm_test(input_text, filtered_kanji, jisho_data) #,context
    katakana_words = hira2kana(llm_result)
    indexed_result = add_index(indices, katakana_words)
    updated_list = update_phonetic(mecab_result, indexed_result)
    yomi_result = get_yomi(updated_list)
    return yomi_result

# convert2kana('これは文章。')


def create_braille_dict(df):
    return {row["kana"]: {"braille": row["braille"], "rep": row["rep"]} for _, row in df.iterrows()}

def list_to_dataframe(data_with_braille):
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data_with_braille)
    return df.T

def get_data(result_df):
    braille_list = result_df.loc["braille"].tolist()
    braille_string = "  ".join(braille_list)
    yomi_list = result_df.loc["phonetic"].tolist()
    yomi_string = "  ".join(yomi_list)
    return braille_string, yomi_string

def convert2braille(word_list, braille_dict):
    for item in word_list:
        phonetic = item.get('phonetic', '')
        rep_string = ''.join(str(braille_dict.get(ch, {'braille': ch})['braille']) for ch in phonetic)
        item['braille'] = rep_string
    return word_list


def all_process(input_text, df):#,context
    mecab_result = mecab_test(input_text)
    only_kanji_r = only_kanji(mecab_result)
    filtered_kanji = filter_ambiguous(only_kanji_r)
    indices, filtered_kanji = split22lists(filtered_kanji)
    jisho_data = get_jisho_data(filtered_kanji)
    # llm_result, prompt_text = llm_test(input_text, filtered_kanji, jisho_data)#,context
    template_result = create_templeate(input_text, filtered_kanji, jisho_data)
    llm_result = llm_test2(template_result)
    # katakana_words = hira2kana(llm_result)
    indexed_result = add_index(indices, llm_result)
    updated_list = update_phonetic(mecab_result, indexed_result)
    yomi_result = get_yomi(updated_list)
    braille_dict = create_braille_dict(df)
    data_with_braille = convert2braille(updated_list, braille_dict)
    result_df = list_to_dataframe(data_with_braille)
    braille_string, yomi_string = get_data(result_df)
    return yomi_result, result_df, braille_string, yomi_string