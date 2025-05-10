import pandas as pd
import os

#Pfade
metadata_path = 'episode_metadata.csv'
transcripts_path = '/Users/alexisarvanitidis/Documents/MasterThesis'  

#1.Prüfen ob Metadateien existieren
if not os.path.exists(metadata_path):
    print("Metadata file not found. Creating a default version...")

    #2.Alle Transkribierte Dateien lesen
    episodes = []
    if not os.path.exists(transcripts_path):
        raise FileNotFoundError(f"Ordner '{transcripts_path}' nicht gefunden.")

    for file in os.listdir(transcripts_path):
        if file.endswith('.txt'):
            episode_id = file.replace('.txt', '').replace('Episode', '').strip()
            episodes.append({
                'episode_id': episode_id,
                'title': '',  
                'date': 'XXXX-XX-XX',                       
                'guest': 'Guest Name',
                'duration': 'XX mins, XX seconds',
                'topic': '',
                                
            })

    #3.Metadaten speichern in csv
    metadata = pd.DataFrame(episodes)
    metadata = metadata.sort_values(by='episode_id', key=lambda col: col.astype(int))
    metadata.to_csv(metadata_path, index=False)
    print(f"Created '{metadata_path}' with {len(episodes)} entries.")

else:
    #4.Wenn Datei existiert einfach csv laden
    metadata = pd.read_csv(metadata_path)
    print(f"Loaded existing metadata with {len(metadata)} entries.")

