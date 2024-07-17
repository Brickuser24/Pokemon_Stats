import streamlit as st
import requests

coverage_options = {
    "Normal": (["Fighting", "Psychic", "Dark"],"WhiteSmoke"),
    "Water": (["Ice", "Steel", "Psychic"],"DodgerBlue"),
    "Poison": (["Bug", "Grass", "Electric"],"MediumOrchid"),
    "Psychic": (["Fairy", "Ghost", "Water"],"HotPink"),
    "Fighting": (["Electric", "Ice", "Fire"],"Brown"),
    "Flying": (["Steel", "Dragon", "Fighting"],"PowderBlue"),
    "Grass": ["Ground", "Poison", "Rock"],
    "Ground": ["Rock", "Grass", "Dark"],
    "Bug": ["Dark", "Poison", "Ground"],
    "Rock": ["Ground", "Fire", "Electric"],
    "Dark": ["Rock", "Electric", "Poison"],
    "Fairy": ["Psychic", "Water", "Grass"],
    "Steel": ["Ice", "Ground", "Ghost"],
    "Ghost": (["Poison", "Flying", "Bug"],"RebeccaPurple"),
    "Ice": ["Water", "Fairy", "Steel"],
    "Dragon": (["Fire", "Grass", "Psychic"],"MediumBlue"),
    "Electric": ["Fairy", "Grass", "Dragon"],
    "Fire": ["Dragon", "Electric", "Fighting"]
}

def write(text,color="gray"):
    st.write(f':{color}[{text}]')

pokemon=st.text_input("Pokemon Name", placeholder="Enter a Pokemon's name")
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
        for coverage in coverage_options[type][0]:
            if coverage not in coverages:
                coverages.append(coverage)
    col1, col2 = st.columns(2)
    with col1:
        write(f"{name} Info")
        types_string=":gray[Types:] "
        for type in types:
            types_string+=f'<span style="color:{coverage_options[type][1]}">{type}</span>'+', '
        st.markdown(types_string[0:-2:], unsafe_allow_html=True)
        for stat in ["hp","attack","defense","special-attack","special-defense","speed"]:
            write(f"{stat.title()}: {base_stats[stat]}","violet")
        write(f"Coverage Options: {coverages}","blue")
    with col2:
        st.image(image_url, width=100)  
    
except:
    if pokemon!="":
        write("Invalid Pokemon Name")
    else:
        write("Guidelines for use:")
        write("-Both uppercase and lowercase work")
        write("-Ensure no spaces between words. Try to replace them with '-'")
        write("-Search groudon-primal instead of primal groudon, etc.")

