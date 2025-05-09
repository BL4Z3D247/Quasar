import speech_recognition as sr
import subprocess

def run():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("[Voice] Listening for command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"[Voice] Recognized: {command}")
        subprocess.run(["python3", "quasar.py", "run", "voice_command", "--cmd", command])
    except sr.UnknownValueError:
        print("[Voice] Could not understand the audio.")
    except sr.RequestError as e:
        print(f"[Voice] Recognition error: {e}")
