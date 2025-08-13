import asyncio
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from share.stt import speech_to_text
from share.model import query_ollama
from share.speech import speak_edge
from tools.weather import get_current_weather
from tools.date_time import get_current_time
from tools.search import search_google
from tools.video import play_youtube_video
from tools.file import search_and_open_file
from tools.system_monitor import open_system_monitor


chat_history = []  # using list instead of string for structured memory
system_stat = ["system status", "memory usage", "processor usage", "system monitor", "cpu usage", "check btop"]
def matches_any(user_input: str, keywords: list) -> bool:
    return any(phrase in user_input.lower() for phrase in keywords)


def build_prompt():
    return "\n".join(chat_history) + "\n"

if __name__ == "__main__":
    print("VERONICA Assistant Ready!")
    while True:
        print("Prompt (y/n): ")
        y_n = input().strip().lower()
        
        if y_n == 'y':
            # For voice input:
            user_input = speech_to_text()

            # For manual typing:
            # user_input = input("🧍 You: ")

            if not user_input:
                continue

            if "weather" in user_input.lower():
                chat_history.append(f"Human: {user_input}")
                response = get_current_weather()
                print("🤖 VERONICA:", response)

            elif "time" in user_input.lower() or "date" in user_input.lower():
                chat_history.append(f"Human: {user_input}")
                response = get_current_time()
                print("🤖 VERONICA:", response)

            elif user_input.lower().startswith("search"):
                chat_history.append(f"Human: {user_input}")
                query = user_input.lower().split("search", 1)[1].strip()
                response = search_google(query=query)
                print("🤖 VERONICA:", response)

            elif "video" in user_input.lower() or "play" in user_input.lower():
                chat_history.append(f"Human: {user_input}")
                query = user_input[5:].strip()
                response = play_youtube_video(query=query)
                print("🤖 VERONICA:", response)

            elif user_input.lower().startswith("open"):
                chat_history.append(f"Human: {user_input}")
                query = user_input[5:].strip()
                response = search_and_open_file(query=query)
                print("🤖 VERONICA:", response)

            elif matches_any(user_input=user_input,keywords=system_stat):
                chat_history.append(f"Human: {user_input}")
                response = open_system_monitor()
                print("🤖 VERONICA:", response)

            else:
                chat_history.append(f"Human: {user_input}")
                prompt = build_prompt()

                response = query_ollama(prompt)
                print("🤖 VERONICA:", response)

            chat_history.append(f"Assistant: {response}")
            asyncio.run(speak_edge(response))
            print()

        elif y_n == 'n':
            print("👋 VERONICA saying bye bye...")
            break
