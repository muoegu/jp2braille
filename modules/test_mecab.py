import MeCab

def mecab_test(input_text):
    """
    Parses the input text using MeCab and returns a list with token information.

    Parameters:
    input_text (str): The text to be parsed.

    Returns:
    list: A list of dictionaries, each dictionary containing 'word', 'phonetic', 
        and 'pos' keys for each token in the text.
    """
    tagger = MeCab.Tagger()
    result = tagger.parse(input_text)
    tokens = result.split("\n")
    data_list = []  # 結果を格納するリスト

    for token in tokens:
        if token:  # 空文字列でないことを確認
            token_parts = token.split("\t")
            if len(token_parts) >= 2:  # リストが2つ以上の要素を持っていることを確認
                word = token_parts[0]  # 単語
                phonetic = token_parts[1]  # 読み
                readings = token_parts[2]  
                pos = token_parts[4]  # POS

                # 特殊なケースの処理
                if word in ["、", "。", "？"]:
                    phonetic = word
                    pos = "補助記号-句点" if word in ["。", "？"] else "補助記号-読点"
                elif phonetic == "オ":
                    phonetic = "ヲ"
                    pos = "助詞-格助詞"

                data_list.append({"word": word, "phonetic": phonetic, "readings":readings, "pos": pos})

    return data_list

# dict_info = mecab_test('私の')
# print(dict_info)