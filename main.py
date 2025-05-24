from moviepy.editor import VideoFileClip
import speech_recognition as sr
import os

video_path = "videos/sample.mp4"
audio_path = "output/sample.wav"
text_path = "output/transcript.txt"

video = VideoFileClip(video_path)
video.audio.write_audiofile(audio_path)

recognizer = sr.Recognizer()
with sr.AudioFile(audio_path) as source:
    print("Listening to audio...")
    audio_data = recognizer.record(source)

    print("Transcribing...")
    try:
        text = recognizer.recognize_google(audio_data, language="en-IN")
        print("\n--- Transcription ---")
        print(text)

        with open(text_path, "a", encoding="utf-8") as f:
            f.write(text)
        print(f"\n transcription saved to {text_path}")

    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"could not request results from google speech recognition service; {e}")
    
os.remove(audio_path)