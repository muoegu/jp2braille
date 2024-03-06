from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"]

llm = OpenAI(temperature=0.7)


output_parser = CommaSeparatedListOutputParser()

template = """

I want the Kanji (漢字) converted to Katakana (カタカナ).
Please output the reading of the target Kanji. Please refer to the following dictionary entries and the context of the input sentence itself.

Input sentence: "{input_text}" 
Target Kanji: "{key_word_list}"
Dictionary entries: "{jisho_data}"

Don't output anything but a list.

Ex: 
Input: [Target1, Target2]
Output: [Reading1, Reading2]
"""

prompt = PromptTemplate(
    template=template, input_variables=["input_text", "key_word_list", "jisho_data"],
    format_instructions = output_parser.get_format_instructions()
)
chain = LLMChain(llm=llm, prompt=prompt)


def create_templeate(input_text, key_word_list, jisho_data):
    prompt_template = prompt.format(
        input_text=input_text, key_word_list=key_word_list, jisho_data=jisho_data)
    return prompt_template