#Import de librerías
import pandas as pd

#Lectura de los CSVs originales
df_2015 = pd.read_csv("data/world_happiness_2015.csv", sep=";")
df_2016 = pd.read_csv("data/world_happiness_2016.csv", sep=";")
df_2017 = pd.read_csv("data/world_happiness_2017.csv", sep=";")
df_2018 = pd.read_csv("data/world_happiness_2018.csv", sep=";")
df_2019 = pd.read_csv("data/world_happiness_2019.csv", sep=";")
df_2020 = pd.read_csv("data/world_happiness_2020.csv", sep=";")
df_2021 = pd.read_csv("data/world_happiness_2021.csv", sep=";")
df_2022 = pd.read_csv("data/world_happiness_2022.csv", sep=";")
df_2023 = pd.read_csv("data/world_happiness_2023.csv", sep=";")
df_2024 = pd.read_csv("data/world_happiness_2024.csv", sep=";")

#Añadimos la columna Year a cada uno de los dataframes
df_2015["Year"] = "2015"
df_2016["Year"] = "2016"
df_2017["Year"] = "2017"
df_2018["Year"] = "2018"
df_2019["Year"] = "2019"
df_2020["Year"] = "2020"
df_2021["Year"] = "2021"
df_2022["Year"] = "2022"
df_2023["Year"] = "2023"
df_2024["Year"] = "2024"

#Renombramos la solumna del fichero de 2024
df_2024.rename(columns={"Ladder score": "Happiness score"}, inplace=True)


#Unificamos los df
df_all = pd.concat([df_2015, df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022, df_2023, df_2024], axis=0)

print(df_all)

