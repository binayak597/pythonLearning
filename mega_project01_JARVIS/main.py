import os
import webbrowser
import requests
import musicLibrary
import speech_recognition as sr
import pyttsx3
from openai import OpenAI
from gtts import gTTS
import pygame

engine = pyttsx3.init()
newsApi = "<your_news_api_key>"
api_key = "<your_api_key>"

def sayBoy_old(text):

    engine.say(text)
    engine.runAndWait()


def sayBoy(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

     # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")


# integrate AI for better result
def aiProcess(c):

    
    client = OpenAI(
        api_key = api_key
    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named jarvis and skilled in all type of general tasks like alexa and google cloud"},
            {
                "role": "user",
                "content": c
            }
        ]
    )

    return completion.choices[0].message.content



def executeCommand(command):

    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in command.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://linkdin.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in command.lower():
        r = requests.get(f"https://newsapi.org/v2/everything?q=Apple&from=2024-11-11&sortBy=popularity&apiKey={newsApi}")

        # Check if the request was successful (status code 200)
        if r.status_code == 200:
            # Parse the response as JSON
            data = r.json()
            
            # Extract the 'articles' list
            articles = data.get("articles", [])


            # using list comprehension
            # titles = [article.get("title") for article in articles if article.get("title")]

            # for title in titles:
            #     sayBoy(title)
            
            # print the headline
            for article in articles:
                # sayBoy(article.get("title"))
                sayBoy(article["title"])

        else:
            print(f"Failed to fetch articles. Status Code: {r.status_code}")
            print(f"Reason: {r.reason}")

    else:

        # let openAI to handle the query
        result = aiProcess(command)
        sayBoy(result)



if __name__ == "__main__":

    sayBoy("Initializing Jarvis...")
    
    while True:

        # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing...")
        

        # recognize speech using Google
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                word = r.recognize_google(audio)
                print(word)
                #it will going to only reply for the hook word

                if word.lower() == "jarvis":
                    sayBoy("Ya")

                    with sr.Microphone() as source:
                        print("Jarvis active...")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)
                        executeCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))