import os
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import nltk

# NLTK Stoppwörter laden
nltk.download('stopwords')

# Tokenizer definieren 
tokenizer = RegexpTokenizer(r'\w+')

# Textbereinigungsprozess, Zeilenumbrüche rau, nur Kleinbuchstaben und Leerzeichen
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\n', ' ', text) 
    text = re.sub(r'[^a-zA-ZäöüÄÖÜß ]', '', text)  
    tokens = tokenizer.tokenize(text)  
    tokens = [word for word in tokens if word not in stopwords.words('english')] 
    return ' '.join(tokens)

# Transkripte einlesen
transcripts_path = '.'
transcripts = {}
for file in os.listdir(transcripts_path):
    if file.endswith('.txt') and file.startswith('Episode'):
        with open(os.path.join(transcripts_path, file), 'r', encoding='utf-8') as f:
            transcripts[file.replace('.txt', '').replace('Episode', '').strip()] = f.read()

print(f"✅ {len(transcripts)} Transkripte erfolgreich geladen.")

# Bereinigung und Speicherung, max. 500 Zeichen
data = []
for ep_id, text in transcripts.items():
    cleaned = clean_text(text)
    data.append({
        'episode_id': ep_id,
        'original_text': text[:500],   
        'cleaned_text': cleaned[:500]  
    })

df = pd.DataFrame(data)
df.to_csv('check_cleaning.csv', index=False)
print("✅ Bereinigte Texte gespeichert in: check_cleaning.csv")
