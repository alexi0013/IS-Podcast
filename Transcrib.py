import whisper
import os

# 1. Pfad zur Datei im Download-Ordner
download_path = os.path.expanduser("/Users/alexisarvanitidis/Documents/MasterThesis/doweneedtheory.mp3")

# 2. Whisper-Modell laden
model = whisper.load_model("tiny") 

# 3. Transkribieren
result = model.transcribe(download_path)

# 4. Transkript speichern
output_file = os.path.expanduser("/Users/alexisarvanitidis/Documents/MasterThesis/Episode1.txt")
with open(output_file, "w", encoding="utf-8") as f:
    f.write(result["text"])
