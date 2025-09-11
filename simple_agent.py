
import os
from dotenv import load_dotenv
load_dotenv()

from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.schema import HumanMessage, AIMessage
from langchain.chat_models import ChatOpenAI

# State 구조: Annotated + add_messages 리듀서
class State(TypedDict):
    messages: Annotated[list, add_messages]


# LLM 초기화 (system_prompt 추가)
llm = ChatOpenAI(temperature=0, system_prompt="이전 대화 히스토리를 반드시 기억하고, 사용자의 이름 등 맥락을 반영해 답변하세요.")

def chatbot_node(state: State):
    # state["messages"]에는 HumanMessage/AIMessage 객체들이 순서대로 들어있음
    print("[DEBUG] 현재 대화 히스토리:")
    for m in state["messages"]:
        print(f"  - {type(m).__name__}: {getattr(m, 'content', str(m))}")
    response_msg = llm(state["messages"])
    return {"messages": [response_msg]}

# StateGraph 구성 및 체크포인터 설정
graph_builder = StateGraph(State)
graph_builder.add_node("Chatbot", chatbot_node)
graph_builder.add_edge(START, "Chatbot")
graph_builder.add_edge("Chatbot", END)

from langgraph.checkpoint.memory import MemorySaver
memory_saver = MemorySaver()
graph = graph_builder.compile(checkpointer=memory_saver)

# thread_id별 대화 persistence 예시
def run_chat(thread_id: str, user_message: str):
    config = {"configurable": {"thread_id": thread_id}}
    user_input = {"messages": [HumanMessage(content=user_message)]}
    result = graph.invoke(user_input, config=config)
    ai_msgs = [m for m in result["messages"] if isinstance(m, AIMessage)]
    return ai_msgs[-1].content if ai_msgs else None

import os
import openai
from dotenv import load_dotenv

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY") or os.getenv("API_KEY")
if not api_key:
    print("OpenAI API 키가 .env 파일이나 환경 변수에 설정되어 있지 않습니다.")
    exit()

client = openai.OpenAI(api_key=api_key)


def simple_agent():
    print("에이전트와 대화하세요. 'exit'을 입력하면 종료됩니다.")
    user_name = input("이름(또는 사용자 ID)을 입력하세요: ")
    thread_id = f"user_{user_name}"
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            print("에이전트를 종료합니다.")
            break
        try:
            agent_response = run_chat(thread_id, user_input)
            print(f"Agent: {agent_response}")
        except Exception as e:
            print(f"API 호출 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    # 콘솔 에이전트 실행
    simple_agent()
