from textblob import TextBlob
import colorama
from colorama import Fore, Back, Style
import sys
import time
user_name=" "#agent's name provide during onboarding
conversation_history=[]#list of all messages entered by the user
positive_count=0#counters to track sentiment trends
negative_count=0
neutral_count=0
def show_processing_animation():
    print(f"{Fore.CYAN}","Detection sentimentclues",end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".",end="")
        sys.stdout.flush()
def analyze_sentiment(text):
    try:
        global positive_count,negative_count,neutral_count
        blob=TextBlob(text)
        sentiment=blob.sentiment.polarity
        conversation_history.append(text)

        if sentiment>0.75:
            positive_count+=1
            return f"\n {Fore.GREEN} ✨✨ Very positive sentiment detected, Agent {user_name}! (score:{sentiment:.2f})"
        elif 0.25 < sentiment <=0.75:
            positive_count +=1
            return f"\n {Fore.GREEN} 😊 Very positive sentiment detected, Agent {user_name}! (score:{sentiment:.2f})"
        elif -0.25 <= sentiment <=0.25:
            neutral_count+=1
            return f"\n {Fore.YELLOW}  😑 Neutral Sentiment detected."
        elif -0.75 <= sentiment <=0.25:
            negative_count +=1
            return "\n {Fore.RED}💔 Negative sentiment detected, Agent {user_name}, (score:{sentiment:.2f})"
        else:
            negative_count +=1
            return f"\n {Fore.RED} 💔💔 Very negative sentiment detected, Agent{user_name}, (score: {sentiment:.2f})"
    except Exception as e:
        return f"{Fore.RED} An error occured during sentiment analysis: {str(e)}"
def execute_command(command):
    if command == "summary":
        return(f"{Fore.CYAN} Mission Report: \n"
               f"{Fore.GREEN} Positive messages detected: {positive_count}\n"
               f"{Fore.RED} Negative messages detected: {negative_count}\n"
               f"{Fore.YELLOW} Neutral messages detected: {neutral_count}")
    elif command == "reset":
        conversation_history.clear()
        positive_count = negative_count = neutral_count =0
        return f"{Fore.CYAN} Mission reset ! All previous data has been cleared."
    elif command == "history":
        return "\n".join([f"{Fore.CYAN} Message {i+1}: {msg}" for i, msg in enumerate(conversion_history)])
             if conversaton_history else f"{Fore.YELLOW} no conversation history available."
    elif command == "help" :
        return {f"{Fore.CYAN}🔍Available commands:\n"
                f"- Type any sentence to analyze its sentiment.\n"
                f"-Type 'summary' to get a mission report on analyzed sentiments.\n"
                f"- Type 'reset' to clear all mission data and start fresh.\n"
                f"- Type 'history' to view all previous messages and analyses.\n"
                f"- Type 'exit' to conclude your mission and leave the chat."}  
    else:
        return f"{Fore.RED} Unknown command. Type 'help' for a list of commands."    
def get_valid_name():
    while True:
        name = input("What's your name?").strip()
        if name and name.isalpha():
            return name
        else:
            print(f"{Fore.RED} Please entr a valid name with only a alphabetic character")
def start_sentiment_chart():
    print(f"{Fore.CYAN}{Style.BRIGHT} 😃Welcome to sentiment Spy! Your personal emotion detection is here")
    global user_name
    user_name = get_valid_name()
    print(f"\n{Fore.CYAN} Nice to meet you, Agent {user_name}! Type your sentences to analyze emotions. Type 'help' for options")
    while True:
        user_input = input(f"\n{Fore.MAGENTA}{Style.BRIGHT}Agent {user_name}: {Style.RESET_ALL}").strip()
        if not user_input:
            print(f"{Fore.RED}Please enter a non-empty message or type 'help' for available commands.")
            print(execute_command(user_input.lower()))
        if user_input.lower() == "exit":
            print(f"\n{Fore.BLUE}🔛Mission complete! Exiting sentiment spy. Farewell, Agent{user_name}!")
            break
        elif user_input.lower() in ['summary','reset','history','help']:
            print(execute_command(user_input.lower()))
        else:
            show_processing_animation()
            result= analyze_sentiment(user_input)
            print(result)
if __name__ =="__main__":
    start_sentiment_chat()