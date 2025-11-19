#FICHERO CON LAS FUNCIONES DE CARGA

"""
Funcion para cargar el dataframe en un csv
"""
def df_to_csv(df):
    try:
        df.to_csv("data/world_happiness_clean.csv")
        print("SE HA CREADO EL FICHERO world_happiness_clean.csv")
    except Exception as e:
        print(f"ERROR N SE HA PODIDO CREAR EL FICHERO world_happiness_clean.csv: {e}")
    return True