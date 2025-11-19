#----------- IMPORTACIONES ----------------------
#Import de librerías
import pandas as pd
import pandasql as ps
#Import de funciones
import extract
import transform
import load

#----------- CARGA DE FICHEROS ----------------------
#Definimos los ficheros y los cargamos en nuestro dataframe
csvs =[]
csvs.append("data/raw/world_happiness_2015.csv")
csvs.append("data/raw/world_happiness_2016.csv")
csvs.append("data/raw/world_happiness_2017.csv")
csvs.append("data/raw/world_happiness_2018.csv")
csvs.append("data/raw/world_happiness_2019.csv")
csvs.append("data/raw/world_happiness_2020.csv")
csvs.append("data/raw/world_happiness_2021.csv")
csvs.append("data/raw/world_happiness_2022.csv")
csvs.append("data/raw/world_happiness_2023.csv")
csvs.append("data/raw/world_happiness_2024.csv")
dfs = extract.load_csvs(csvs)
df_all = pd.concat(dfs, axis=0)

#----------- TRANSFORMACIONES ----------------------
#Renombramos la columna Ladder score como Hapiness score
if "Ladder score" in df_all.columns:
    df_all = transform.transf_ladder_score(df_all)
    
#Comprobamos si hay valores nulos en Regional indicator y si hay nulos aplicamos la moda
query = "SELECT DISTINCT country FROM df_all WHERE `Regional indicator` IS NULL"
resultado = ps.sqldf(query, locals())

if not resultado.empty:
    df_all = transform.transf_regional_indicator(df_all, resultado)

#----------- CREACION DE FICHERO CSV ----------------------
load.df_to_csv(df_all)