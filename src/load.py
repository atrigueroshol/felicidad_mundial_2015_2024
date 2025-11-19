# FICHERO CON LAS FUNCIONES DE CARGA

#Imports
import pandas as pd

def load_csvs(lista):
    dfs = []
    for csv in lista:
        try:
            df = pd.read_csv(csv, sep=";")
            df["File"] = csv
            dfs.append(df)
        except Exception as e:
            print(f"ERROR: NO SE HA PODIDO CARGAR {csv}: {e}")

    return dfs