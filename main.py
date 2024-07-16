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

def write(text):
    st.markdown(f'<span style="color:gray">{text}</span>', unsafe_allow_html=True)

pokemon=st.text_input("Pokemon Name")
try:
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon.lower().rstrip().lstrip()
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
    col1, col2 = st.columns(2)
    with col1:
        write(f"{name} Info")
        write(f"Types: {types}")
        for stat in ["hp","attack","defense","special-attack","special-defense","speed"]:
            write(f"{stat.title()}: {base_stats[stat]}")
        write(f"Coverage Options: {coverages}")
    with col2:
        st.image(image_url, width=100)  
    
except:
    if pokemon!="":
        write("Invalid Pokemon Name")

