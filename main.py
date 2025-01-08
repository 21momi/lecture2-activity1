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
        

show_processing_animation()




