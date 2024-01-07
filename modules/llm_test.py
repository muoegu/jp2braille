from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['API_KEY']

output_parser = CommaSeparatedListOutputParser()

#Context:{context}
template = """
I have a Japanese sentence："{input_text}" 

I want the Kanji(Chinese characters) in the sentence converted to Katakana.
Target Kanji："{key_word_list}"

Please output the reading of the target Kanji, referring to the dictionary, and the context of the sentence itself.

Please reffer following dictionary entries.
"{jisho_data}"

Don't output anything but list.
Please output just only one anser as corresponding kana list, no need to describe answer.
ex: [yomi1, yomi2]
"""

prompt = PromptTemplate(
    template=template, input_variables=["input_text", "key_word_list", "jisho_data"],
    format_instructions = output_parser.get_format_instructions()
)
#,'context'

def llm_test(input_text, key_word_list, jisho_data): #, context
    prompt_text = prompt.format(
        input_text=input_text, key_word_list=key_word_list, jisho_data=jisho_data
    )#,context=context
    llm = OpenAI(model_name="gpt-3.5-turbo")  # text-davinci-003
    result = llm(prompt_text)
    return result, prompt_text