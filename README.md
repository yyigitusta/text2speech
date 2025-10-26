# 🔊 Text-to-Speech (TTS) GUI (Offline)

Bu proje, **metni konuşmaya dönüştüren** tamamen **offline** çalışan bir masaüstü uygulamadır.  
Python’un `pyttsx3` kütüphanesini kullanarak Windows’un yerel ses motorunu (SAPI5) kullanır.  
Grafik arayüz **Tkinter** ile oluşturulmuştur.

---

## 🎯 Özellikler
- 💬 Girilen metni sesli olarak okur  
- 🎙️ Sesi `.wav` dosyası olarak kaydeder  
- ⚙️ Hız, ses yüksekliği ve ses seçimi ayarlanabilir  
- 🧹 Arayüz üzerinden kolay temizlik  
- 💻 **Tamamen offline** çalışır (internet gerekmez)

---

## 🧩 Kurulum

Terminalde:
```bash
pip install pyttsx3
▶️ Çalıştırma
bash
Kodu kopyala
python src/tts_gui.py
🖥️ Arayüz Özellikleri
Buton	Açıklama
▶ Konuş	Metni sesli olarak okur
💾 WAV Kaydet	Metni ses dosyasına kaydeder
🧹 Temizle	Metin kutusunu temizler
Ses Seçimi	SAPI5 üzerinden mevcut sesleri listeler
Hız ve Ses Ayarı	Konuşma hızını ve ses seviyesini değiştirir

📂 Dosya Yapısı
text_to_speech_gui/
 ├── src/
     └── tts_gui.py

⚙️ Teknik Bilgiler
Kütüphane: pyttsx3

Motor: SAPI5 (Windows)

GUI: Tkinter

Ses formatı: .wav

💡 Geliştirme Fikirleri
MP3 formatında çıktı (pydub + ffmpeg ile)

Seçili metni otomatik okuma (clipboard listener)

Dosya içeriğini sırayla okuma (toplu TTS)

GUI temasını Fluent/Modern tarzda güncelleme

👨‍💻 Geliştirici
Yiğit Usta
🎓 Kocaeli Üniversitesi – Bilgisayar Mühendisliği
