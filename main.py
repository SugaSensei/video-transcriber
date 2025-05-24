from moviepy.editor import VideoFileClip

video_path = "videos/sample.mp4"

video = VideoFileClip(video_path)
video.audio.write_audiofile("output/sample_audio.wav    ")