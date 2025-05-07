import pandas as pd

# Bereinigte Texte laden
df_cleaned = pd.read_csv('check_cleaning.csv')

# Metadaten mit Delimeter als Trenner
df_meta = pd.read_csv('MetadataIS.csv', sep=';', quotechar='"', on_bad_lines='skip')
df_meta.columns = df_meta.columns.str.strip().str.replace('\ufeff', '', regex=True)

# Sicherstellen, dass episode numerisch ist
df_meta['episode_id'] = pd.to_numeric(df_meta['episode_id'], errors='coerce')
df_cleaned['episode_id'] = pd.to_numeric(df_cleaned['episode_id'], errors='coerce')

# Merging Prozess
df_combined = pd.merge(df_meta, df_cleaned, on='episode_id', how='inner')

# Export in .csv Datei
df_combined.to_csv('prepared_data.csv', index=False)
print("✅ Export abgeschlossen: prepared_data.csv gespeichert.")
