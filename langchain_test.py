from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in one sentence."
)

parser = StrOutputParser()

chain = prompt | model | parser

topic = input("Enter a topic: ")

response = chain.invoke({
    "topic": topic
})

print(response)