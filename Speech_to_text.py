import speech_recognition as sr
import pyttsx3

src = sr.Recognizer() 
engine = pyttsx3.init()

while True:
    try:
        with sr.Microphone(1) as source1:

            src.adjust_for_ambient_noise(source1,duration=0.2)
            audio = src.listen(source1)
            txt = src.recognize_google(audio)
            txt = txt.lower()

    except sr.RequestError as re:
        print('Request Error')
    except sr.UnknownValueError as uve:
        print('Unknown value error')
