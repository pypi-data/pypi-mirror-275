import os
import time
import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import pygame
import wikipediaapi
import webbrowser
import requests
import datetime
import pytz
import google.generativeai as genai


class Parsoon:
    def __init__(self, api_key="", countrycode="IN", sound_file="output.mp3", savefile=False, ai_engine="gemini", speech_engine="gTTS", gui=False, play_sound_enabled=True, enable_openweb=True, lang="en"):
        self.ai_engine = ai_engine
        self.play_sound_enabled = play_sound_enabled
        self.speech_engine = speech_engine
        self.gui = gui
        self.recognizer = sr.Recognizer()
        self.enable_openweb = enable_openweb
        self.lang = lang
        self.savefile = savefile
        self.filename = sound_file
        self.country_code = countrycode
        self.api_of_weather = api_key
   
        
    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""

    def play_sound(self, sound_file):
        pygame.init()
        pygame.mixer.init()
        try:
            sound = pygame.mixer.Sound(sound_file)
            sound.play()
            pygame.time.wait(int(sound.get_length() * 1000))
        except pygame.error as e:
            print("Error playing sound:", e)

    def speak(self, text):
        if not text:
            print("No text to speak.")
            return
        if self.speech_engine == "gTTS":
            tts = gTTS(text=text, lang=self.lang)
            tts.save(self.filename)
            print("Speaking...")
            self.play_sound(self.filename)
            if not self.savefile:
                os.remove(self.filename)
        elif self.speech_engine == "pyttsx3":
            engine = pyttsx3.init()
            engine.say(text)
            if self.savefile:
                engine.save_to_file(text, self.filename)
            engine.runAndWait()
        else:
            print("Invalid speech engine. Please select 'pyttsx3' or 'gTTS'.")
            self.speech_engine = "pyttsx3"
            self.speak(text)

    def intcheck(self):
        try:
            requests.get("https://www.google.com/", timeout=5)
            return True
        except requests.ConnectionError:
            return False

    def open_web(self, web):
        if self.intcheck():
            try:
                requests.get(f'https://www.{web}', timeout=5)
                webbrowser.open(f'https://www.{web}')
            except requests.ConnectionError:
                if not (web.endswith('.com') or web.endswith(".in") or web.endswith(".org")):
                    nweb = f'https://www.{web}.com'
                    requests.get(nweb, timeout=5)
                    webbrowser.open(nweb)
                else:
                    print("Not found")
        else:
            print("No internet connection.")

    def ai_response(self, query, token):
        if self.ai_engine == "gemini":
            genai.configure(api_key=token)
            model = genai.GenerativeModel('gemini-1.0-pro-latest')
            response = model.generate_content(query)
            return(response.text)
        elif self.ai_engine == "ollama":    
            import SimpleVoiceAssistant.ollm as ollm
            return ollm.olama(query, model)
        else:
            print("Invalid AI engine. Please select 'test'.")
            return "Invalid AI engine."

    @staticmethod
    def wikipedia_summary(query):
        wiki = wikipediaapi.Wikipedia('en')
        try:
            page = wiki.page(query)
            if page.exists():
                summary = page.summary
                return summary
            else:
                return "Page not found. Please try another query."
        except Exception as e:
            print(f"An error occurred: {e}")
            return "Error fetching Wikipedia page."

    def search_web(self, query):
        webbrowser.open("https://www.google.com/search?q=" + '+'.join(query.split()))

    def set_reminder(self, time, task):
        pass

    def get_weather(self, location):
        pass

    def send_email(self, recipient, subject, body):
        pass

    def manage_calendar(self, action, event_details):
        pass

    def show_gui(self):
        pass

    def get_current_time(self, country_code):
        country_tz = pytz.country_timezones.get(country_code)
        if country_tz:
            tz = pytz.timezone(country_tz[0])
            current_time = datetime.datetime.now(tz=tz)
            if country_code == "IN":  # India uses 12-hour time format
                formatted_time = current_time.strftime("%I:%M %p")
            else:  # Other countries use 24-hour time format
                formatted_time = current_time.strftime("%H:%M")
            return formatted_time
        else:
            return "Invalid country code"

    def get_current_date(self, country_code):
        country_tz = pytz.country_timezones.get(country_code)
        if country_tz:
            tz = pytz.timezone(country_tz[0])
            current_date = datetime.datetime.now(tz=tz)
            formatted_date = current_date.strftime("%d-%m-%Y")
            return formatted_date
        else:
            return "Invalid country code"

    def temperature(self, location):
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = f"{base_url}q={location}&appid={self.api_of_weather}&units=metric"
        try:
            response = requests.get(complete_url)
            data = response.json()
            if data["cod"] != "404":
                main = data["main"]
                temperature = main["temp"]
                return temperature
            else:
                return "City not found"
        except Exception as e:
            print("An error occurred:", e)
            return "Error fetching weather data"

if __name__ == "__main__":
    ai = Parsoon()
    current_time = ai.get_current_time(ai.country_code)
    current_date = ai.get_current_date(ai.country_code)
    print("Current time:", current_time)
    print("Current date:", current_date)
    sound_file = ""  
    ai.play_sound(sound_file)
    ai.speak("")
    query = ai.listen()
    ai.ai_response(query,token)  # `token` is not defined here