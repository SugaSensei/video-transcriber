from moviepy.editor import VideoFileClip
import speech_recognition as sr

video_path = "videos/sample.mp4"
video = VideoFileClip(video_path)
audio_path = "output/sample.mp3"
video.audio.write_audiofile(audio_path)

recognizer = sr.Recognizer()
with sr.AudioFile(audio_path) as source:
    print("Listening to audio...")
    audio_data = recognizer.record(source)

    print("Transcribing...")
    try:
        text = recognizer.recognize_google(audio_data)
        print("\n--- Transcription ---")
        print(text)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"could not request results from google speech recognition service; {e}")
    
os.remove(audio_path)