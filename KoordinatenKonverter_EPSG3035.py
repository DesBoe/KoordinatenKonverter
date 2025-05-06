import pandas as pd
import pyproj
import os

def convert_coordinates(input_csv):
    # Einlesen der CSV-Datei
    df = pd.read_csv(input_csv, delimiter=';')
    
    # Prüfen, ob Latitude und Longitude Spalten existieren
    if 'latitude' not in df.columns or 'longitude' not in df.columns:
        raise ValueError("Die CSV-Datei muss Spalten mit den Namen 'latitude' und 'longitude' enthalten.")
    
    # Korrigieren der Punkte in den Koordinatenwerten
    df['latitude'] = df['latitude'].astype(str).str.replace(',', '.', regex=False).astype(float)
    df['longitude'] = df['longitude'].astype(str).str.replace(',', '.', regex=False).astype(float)
    
    # Definiere die Koordinaten-Transformation
    transformer = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:3035", always_xy=True)
    
    # Koordinaten transformieren
    df['X'], df['Y'] = zip(*df.apply(lambda row: transformer.transform(row['longitude'], row['latitude']), axis=1))
    
    # Ausgabe-Dateiname erstellen
    output_csv = os.path.splitext(input_csv)[0] + "_EPSG3035.csv"
    
    # Speichern der neuen CSV-Datei
    df.to_csv(output_csv, index=False, sep=';', decimal='.')
    print(f"output saved as {output_csv}")



if __name__ == "__main__":
    print("Enter the path of the csv file that contains the coordinates in WGS84 format")
    input_csv = input()
    convert_coordinates(input_csv)