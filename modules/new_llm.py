# LLM ラッパーをインポート
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain_community.llms import OpenAI
from dotenv import load_dotenv
import os
from langchain.prompts import PromptTemplate


load_dotenv()

os.environ["OPENAI_API_KEY"]



# LLM ラッパーを初期化
llm = OpenAI(temperature=0.7)

from langchain.llms import OpenAI

# LLM ラッパーを初期化
llm = OpenAI(temperature=0.7)


def llm_test2(template):
    prediction = llm(template)
    result = prediction.strip()
    return result