from langchain.agents import initialize_agent, Tool
import os
import openai
from langchain.llms import OpenAI
from langchain.tools import tool

openai.api_key = os.environ.get("OPENAI_API_KEY")

llm = OpenAI(temperature=0)


@tool("FAQ")
def faq(intput: str) -> str:
    """useful for when you need to answer questions about shopping policies, like return policy, shipping policy, etc."""

    return "faqqqq"


@tool("Recommend Product")
def recommend_product(input: str) -> str:
    """useful for when you need to search and recommend products and recommend it to the user"""

    return "rppp"


def search_order(input: str) -> str:
    return "订单状态：已发货；发货日期：2023-01-01；预计送达时间：2023-01-10"


tools = [

    Tool(

        name="Search Order", func=search_order,
        description="useful for when you need to answer questions about customers orders"

    ),

    recommend_product, faq]

agent = initialize_agent(
    tools, llm, agent="zero-shot-react-description", verbose=True)
# agent = initialize_agent(
#     tools, llm, agent="zero-shot-react-description", verbose=True)
# agent = initialize_agent(
#     tools, llm, agent="zero-shot-react-description", max_iterations=2, verbose=True)
question = "我衣服可以退款吗"
result = agent.run(question)
print(result)
# from langchain.chains import LLMChain
# from langchain.llms import OpenAIChat
# from langchain.prompts import PromptTemplate
# import openai
# import os

# os.environ["OPENAI_API_KEY"] = "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"
# openai.api_key = os.environ.get("OPENAI_API_KEY")

# llm = OpenAIChat(max_tokens=2048, temperature=0.5)

# multiple_choice = """

# 请针对 >>> 和 <<< 中间的用户问题，选择一个合适的工具去回答她的问题。只要用A、B、C的选项字母告诉我答案。

# 如果你觉得都不合适，就选D。

# >>> {question}<<<

# 我们有的工具包括：

# A. 一个能够查询商品信息，为用户进行商品导购的工具

# B. 一个能够查询订单信息，获得最新的订单情况的工具

# C. 一个能够搜索商家的退换货政策、运费、物流时长、支付渠道、覆盖国家的工具

# D. 都不合适

# """

# multiple_choice_prompt = PromptTemplate(template=multiple_choice, input_variables=["question"])

# choice_chain = LLMChain(llm=llm, prompt=multiple_choice_prompt, output_key="answer")

# question = "我想买一件衣服，但是不知道哪个款式好看，你能帮我推荐一下吗？"

# print(choice_chain(question))
