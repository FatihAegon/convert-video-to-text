from moviepy.editor import VideoFileClip

# Video dosyasının yolu - Çift backslash kullanarak veya raw string olarak belirtebilirsiniz
video_path =(r"C:\Users\erenb\ses\a.mp4")


# Ses dosyasının kaydedileceği yol ve dosya adı
ses_path = (r"C:\Users\erenb\ses\audio.wav")

# Video dosyasını yükle ve sesi ayır
video_clip = VideoFileClip(video_path)
audio_clip = video_clip.audio

# Ses dosyasını WAV formatında kaydet
audio_clip.write_audiofile(ses_path, codec='pcm_s16le')

# Belleği ve geçici dosyaları temizle
audio_clip.close()
video_clip.close()

print(f"Video sesi başarıyla '{ses_path}' dosyasına kaydedildi.")