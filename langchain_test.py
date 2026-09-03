from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    thinking_level = "minimal"
)

prompt = ChatPromptTemplate.from_messages([
  ( 
    "system",
    "You are a helpful AI assistant."
  ),
  MessagesPlaceholder("messages"),
  (
     "human",
     "{topic}"
  )
])

parser = StrOutputParser()
chain = prompt | model | parser
messages = []

while True:

  topic = input("Enter a topic: ")

  if topic.lower() == "exit":
      break

  messages.append(
     HumanMessage(content=topic)
  )

  try:
      response = chain.invoke({
          "messages": messages,
          "topic": topic
      })

      messages.append(
        AIMessage(content=response)
      )

      print("AI:", response)

  except Exception as e:
     messages.pop()
     print("Error:", e)