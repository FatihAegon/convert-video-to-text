from moviepy.editor import VideoFileClip

video_path =(r"C:\Users\erenb\ses\a.mp4")

ses_path = (r"C:\Users\erenb\ses\audio.wav")

video_clip = VideoFileClip(video_path)
audio_clip = video_clip.audio

audio_clip.write_audiofile(ses_path, codec='pcm_s16le')

audio_clip.close()
video_clip.close()

print(f"Video sesi başarıyla '{ses_path}' dosyasına kaydedildi.")
