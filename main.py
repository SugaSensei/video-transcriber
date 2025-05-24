from moviepy.editor import VideoFileClip

video_path = "videos/sample.mp4"
video = VideoFileClip(video_path)
audio_path = "output/sample.mp3"
video.audio.write_audiofile(audio_path)