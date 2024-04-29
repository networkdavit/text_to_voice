from gtts import gTTS
import os

def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language)
    tts.save("output.mp3")  
    os.system("mpg123 output.mp3")

text = "Hello, how are you?"
text_to_speech(text)
