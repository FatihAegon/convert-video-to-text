import speech_recognition as sr

ses_path = r"C:\Users\erenb\ses\audio.wav"

r = sr.Recognizer()

with sr.AudioFile(ses_path) as source:
    audio_data = r.record(source) 
    
    try:
        text = r.recognize_sphinx(audio_data)  
        print("Tanıma başarılı:", text)
    except sr.UnknownValueError:
        print("Tanınabilir bir şey bulunamadı.")
    except sr.RequestError as e:
        print(f"Tanıma servisine erişilemiyor; {e}")
