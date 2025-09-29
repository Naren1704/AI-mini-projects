from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
load_dotenv()
@tool
def add(a: float, b: float)-> str:
    """Useful to adds two numbers together"""
    print("tool used")
    return f"The sum of {a} and {b} is {a + b}"
def greet(name: str)-> str:
    """Useful to greet a person by name"""
    print("tool used")
    return f"Sup {name}, hope ur having a good day buddy"
# We can add the tools as we desire
# Before running this 
def main():
    model = ChatGoogleGenerativeAI(temperature=0, model="gemini-2.5-pro")
    tools = [add, greet]
    agent_executor = create_react_agent(model, tools)
    print("Whatsup! Yo I'm Jesse your AI assistant ask me anything related to calculation lemme help you out. Type 'quit' to exit")
    while True:
        user_in = input("\nYou: ").strip()
        if user_in.lower() == "quit":
            break
        print("\nJesse: ", end='')
        for chunk in agent_executor.stream({"messages": [HumanMessage(content=user_in)]}):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end='')
        print()
if __name__ == "__main__":
    main()