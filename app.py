import streamlit as st
import pandas as pd
from modules.main import all_process

st.title('JP braille Translation Demo Page')

df = pd.read_csv('./braille_jp.csv')
# st.dataframe(df)


def main():
    input = st.text_area(
        f'Enter Japanese sentence here. / こちらに翻訳したい文章を入力してください。', placeholder="This is a test sentence. / これはテスト文章です。")
    if input:
            yomi_result, result_df, braille_string, yomi_string = all_process(input, df)
            st.dataframe(result_df)
            st.write('Braille:', braille_string)
            st.write('Reading:', yomi_result)
            

if __name__ == '__main__':
    main()