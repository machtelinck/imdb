import streamlit as st
st.title("Bonjour Cinéphile , installe-toi et trouve ton film pour ce week-end !!!")
import pymongo 
import pandas as pd
import json
import csv
from pymongo import MongoClient
import matplotlib as plt



# Connect to your MongoDB database
client = MongoClient("mongodb://localhost:27017") 
movie_collection =client.films.sc
# Import the FuzzyWuzzy library
from fuzzywuzzy import process

# Importez les bibliothèques nécessaires
from pymongo import MongoClient
import streamlit as st






actors = list(movie_collection.distinct("Acteurs"))

# Use the st.text_input() function to create a text input field




# Récupérez les paramètres de la sidebar de Streamlit

score = st.sidebar.slider("Score",min_value= 8.0 , max_value=9.3,step= 0.1)
comparison_score = st.sidebar.radio("Score", ("supérieure", "inférieure"))
duration = st.sidebar.slider("Durée",min_value = 46 , max_value=238 , step = 1)
comparison = st.sidebar.radio("Durée", ("supérieure", "inférieure"))

actors = movie_collection.distinct("Acteurs")
liste_genre = movie_collection.distinct("Genre")
beta = []
gamma = []
for elt in liste_genre:
    beta.append(str(elt).split(','))
for element in beta:
    for Why in element:
        gamma.append(Why)
gamma = list(set(gamma))


beta2 = []
liste_acteurs = []

for elt in actors:
    beta2.append(str(elt).split(','))
for element in beta2:
    for Why in element:
        liste_acteurs.append(Why)
liste_acteurs = list(set(liste_acteurs))
liste_acteurs.insert(0,'vide')
gamma.insert(0,'vide')
# Use the st.auto_complete() function to create a text input field
# with autocompletion for the actor names
actor = st.sidebar.selectbox("Nom de l'acteur", liste_acteurs)


genre = st.sidebar.selectbox("Genre",gamma)
title = st.sidebar.text_input("Titre du film")

# Créez la requête MongoDB pour filtrer les films en fonction des paramètres spécifiés
query = {}
if title:
    query["title"] = title
if score:
    if comparison_score == "supérieure":
        query["Score"] = {"$gt": score}
    elif comparison_score == "inférieure":
        query["Score"] = {"$lt": score}
if actor != 'vide':
    query["Acteurs"] = {"$regex" :actor}
if duration:
    # Utilisez l'opérateur $gt ou $lt en fonction de l'option choisie dans le radio field
    if comparison == "supérieure":
        query["duree"] = {"$gt": duration}
    elif comparison == "inférieure":
        query["duree"] = {"$lt": duration}
if genre != 'vide':
    query["Genre"] = {"$regex":genre}

# Exécutez la requête et récupérez les résultats
results = movie_collection.find(query)
resultos = movie_collection.count_documents(query)
# Affichez les résultats dans le corps principal de Streamlit

if resultos > 0:
    # Affichez les résultats dans le corps principal de Streamlit
    st.write("Voici les films trouvés :")

    st.dataframe((pd.DataFrame(list(results)).drop(columns="_id")))
else:
    # Affichez un message personnalisé si aucun résultat n'a été trouvé
    st.write("il semble que nous n'avons rien trouver") 


df = pd.DataFrame(columns=['genre', 'percentage'])

# Loop through the genres and calculate the percentage of films in each genre
for elt in gamma:
    az = movie_collection.count_documents({"Genre" : {"$regex" : elt}})
    percentage = (az*100)/250
    # Add a new row to the DataFrame with the genre name and percentage
    df = df.append({'genre': elt, 'percentage': percentage}, ignore_index=True)

show_chart = st.checkbox("Show chart")

# Use the bar chart function to plot the data
if show_chart:
    st.bar_chart(df, x="genre", y="percentage")
    show_chart2 = st.checkbox("explain")
    if show_chart2:
        st.write("sur-representation des drama, donc la durée moyenne calculée par genre est biaisé  le total ne fait pas 100 pourcent comme un film a plusieurs genre")

















































































































































    











