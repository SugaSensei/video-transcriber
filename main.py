from moviepy.editor import VideoFileClip


clip = VideoFileClip("videos/sample.mp4")
print(f"Duration: {clip.duration} seconds")
