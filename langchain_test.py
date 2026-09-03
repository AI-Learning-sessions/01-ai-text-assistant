from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

def create_model():
    return ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        thinking_level="minimal"
    )

def create_chain(model):

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a helpful AI assistant."
        ),
        MessagesPlaceholder("messages")
    ])

    parser = StrOutputParser()

    return prompt | model | parser

def chat(chain):

    messages = []

    while True:

        topic = input("You: ")

        if topic.lower() == "exit":
            break

        messages.append(
            HumanMessage(content=topic)
        )

        try:

            response = chain.invoke({
                "messages": messages
            })

            messages.append(
                AIMessage(content=response)
            )

            print("AI:", response)

        except Exception as e:

            messages.pop()

            print("Error:", e)

def main():

    load_dotenv()

    model = create_model()

    chain = create_chain(model)

    chat(chain)

if __name__ == "__main__":
    main()