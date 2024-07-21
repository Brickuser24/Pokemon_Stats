import streamlit as st
import requests

with open("Pokedex.txt", "r") as f:
    read=f.read()
    options=read.split("\n")
    f.close()

def pokemon_analysis(pokemon):
    print(pokemon.capitalize())
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon.lower()
    data = requests.get(url).json()
    base_stats = []
    bst=0
    for stat in data["stats"]:
        base_stats.append([stat["base_stat"],stat["stat"]["name"]])
        if stat["stat"]["name"]!="hp":
            bst+=stat["base_stat"]
    st.write(f":red[{base_stats}]")
    major_offense=max([base_stats[1],base_stats[3]])
    minor_offense=min([base_stats[1],base_stats[3]])
    if major_offense[0]>=0.18*bst:
        if major_offense[0]*0.9<=minor_offense[0]:
            st.write(":red[Mixed Attacker]")
        elif major_offense[1]=="attack":
            st.write(":red[Physical Attacker]")
        else:
            st.write(":red[Special Attacker]")
    else:
        st.write(":red[Defensive]")

pokemon=st.selectbox("Pokemon Name", placeholder="Select a Pokemon", options=options)
pokemon_analysis(pokemon)
