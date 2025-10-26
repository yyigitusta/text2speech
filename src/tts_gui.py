import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import pyttsx3

class TTSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text → Speech (Offline TTS)")
        self.root.geometry("800x600")

        # TTS engine
        self.engine = pyttsx3.init()  # Windows: SAPI5
        self.voices = self.engine.getProperty("voices")

        # UI
        top = tk.Frame(root, padx=10, pady=10)
        top.pack(fill="x")

        tk.Label(top, text="Ses:").pack(side="left")
        self.voice_var = tk.StringVar()
        self.voice_menu = tk.OptionMenu(top, self.voice_var, *[v.name for v in self.voices])
        self.voice_menu.config(width=25)
        self.voice_menu.pack(side="left", padx=8)

        tk.Label(top, text="Hız:").pack(side="left", padx=(20,0))
        self.rate_scale = tk.Scale(top, from_=100, to=250, orient="horizontal")
        self.rate_scale.set(self.engine.getProperty("rate"))
        self.rate_scale.pack(side="left")

        tk.Label(top, text="Ses Yüksekliği:").pack(side="left", padx=(20,0))
        self.vol_scale = tk.Scale(top, from_=0, to=100, orient="horizontal")
        self.vol_scale.set(int(self.engine.getProperty("volume") * 100))
        self.vol_scale.pack(side="left")

        mid = tk.Frame(root, padx=10, pady=10)
        mid.pack(fill="both", expand=True)
        self.text_in = scrolledtext.ScrolledText(mid, wrap="word", height=18)
        self.text_in.pack(fill="both", expand=True)

        bottom = tk.Frame(root, padx=10, pady=10)
        bottom.pack(fill="x")
        tk.Button(bottom, text="▶ Konuş", width=16, bg="#4CAF50", fg="white",
                  command=self.speak).pack(side="left", padx=6)
        tk.Button(bottom, text="💾 WAV Kaydet", width=16, bg="#2196F3", fg="white",
                  command=self.save_wav).pack(side="left", padx=6)
        tk.Button(bottom, text="🧹 Temizle", width=12, command=lambda: self.text_in.delete("1.0", "end")).pack(side="left", padx=6)

        # varsayılan ses
        if self.voices:
            self.voice_var.set(self.voices[0].name)

    def _apply_settings(self):
        # Voice
        sel = self.voice_var.get()
        for v in self.voices:
            if v.name == sel:
                self.engine.setProperty("voice", v.id)
                break
        # Rate & Volume
        self.engine.setProperty("rate", int(self.rate_scale.get()))
        self.engine.setProperty("volume", float(self.vol_scale.get()) / 100.0)

    def speak(self):
        text = self.text_in.get("1.0", "end").strip()
        if not text:
            messagebox.showwarning("Uyarı", "Lütfen metin gir.")
            return
        self._apply_settings()
        self.engine.stop()
        self.engine.say(text)
        self.engine.runAndWait()

    def save_wav(self):
        text = self.text_in.get("1.0", "end").strip()
        if not text:
            messagebox.showwarning("Uyarı", "Lütfen metin gir.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".wav",
                                            filetypes=[("WAV", "*.wav")],
                                            title="WAV olarak kaydet")
        if not path:
            return
        self._apply_settings()
        try:
            self.engine.save_to_file(text, path)
            self.engine.runAndWait()
            messagebox.showinfo("Tamam", f"Kaydedildi:\n{path}")
        except Exception as e:
            messagebox.showerror("Hata", str(e))

def main():
    root = tk.Tk()
    app = TTSApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
