from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def create_model():
    return ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        thinking_level="minimal"
    )

def create_chain(model):

    prompt = ChatPromptTemplate.from_messages([
        (
          "system",
          """You are a helpful AI learning assistant.

          Explain technical concepts clearly and simply.
          Use practical examples when appropriate.
          If the user is learning a programming concept, explain the idea first
          and then show a small example.
          Avoid unnecessarily long answers."""
        ),
        MessagesPlaceholder("messages")
    ])

    parser = StrOutputParser()

    return prompt | model | parser

def handle_error(e):
    error_message = str(e)

    if "429" in error_message:
        return "API quota exceeded. Please try again later."

    elif "401" in error_message or "403" in error_message:
        return "API authentication failed. Check your API key."

    elif "404" in error_message:
        return "The requested AI model was not found."

    else:
        return "An unexpected error occurred."

def chat(chain):

    messages = []

    MAX_TURNS = 5

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

            messages = messages[-(MAX_TURNS * 2):]

            print("AI:", response)

        except Exception as e:

            messages.pop()
            print("⚡", handle_error(e))

def main():

    load_dotenv()

    model = create_model()

    chain = create_chain(model)

    chat(chain)

if __name__ == "__main__":
    main()