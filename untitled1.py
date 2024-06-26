import speech_recognition as sr

# Ses dosyasının yolu
ses_path = r"C:\Users\erenb\ses\audio.wav"

# Tanıma motoru oluşturma
r = sr.Recognizer()

# Ses dosyasını yükle
with sr.AudioFile(ses_path) as source:
    audio_data = r.record(source)  # Ses dosyasını oku

    # Tanıma işlemi
    try:
        text = r.recognize_sphinx(audio_data)  # CMU Sphinx ile tanıma
        print("Tanıma başarılı:", text)
    except sr.UnknownValueError:
        print("Tanınabilir bir şey bulunamadı.")
    except sr.RequestError as e:
        print(f"Tanıma servisine erişilemiyor; {e}")