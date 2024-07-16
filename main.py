import streamlit as st
import requests

coverage_options = {
    "Normal": ["Fighting", "Psychic", "Dark"],
    "Water": ["Ice", "Steel", "Psychic"],
    "Poison": ["Bug", "Grass", "Electric"],
    "Psychic": ["Fairy", "Ghost", "Water"],
    "Fighting": ["Electric", "Ice", "Fire"],
    "Flying": ["Steel", "Dragon", "Fighting"],
    "Grass": ["Ground", "Poison", "Rock"],
    "Ground": ["Rock", "Grass", "Dark"],
    "Bug": ["Dark", "Poison", "Ground"],
    "Rock": ["Ground", "Fire", "Electric"],
    "Dark": ["Rock", "Electric", "Poison"],
    "Fairy": ["Psychic", "Water", "Grass"],
    "Steel": ["Ice", "Ground", "Ghost"],
    "Ghost": ["Poison", "Flying", "Bug"],
    "Ice": ["Water", "Fairy", "Steel"],
    "Dragon": ["Fire", "Grass", "Psychic"],
    "Electric": ["Fairy", "Grass", "Dragon"],
    "Fire": ["Dragon", "Electric", "Fighting"]
}
pokemon=st.text_input("Pokemon Name")
try:
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon.lower()
    data = requests.get(url).json()
    name = data['name'].title()
    image_url = data['sprites']['front_default']
    base_stats = {}
    for stat in data["stats"]:
        base_stats[stat["stat"]["name"]] = stat["base_stat"]
    types = [type_data["type"]["name"].capitalize() for type_data in data["types"]]
    coverages = []
    for type in types:
        for coverage in coverage_options[type]:
            if coverage not in coverages:
                coverages.append(coverage)
    st.write(f"{name} Info")
    st.write(f"Types: {types}")
    for stat in ["hp","attack","defense","special-attack","special-defense","speed"]:
        st.write(f"{stat.title()}: {base_stats[stat]}")
    st.write(f"Coverage Options: {coverages}")
            
except:
    if pokemon!="":
        st.write("Invalid Pokemon Name")