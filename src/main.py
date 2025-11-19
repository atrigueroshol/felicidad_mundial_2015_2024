#Import de librerías
import pandas as pd
#Import de funciones
import load, transform

#Definimos los ficheros y los cargamos en nuestro dataframe
csvs =[]
csvs.append("data/world_happiness_2015.csv")
csvs.append("data/world_happiness_2016.csv")
csvs.append("data/world_happiness_2017.csv")
csvs.append("data/world_happiness_2018.csv")
csvs.append("data/world_happiness_2019.csv")
csvs.append("data/world_happiness_2020.csv")
csvs.append("data/world_happiness_2021.csv")
csvs.append("data/world_happiness_2022.csv")
csvs.append("data/world_happiness_2023.csv")
csvs.append("data/world_happiness_2024.csv")
dfs = load.load_csvs(csvs)
df_all = pd.concat(dfs, axis=0)

#Renombramos la columna Ladder score como Hapiness score
if "Ladder score" in df_all.columns:
    df_all = transform.transf_ladder_score(df_all)




# #Renombramos la solumna del fichero de 2024
# df_2024.rename(columns={"Ladder score": "Happiness score"}, inplace=True)

# #Unificamos los df
# df_all = pd.concat([df_2015, df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022, df_2023, df_2024], axis=0)

# #Transformación de los nulos en la columna Regional Indicator
# moda_greece = df_all[df_all["Country"] == "Greece"]["Regional indicator"].mode()[0]
# df_all.loc[(df_all["Country"] == "Greece") & (df_all["Regional indicator"].isnull()), "Regional indicator"] = moda_greece

# moda_cyprus = df_all[df_all["Country"] == "Cyprus"]["Regional indicator"].mode()[0]
# df_all.loc[(df_all["Country"] == "Cyprus") & (df_all["Regional indicator"].isnull()), "Regional indicator"] = moda_cyprus

# moda_gambia = df_all[df_all["Country"] == "Gambia"]["Regional indicator"].mode()[0]
# df_all.loc[(df_all["Country"] == "Gambia") & (df_all["Regional indicator"].isnull()), "Regional indicator"] = moda_gambia

# print(df_all)

